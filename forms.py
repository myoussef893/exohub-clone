from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,FloatField,EmailField,PasswordField,SubmitField,SelectField
from wtforms.validators import DataRequired


categories_list = ['Clothes','Sunglasses','Wallets','Toys','Shoes','Bags','Other']


class Signup(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    email = EmailField('Email Address',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Signup')

class Login(FlaskForm): 
    email = EmailField('Email Address',validators=[DataRequired()])
    password = PasswordField('Password', validators= [DataRequired()])
    login_button = SubmitField('Login')

class PackageScanner(FlaskForm): 
    tracking_number = StringField('Tracking Number',validators=[DataRequired()])
    items_count = IntegerField('Items Count in Package',validators=[DataRequired()])
    locker_number = StringField('Locker id')
    save_button = SubmitField('Submit')

class ItemScanner(FlaskForm): 
    tracking_number = StringField('Tracking Number',validators=[DataRequired()])
    item_weigt = FloatField('Item Weight',validators=[DataRequired()])
    category = SelectField('Category',validators=[DataRequired()],choices=categories_list)
    submit = SubmitField('Add Item')

    