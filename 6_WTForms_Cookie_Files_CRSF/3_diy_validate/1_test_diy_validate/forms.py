from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, EqualTo, Email, InputRequired, NumberRange, Regexp, URL, UUID, ValidationError


class LoginForm(Form):
    # email = StringField(validators=[Email()])
    # username = StringField(validators=[InputRequired()])
    # age = IntegerField(validators=[NumberRange(12, 100)])
    # phone = StringField(validators=[Regexp(r'1[357]\d{9}')])
    # homepage = StringField(validators=[URL()])
    # uuid = StringField(validators=[UUID()])
    captcha = StringField(validators=[Length(4, 4)])

    def validate_captcha(self, field):
        if field.data != '1234':
            raise ValidationError("验证码错误！")


class SettingsForm(Form):
    username = StringField("用户名", validators=[InputRequired()])
    age = IntegerField('年龄', validators=[Length(10, 100)])