from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired


# 添加文章表单
class ArtForm(FlaskForm):
    title = StringField(
        label="标题",
        description="标题",
        validators=[
            DataRequired("标题不能为空")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入标题",
        }
    )

    content = TextAreaField(
        label="内容",
        description="内容",
        validators=[
            DataRequired("内容不能为空")
        ],
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

# 添加文章表单
class ArtEditForm(FlaskForm):
    id = IntegerField(
        label="编号",
        description="编号",
        validators=[
            DataRequired("编号不能为空")
        ],
        render_kw={
            "class": "form-control",
        }

    )
    title = StringField(
        label="标题",
        description="标题",
        validators=[
            DataRequired("标题不能为空")
        ],
        render_kw={
            "class": "form-control",
        }
    )

    content = TextAreaField(
        label="内容",
        description="内容",
        validators=[
            DataRequired("内容不能为空")
        ],
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
