import unittest
from app.models import Quote

class Quotestest(unittest.TestCase):
  """Test class to test beaviour of quotes class"""

  def setUp(self):
    """setup method that runs before every test"""
    self.new_quote = Quote('Rick Osborne',9,'Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.','http://quotes.stormconsultancy.co.uk/quotes/9')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_quote,Quote))