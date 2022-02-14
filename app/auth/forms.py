from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Email,EqualTo
from wtforms import ValidationError
from ..models import User

class RegistrationForm(FlaskForm):
  email = StringField('Your Email Address', validators=[InputRequired(),Email()])
  username = StringField('Enter your username', validators=[InputRequired()])
  password = PasswordField('password', validators=[InputRequired(), EqualTo('password_confirm', message='Passwords must match')])
  submit = SubmitField('Sign Up')

  def validate_email(self,data_field):
    if User.query.filter_by(email=data_field.data).first():
      raise ValidationError('There is an account with that email')

  def validate(self)
