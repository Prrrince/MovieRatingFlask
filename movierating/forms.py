import wtforms as forms
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import validators as valid

from movierating.models import User


class UserCreationForm(FlaskForm):
    username = forms.StringField('Username',
                                 validators=[valid.DataRequired(),
                                             valid.Length(min=2, max=20)])
    email = forms.StringField('Email',
                              validators=[valid.DataRequired(), valid.Email()])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise valid.ValidationError("This username is already taken")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise valid.ValidationError("An account already exists for this \
                                        email")


class RegistrationForm(UserCreationForm):
    password = forms.PasswordField('Password',
                                   validators=[valid.DataRequired()])
    confirm_password = forms.PasswordField('Confirm Password',
                                           validators=[
                                            valid.DataRequired(),
                                            valid.EqualTo('password')
                                            ])


class UserUpdateForm(UserCreationForm):
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise valid.ValidationError("This username is already taken")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise valid.ValidationError("An account already exists for thi\
                                            s email")


class LoginForm(FlaskForm):
    email = forms.StringField('Email',
                              validators=[valid.DataRequired(), valid.Email()])
    password = forms.PasswordField('Password',
                                   validators=[valid.DataRequired()])
    remember = forms.BooleanField('Remember Me')
