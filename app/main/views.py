from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_quotes
from ..models import Blog,User
from .forms import BlogForm,UpdateProfile
from flask_login import login_required,current_user
from .. import db,photos

#views
@main.route('/')
def index():
  """view root page function that returns index page and its data"""
  quotes=get_quotes()

  return render_template('index.html', quotes= quotes)

@main.route('/blog/<int:blog_id>')
def blog(blog_id):
  """view blog function that return the blog details page and its data"""
  return render_template('blog.html')

@main.route('/blog/new/<int:id>', methods=['POST','GET'])
@login_required
def new_blog(id): 
  form = BlogForm()
  user = User.query.filter_by(id=id).first()

  if form.validate_on_submit():
    title = form.title.data
    blog = form.blog.data
    
    # blog instance       
    new_blog = Blog(title=title,blog=blog,user=current_user)

    new_blog.save_blog()
    # return redirect(request.url)
    return redirect(url_for('.view_blogs', uname=user.username))

  return render_template('new_blog.html', blog_form = form)

@main.route('/blog/all/<uname>')  
def view_blogs(uname):
  user = User.query.filter_by(username=uname).first()
  blogs = Blog.get_blogs(user.id)

  if user is None:
    abort(404)

  return render_template('all_blogs.html', uname=user.username,user=user, blogs=blogs)

@main.route('/user/<uname>')  
def profile(uname):
  user = User.query.filter_by(username=uname).first()
  blogs = Blog.get_blogs(user.id)

  if user is None:
    abort(404)

  return render_template('profile/profile.html', uname=user.username,user=user, blogs=blogs)

@main.route('/user/<uname>/update', methods=['GET','POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username=uname).first()

  if user is None:
    abort(404)

  form = UpdateProfile()
  if form.validate_on_submit():
    user.bio = form.bio.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile', uname=user.username))

  return render_template('profile/update.html', form=form)

@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username=uname).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic_path = path
    db.session.commit()

  return redirect(url_for('main.profile', uname=uname))
