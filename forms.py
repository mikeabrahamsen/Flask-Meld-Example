from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField(('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(('Password'), validators=[DataRequired()])
    password_confirm = PasswordField(
        ('Confirm Password'), validators=[DataRequired(),
                                          EqualTo('password')])
    submit = SubmitField(('Submit'))
