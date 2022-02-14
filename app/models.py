from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

class Quote:
  """Quote class to define quotes object"""

  def __init__(self,author,id,quote,permalink):
    self.author = author
    self.id = id
    self.quote = quote
    self.permalink = permalink


class User(UserMixin,db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255), unique=True, index = True)
  pass_secure = db.Column(db.String(255))
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self,password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.pass_secure, password)

  def __repr__(self):
    return f'User {self.username}'

  @login_manager.user_loader
  def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
  __tablename__ = 'roles'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255))
  users = db.relationship('User',backref='role',lazy='dynamic')

  def __repr__(self):
    return f'user{self.name}'

class Blog:
  all_Blogs = []

  def __init__(self,blog_id,title,blog):
    self.blog_id = blog_id
    self.title = title
    self.blog = blog

  def save_blog(self):
    Blog.all_Blogs.append(self)

  @classmethod
  def clear_blogs(cls):
    Blog.all_Blogs.clear()

  @classmethod
  def get_blogs(cls,id):
    response = []
     
    for blog in cls.all_Blogs:
      if blog.id == id:
        response.append(blog)

      return response