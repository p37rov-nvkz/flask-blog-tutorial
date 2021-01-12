#wtforms
from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired



class PostForm(Form):
    title = StringField('Заголовок:', validators=[DataRequired()])
    body = TextAreaField('Пост:', validators=[DataRequired()])

