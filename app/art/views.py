from flask import render_template, redirect

from .forms import ArtForm
from . import art
from pkg.funcs import user_login_req


# 发布文章
@art.route("/add/", methods=["GET", "POST"])
@user_login_req
def add():
    form = ArtForm()

    form.cate.choices = [
        (1, "分类1"),
        (2, "分类2"),
        (3, "分类3"),
    ]
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
@art.route("/list/", methods=["GET"])
@user_login_req
def list():
    return render_template("art/art_list.html", title="文章列表")
