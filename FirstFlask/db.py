import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime,Text, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine=sqlalchemy.create_engine('sqlite:///blog.sqlite')

db_session=scoped_session(sessionmaker(bind=engine))
Base=declarative_base()
Base.query=db_session.query_property()

class User(Base):
    _tablename='users'
    id=Column(Integer, primary_key=True)
    first_name=Column(String(50))
    last_name=Column(String(50))
    email=Column(String(120), unique=True)

    def __init__(self, first_name=None, last_name=None, email=None):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email

    def __repr__(self):
        return '<User {} {} {}>'.format(self.first_name, self.last_name, self.email)
    
class Post(Base):
    _tablename='posts'
    id=Column(Integer, primary_key=True)
    title=Column(String(150))
    published=Column(DateTime)
    content=Column(Text)
    userid=Column(Integer, ForeignKey('user.id'))

    def __init__(self, title=None, published=None, content=None, userid=None):
        self.title=title
        self.published=published
        self.content=content
        self.userid=userid

    def __repr__(self):
        return '<Post {} >'.format(self.title)
    