from wtforms import Form, FileField, StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed


class UpLoadForm(Form):
    avatar = FileField(validators=[FileRequired(), FileAllowed(['jpeg', 'gif', 'jpg'])])
    desc = StringField(validators=[InputRequired()])
