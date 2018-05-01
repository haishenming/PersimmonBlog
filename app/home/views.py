from flask import render_template, redirect, url_for

from .forms import LoginForm, RegisterForm
from . import home

from .. import app
app.config["SECRET_KEY"] = "hjdahnjehhjkkjajehjakihufeiasdkj"

@home.route("/")
def index():
    return "<h1>Hello home<h1>"


# 登陆
@home.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()

    return render_template("home/login.html", title="登陆", form=form)


# 注册
@home.route("/register/", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    return render_template("home/register.html", title="注册", form=form)


# 退出
@home.route("/logout/", methods=["GET"])
def logout():
    # return redirect(url_for("home.login"))
    return redirect(url_for("home.login"))
