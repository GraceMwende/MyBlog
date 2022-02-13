class Quote:
  """Quote class to define quotes object"""

  def __init__(self,author,id,quote,permalink):
    self.author = author
    self.id = id
    self.quote = quote
    self.permalink = permalink


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