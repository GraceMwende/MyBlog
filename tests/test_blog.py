import unittest
from app.models import Blog

class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Blog class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_blog = Blog(1234,'Python Must Be Crazy','A  Python Series')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))

    def test_init(self):
        """check if the object is instantiated,correctly"""
        self.assertEqual(self.new_blog.id, 5)
        self.assertEqual(self.new_blog.category, "promotion")
        self.assertEqual(self.new_blog.title, "Banking success")
        self.assertEqual(self.new_blog.decription, "This is where great minds meet and great things happen")

