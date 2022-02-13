from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired


class BlogForm(FlaskForm):
  title = StringField('Blog Title', validators=[InputRequired()])
  blog = TextAreaField('Blog', validators=[InputRequired()])
  submit = SubmitField('Submit')