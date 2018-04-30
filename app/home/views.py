
from flask import render_template, redirect, url_for

from . import home


@home.route("/")
def index():
    return "<h1>Hello home<h1>"



# 登陆
@home.route("/login/", methods=["GET", "POST"])
def login():
    return render_template("home/login.html")

# 注册
@home.route("/register/", methods=["GET", "POST"])
def register():
    return render_template("home/register.html")

# 退出
@home.route("/logout/", methods=["GET"])
def logout():
    # return redirect(url_for("home.login"))
    return redirect(url_for("home.login"))