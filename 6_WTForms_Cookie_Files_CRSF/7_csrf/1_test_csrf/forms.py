from wtforms import Form, StringField, FloatField
from wtforms.validators import Email, Length, EqualTo, InputRequired, NumberRange


class RegistForm(Form):
    email = StringField(validators=[Email()])
    username = StringField(validators=[Length(3, 20)])
    password = StringField(validators=[Length(6, 20)])
    password_repeat = StringField(validators=[EqualTo('password')])
    deposit = FloatField(validators=[InputRequired()])


class LoginForm(Form):
    email = StringField(validators=[Email()])
    password = StringField(validators=[Length(6, 20)])


class TransferForm(Form):
    email = StringField(validators=[Email()])
    money = FloatField(validators=[NumberRange(1, 100000)])