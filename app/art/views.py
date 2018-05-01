from flask import render_template, redirect
from . import art


# 发布文章
@art.route("/add/", methods=["GET", "POST"])
def add():
    return render_template("art/art_add.html", title="添加文章")


# 编辑文章
@art.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    return render_template("art/art_edit.html", title="编辑文章")


# 删除文章
@art.route("/dele/<int:id>", methods=["GET", "POST"])
def dele(id):
    return redirect("art/list")


# 文章列表
@art.route("/list/", methods=["GET"])
def list():
    return render_template("art/art_list.html", title="文章列表")
