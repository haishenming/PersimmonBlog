from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError


# 登陆表单
class LoginForm(FlaskForm):
    name = StringField(
        label="帐号",
        validators=[
            DataRequired("帐号不能为空"),
        ],
        description="帐号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入帐号",
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("密码不能为空"),

        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码",
        }
    )
    submit = SubmitField(
        "登陆",
        render_kw={
            "class": "btn btn-primary",
        }
    )


# 注册表单
class RegisterForm(FlaskForm):
    name = StringField(
        label="帐号",
        validators=[
            DataRequired("帐号不能为空"),

        ],
        description="帐号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入帐号",
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("密码不能为空"),

        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码",
        }
    )
    repwd = PasswordField(
        label="确认密码",
        validators=[
            DataRequired("确认密码不能为空"),
            EqualTo('pwd', "两次输入密码不一致")
        ],
        description="确认密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请再次输入密码",
        }
    )
    code = StringField(
        label="验证码",
        validators=[
            DataRequired("验证码不能为空"),

        ],
        description="验证码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入验证码",
        }
    )
    submit = SubmitField(
        "注册",
        render_kw={
            "class": "btn btn-primary",
        }
    )
