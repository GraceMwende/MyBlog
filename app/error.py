from flask import render_template
from app import app

@app.errorhandler(404)
def errors(error):
  """Functon to render the 404 error page"""
  return render_template('errors.html'),404