# Generated by Django 4.2.1 on 2023-07-01 10:58

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_author_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(crop=None, default='media/defaults/default_profile_pic.jpg', force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[50, 80], upload_to='authors'),
        ),
        migrations.AlterField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('U', 'Up Vote'), ('D', 'Down Vote')], max_length=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
            ],
        ),
    ]
