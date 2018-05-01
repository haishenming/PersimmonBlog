from datetime import datetime
from flask import render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash

from ..models import User, db
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

    if form.validate_on_submit():
        data = form.data
        user = User(
            name=data["name"],
            pwd=generate_password_hash(data["pwd"]),
            addtime=datetime.now()
        )
        db.session.add(user)
        db.session.commit()
        # 闪现
        flash("注册成功", "ok")
        return redirect("/login/")
    else:
        flash("请输入注册信息", "err")
    return render_template("home/register.html", title="注册", form=form)


# 退出
@home.route("/logout/", methods=["GET"])
def logout():
    # return redirect(url_for("home.login"))
    return redirect(url_for("home.login"))
