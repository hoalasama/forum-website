cách chạy forumweb
```bash
cd forumweb
```

```bash
pip install virtualenv
```

```bash
virtualenv env
```

sau khi đã cài virtualenv, sau này chỉ cần chạy lại từ dòng này 

```bash
env\scripts\activate
```

không cần chạy lại dòng này từ lần thứ 2

```bash
pip install -r requirements.txt
```

run server : 
```bash
python manage.py runserver
```
server : http://127.0.0.1:8000/
admin site : http://127.0.0.1:8000/admin/ 
admin account : 
```bash
admin
```
password : 
```bash
lmaolmao
```
front-end : static, templates
##
when picking a function to do, add "your-name is working on" after the function, EX  "search : lmao is working on"
##
expected function
##
search : ✅
##
edit post : ✅
##
hide comment, reply area : ✅
##
edit comment, reply : ✅
##
view user info : ✅
##
edit user info : ✅
##
view user in post, comment, reply : ✅
##
show tag in post : ✅
##
upvote, downvote : user can upvote and downvote, but cant cancel it, 
here some document for upvote, downvote: https://simpleisbetterthancomplex.com/tutorial/2016/10/13/how-to-use-generic-relations.html
##
posts with tag list : ✅
##
keep scroll position after voting : ✅
##
post with picture : ✅
##
change language : guide : https://djangowaves.com/tutorial/multiple-languages-in-Django/
##
following the post :
##
notification for new comment in following post :
##
notification when someone reply your comment : 
##
notification on new reply in comment that you replied :
##
role : 
##
report post, category, bug :
##
(optional) show current popular posts :
##
user point for ranking :
##
advanced function 
##
use chatgpt to correct the user post, comment, reply :  
##
bot answer user post :
##
click on IT keyword in post, comment, reply to see meaning of it : 
##
(if possible) English test automatically generated base on user previous test:
##
user can save words that easy to forget : 
##
click on the word to hear it : 
##
(optional) reward by cash monthly to top 3 user by point :
##
provide grammar check, listening : 
##
alert in post when uploading if grammar is wrong : 
##
alert in comment when uploading if grammar is wrong : 
##
