from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_quotes
from ..models import Blog
from .forms import BlogForm

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

@main.route('/blog/new', methods=['POST','GET'])
def new_blog():
  form = BlogForm()

  if form.validate_on_submit():
    title = form.title.data
    blog = form.blog.data
    new_blog = Blog(title,blog)
    new_blog.save_blog()
    return redirect(request.url)

  return render_template('new_blog.html', blog_form = form)