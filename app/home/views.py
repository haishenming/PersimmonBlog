from datetime import datetime
from werkzeug.security import generate_password_hash
from functools import wraps

from flask import render_template, redirect, url_for, flash, session, request

from pkg.funcs import user_login_req
from ..models import User, db, Article, Comment
from .forms import LoginForm, RegisterForm, CommentForm
from . import home
from .. import app

app.config["SECRET_KEY"] = "hjdahnjehhjkkjajehjakihufeiasdkj"


# 登陆
@home.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=data["name"]).first()
        session["user"] = data["name"]
        return redirect(url_for("home.index", id=user.id, page=1))
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


# 用户主页
@home.route("/home/<int:id>/<int:page>", methods=["GET"])
def index(id, page):
    user = User.query.get_or_404(int(id))
    page_data = Article.query.filter_by(user_id=user.id).order_by(Article.addtime.desc()).paginate(page=page,
                                                                                                   per_page=10)
    return render_template("home/userHome.html", arts=page_data, user=user, title="{}的主页".format(user.name))


# 文章详情
@home.route("/detail/<int:id>", methods=["GET"])
def detail(id):
    user = User.query.filter_by(name=session['user']).first()
    art = Article.query.get_or_404(int(id))
    art.shownum += 1
    db.session.add(art)
    db.session.commit()
    title = art.title
    form = CommentForm(id=id)

    return render_template("home/detail.html", art=art, user=user, title=title, form=form)

# 文章详情
@home.route("/comment/", methods=["POST"])
def comment():
    user = User.query.filter_by(name=session['user']).first()
    form = CommentForm()
    if form.validate_on_submit():
        comment_model = Comment()
        comment_model.content = form.content.data
        comment_model.user_id = user.id
        comment_model.article = form.id.data
        db.session.add(comment_model)
        db.session.commit()

    return redirect("/detail/{}".format(form.id.data))

