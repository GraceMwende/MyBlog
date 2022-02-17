import unittest
from app.models import Comments,User
from app import db

class CommentTest(unittest.TestCase):
  """tets behaviour for comment class"""
  def setUp(self):
    self.user_grace = User(username='Grace',password='potato',email='gracemwende@ms.com')
    self.new_comment = Comments(blog_id=123,comment="This is good",user=self.user_grace)

  def tearDown(self):
    Comments.query.delete()
    User.query.delete()

  def test_save_comment(self):
    self.new_comment.save_comment()
    self.assertTrue(len(Comments.query.all())>0)

  def test_get_comment_by_id(self):

    self.new_comment.save_comment()
    got_comment = Comment.get_comment(12345)
    self.assertTrue(len(got_comment) == 1)