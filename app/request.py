from app import app
import urllib.request, json
from .models import quote

Quote = quote.Quote

# Getting the Quotes base url
base_url = app.config['QUOTES_API_BASE_URL']

def get_quotes():
  """Function that gets the json response to our url request"""

  with urllib.request.urlopen(base_url) as url:
    get_quotes_data = url.read()
    get_quotes_response = json.loads(get_quotes_data)

    quotes_results = None

    quotes_result_list = get_quotes_response
    quotes_results = process_results(quotes_result_list)

  return quotes_results

def process_results(quote_list):
  """Function that processes the quote result and transform them to a list of objects
  Args:
      quote_list :A list of dictionaries that contains quote details
  Returns:
      quotes_results:A list of quotes object
  """

  quotes_results = []
  for quote_item in quote_list:
    author = quote_item.get('author')
    id = quote_item.get('id')
    quote = quote_item.get('quote')
    permalink = quote_item.get('permalink')

    if quote:
      quote_object = Quote(author,id,quote,permalink)
      quotes_results.append(quote_object)

  return quotes_results