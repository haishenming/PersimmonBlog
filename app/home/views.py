from datetime import datetime
from werkzeug.security import generate_password_hash
from functools import wraps

from flask import render_template, redirect, url_for, flash, session, request

from pkg.funcs import user_login_req
from ..models import User, db
from .forms import LoginForm, RegisterForm
from . import home
from .. import app

app.config["SECRET_KEY"] = "hjdahnjehhjkkjajehjakihufeiasdkj"

# 登陆
@home.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        session["user"] = data["name"]
        return redirect("/art/list/1")
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
@user_login_req
def logout():
    # return redirect(url_for("home.login"))
    session.pop("user", None)
    s = session.get("user")
    return redirect(url_for("home.login"))
