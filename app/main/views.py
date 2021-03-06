from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_quotes
from ..models import Blog,User,Comments
from .forms import BlogForm,UpdateProfile,CommentForm
from flask_login import login_required,current_user
from .. import db,photos
import markdown2

#views
@main.route('/')
def index():
  """view root page function that returns index page and its data"""
  quotes=get_quotes()
  allBlogs = Blog.query.all()
  return render_template('index.html', quotes= quotes, blogs=allBlogs)

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

@main.route('/blog/comment/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
  form = CommentForm()
  blogs = Blog.query.filter_by(id=id).first()
  #blog = get_blogs(id)
  comments_blog= Comments.query.filter_by(blog=blogs).all()
  
  if form.validate_on_submit():
    comment = form.comment.data

    #comment instance  
    new_comment = Comments(blog_id = blogs.id,comment=comment, user= current_user)
    #save_comment
    new_comment.save_comment()
    return redirect(request.url)
  
  return render_template('new_comment.html', comment_form= form,blog=blogs,comments_blog=comments_blog)

@main.route('/comment/<int:id>')
def single_comment(id):
    comment = Comments.query.get(id)
    if comment is None:
        abort(404)
    format_comment = markdown2.markdown(comment.comment,extras=["code-friendly","fenced-code-blocks"])
    return render_template('comment.html',comment=comment,format_comment=format_comment)

@main.route('/blog/<int:id>')
def single_blog(id):
    blog=Blog.query.get(id)
    if blog is None:
        abort(404)
    format_blog = markdown2.markdown(blog.blog,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('blogging.html',blog = blog,format_blog=format_blog)


