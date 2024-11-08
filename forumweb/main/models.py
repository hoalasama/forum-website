from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField
from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager
from django.shortcuts import reverse
from django.utils.crypto import get_random_string
from django.core.validators import EmailValidator

User = get_user_model()

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    bio = HTMLField(default='none')
    points = models.IntegerField(default=0)
    email = models.EmailField(unique=False,default="example@gmail.com", validators=[EmailValidator(message="Invalid email format")])
    profile_pic = ResizedImageField(size=[400, 400], quality=100, upload_to="authors", default="defaults/default_user.png", null=True, blank=False)
    ROLES = (
        ('user','User'),
        ('teacher','Teacher'),
        ('admin','Admin'),
    )
    roles = models.CharField(max_length=50, choices=ROLES, default="user")
    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    description = models.TextField(default="description")

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("posts", kwargs={
            "slug":self.slug
        })
    
    @property
    def num_posts(self):
        return Post.objects.filter(categories=self).count()

    @property
    def last_post(self):
        return Post.objects.filter(categories=self).latest("date")
    
class Reply(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:100]
    
    class Meta:
        verbose_name_plural = "replies"

class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    replies = models.ManyToManyField(Reply, blank=True)

    def __str__(self):
        return self.content[:100]

class Post(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = HTMLField()
    categories = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)

    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )
    tags = TaggableManager()
    comments = models.ManyToManyField(Comment, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            random_string = get_random_string(length=8)
            self.slug = f"{base_slug}-{random_string}"
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_vote_count(self):
        upvotes = Vote.objects.filter(post=self, activity_type=Vote.UP_VOTE).count()
        downvotes = Vote.objects.filter(post=self, activity_type=Vote.DOWN_VOTE).count()
        return upvotes - downvotes
    
    def get_url(self):
        return reverse("detail", kwargs={
            "slug":self.slug
        })
    
    class Meta:
        ordering = ['-date']

    @property
    def num_comments(self):
        return self.comments.count()
    
    @property
    def last_reply(self):
        return self.comments.latest("date")
    
class Vote(models.Model):
    UP_VOTE = 'U'
    DOWN_VOTE = 'D'
    ACTIVITY_TYPES = (
        (UP_VOTE, 'Up Vote'),
        (DOWN_VOTE, 'Down Vote'),
    )

    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)  
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)

    class Meta:
        unique_together = ('user', 'post')

