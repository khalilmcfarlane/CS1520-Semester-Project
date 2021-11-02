from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators, TextAreaField

class NewPostForm(Form):
    title=StringField('Title', [validators.DataRequired()])
    article=TextAreaField('Article', [validators.DataRequired()])