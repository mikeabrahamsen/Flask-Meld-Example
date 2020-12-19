from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    IntegerField,
    FormField,
    FieldList,
    Form,
)
from wtforms.validators import DataRequired, Email, EqualTo, Optional, Length, Regexp


class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8, message="Password be at least 8 characters"),
            Regexp("^(?=.*[a-z])", message="Password must have a lowercase character"),
            Regexp("^(?=.*[A-Z])", message="Password must have an uppercase character"),
            Regexp("^(?=.*\\d)", message="Password must contain a number"),
            Regexp(
                "(?=.*[@$!%*#?&])", message="Password must contain a special character"
            ),
        ],
    )
    password_confirm = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match"),
        ],
    )
    submit = SubmitField("Submit")


class ProductForm(Form):
    title = StringField("Title")
    price = IntegerField("Price", validators=[Optional()])


class InventoryForm(FlaskForm):
    category_name = StringField("Category Name")
    products = FieldList(FormField(ProductForm), min_entries=4, max_entries=8)
