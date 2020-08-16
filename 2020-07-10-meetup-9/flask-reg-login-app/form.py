from flask_wtf import Form
from wtforms import validators, StringField, PasswordField


class RegistrationForm(Form):
    name = StringField('Name', [validators.DataRequired(), validators.Length(max=100)])
    email = StringField('Email', [validators.DataRequired(), validators.Email(), validators.Length(min=8, max=200)])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Password does not match')])
    confirm = PasswordField('Confirm Password', [validators.DataRequired()])


class LoginForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Email(), validators.Length(min=8, max=200)])
    password = PasswordField('Password', [validators.DataRequired()])
