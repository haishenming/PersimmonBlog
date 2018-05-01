from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField, TextAreaField, SubmitField


# 添加文章表单
class ArtForm(FlaskForm):
    title = StringField(
        label="标题",
        description="标题",
        validators=[],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入标题",
        }
    )

    cate = SelectField(
        label="分类",
        description="分类",
        validators=[],
        coerce=int,
        render_kw={
            "class": "form-control",
        }
    )

    logo = FileField(
        label="封面",
        description="封面",
        validators=[],
        render_kw={
            "class": "form-control-file",
        }
    )

    content = TextAreaField(
        label="内容",
        description="内容",
        validators=[],
        render_kw={
            "style": "height: 300px;",
            "id": "content",
        }
    )

    submit = SubmitField(
        "发布",
        render_kw={
            "class": "btn btn-primary",
        }
    )
