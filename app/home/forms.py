from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from ..models import User


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

    def validate_pwd(self, field):
        pwd = field.data
        user = User.query.filter_by(name=self.name.data).first()
        if not user:
            raise ValidationError("用户未注册")
        else:
            if not user.check_pwd(pwd):
                raise ValidationError("密码不正确")


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
    # code = StringField(
    #     label="验证码",
    #     validators=[
    #         DataRequired("验证码不能为空"),
    #
    #     ],
    #     description="验证码",
    #     render_kw={
    #         "class": "form-control",
    #         "placeholder": "请输入验证码",
    #     }
    # )
    submit = SubmitField(
        "注册",
        render_kw={
            "class": "btn btn-primary",
        }
    )

    # 验证用户名
    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user > 0:
            raise ValidationError("用户名已经存在")


class CommentForm(FlaskForm):
    id = IntegerField(
        label="编号",
        description="编号",
        validators=[
            DataRequired("编号不能为空")
        ],
    )

    content = TextAreaField(
        label="评论",
        description="评论",
        validators=[
            DataRequired("内容不能为空")
        ],
        render_kw={
            "class": "form-control",
            "style": "height: 100px;",
        }
    )

    submit = SubmitField(
        "评论",
        render_kw={
            "class": "btn btn-primary",
        }
    )
