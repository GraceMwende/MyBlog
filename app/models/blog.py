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