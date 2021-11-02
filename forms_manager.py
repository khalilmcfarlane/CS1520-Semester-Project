from wtforms import Form, StringField, validators, TextAreaField, TextField, BooleanField
from wtforms.validators import Required


class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
class NewPostForm(Form):
    title=StringField('Title', [validators.DataRequired()])
    article=TextAreaField('Article', [validators.DataRequired()])