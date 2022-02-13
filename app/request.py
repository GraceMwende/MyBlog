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

  if get_quotes_response:
    author = get_quotes_response.get('author')
    id = get_quotes_response.get('id')
    quote = get_quotes_response.get('quote')
    permalink = get_quotes_response.get('permalink')

    quotes_results = Quote(author,id,quote,permalink)
    

  return quotes_results