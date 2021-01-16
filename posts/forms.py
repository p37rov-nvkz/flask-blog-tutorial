#wtforms
from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired



class PostForm(FlaskForm):
    title = StringField('Заголовок:', validators=[DataRequired()])
    body = TextAreaField('Пост:', validators=[DataRequired()])