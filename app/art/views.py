import os
from datetime import datetime
import uuid
from werkzeug.utils import secure_filename

from flask import render_template, redirect, session

from .forms import ArtForm
from . import art
from ..models import User, Article, db
from pkg.funcs import user_login_req


def change_name(name):
    info = os.path.splitext(name)
    name = datetime.now().strftime("%Y%m%d%X") + str(uuid.uuid4().hex) + info[-1]
    return name


# 发布文章
@art.route("/add/", methods=["GET", "POST"])
@user_login_req
def add():
    form = ArtForm()
    if form.validate_on_submit():
        data = form.data
        # 获取用户id
        user = User.query.filter_by(name=session['user']).first()
        user_id = user.id
        # 保存数据
        art = Article(
            title=data["title"],
            user_id=user_id,
            content=data["content"]
        )
        db.session.add(art)
        db.session.commit()

    return render_template("art/art_add.html", title="添加文章", form=form)


# 编辑文章
@art.route("/edit/<int:id>", methods=["GET", "POST"])
@user_login_req
def edit(id):
    return render_template("art/art_edit.html", title="编辑文章")


# 删除文章
@art.route("/dele/<int:id>", methods=["GET", "POST"])
@user_login_req
def dele(id):
    return redirect("art/list")


# 文章列表
@art.route("/list/<int:page>", methods=["GET"])
@user_login_req
def list(page):
    if page is None:
        page = 1
    user = User.query.filter_by(name=session["user"]).first()
    page_data = Article.query.filter_by(user_id=user.id).order_by(Article.addtime.desc()).paginate(page=page, per_page=10)

    return render_template("art/art_list.html", title="文章列表", page_data=page_data)
