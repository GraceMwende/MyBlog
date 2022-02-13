from flask import render_template
from app import app
from .request import get_quotes

#views
@app.route('/')
def index():
  """view root page function that returns index page and its data"""
  quotes=get_quotes()

  return render_template('index.html', quotes= quotes)

@app.route('/blog/<int:blog_id>')
def blog(blog_id):
  """view blog function that return the blog details page and its data"""
  return render_template('blog.html', id = blog_id)
