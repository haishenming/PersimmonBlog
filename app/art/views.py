import os
from datetime import datetime
import uuid
from werkzeug.utils import secure_filename

from flask import render_template, redirect, session, url_for

from .forms import ArtForm, ArtEditForm
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
    # 获取用户id
    user = User.query.filter_by(name=session['user']).first()
    user_id = user.id
    if form.validate_on_submit():
        data = form.data
        # 保存数据
        art = Article(
            title=data["title"],
            user_id=user_id,
            content=data["content"]
        )
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("art.list", page=1))

    return render_template("art/art_add.html", title="添加文章", form=form, user=user)


# 编辑文章
@art.route("/edit/<int:id>", methods=["GET", "POST"])
@user_login_req
def edit(id):
    form = ArtEditForm()
    # 获取用户id
    user = User.query.filter_by(name=session['user']).first()
    art = Article.query.get_or_404(int(id))
    if form.validate_on_submit():
        data = form.data
        art.title = data["title"]
        art.content = data["content"]
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("art.list", page=1))
    form.id.data = art.id
    form.title.data = art.title
    form.content.data = art.content
    return render_template("art/art_edit.html", title="编辑文章", form=form, art=art, user=user)


# 删除文章
@art.route("/dele/<int:id>", methods=["GET", "POST"])
@user_login_req
def dele(id):
    art = Article.query.get_or_404(int(id))
    db.session.delete(art)
    db.session.commit()

    return redirect(url_for("art.list", page=1))


# 文章列表
@art.route("/list/<int:page>", methods=["GET"])
@user_login_req
def list(page=1):
    user = User.query.filter_by(name=session["user"]).first()
    page_data = Article.query.filter_by(user_id=user.id).order_by(Article.addtime.desc()).paginate(page=page,
                                                                                                   per_page=10)

    return render_template("art/art_list.html", title="文章列表", page_data=page_data, user=user)
