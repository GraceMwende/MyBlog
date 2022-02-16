from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired


class BlogForm(FlaskForm):
  title = StringField('Blog Title', validators=[InputRequired()])
  blog = TextAreaField('Blog', validators=[InputRequired()])
  submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about you', validators=[InputRequired()])
  submit = SubmitField('Submit')

class CommentForm(FlaskForm):
  comment = TextAreaField('Post a Comment')
  submit = SubmitField('Submit')