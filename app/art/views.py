from flask import render_template, redirect
from . import art


# 发布文章
@art.route("/add/", methods=["GET", "POST"])
def art_add():
    return render_template("art/art_add.html")


# 编辑文章
@art.route("/edit/<int:id>", methods=["GET", "POST"])
def art_add(id):
    return render_template("art/art_edit.html")


# 删除文章
@art.route("/del/<int:id>", methods=["GET", "POST"])
def art_add(id):
    return redirect("art/list")


# 文章列表
@art.route("/list/", methods=["GET"])
def art_add():
    return render_template("art/art_list.html")
