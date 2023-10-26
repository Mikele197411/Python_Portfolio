import csv
import datetime
from db import User, Post, db_session
u=User

posts_list=[]

with open('example.csv', 'r', encoding='utf-8') as f:
    fields=['title', 'published', 'content', 'email', 'first_name', 'last_name']
    reader=csv.DictReader(f, fields, delimiter=';')
    for row in reader:
        row['published']=datetime.datetime.strftime(row['published'], '%d/%m/%Y, %H:%M:%S')
        author=u.query.filter(User.email==row['email'])
        posts_list.append(row)

for post_data in posts_list:
    post=Post(post_data['title'], post_data['published'], post_data['content'], post_data['user_id'])
    db_session.add(post)

db_session.commit()