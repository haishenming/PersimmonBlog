from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Haishen123@127.0.0.1:3306/persimmon_blog"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


# 用户
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号
    info = db.Column(db.Text)  # 简介
    face = db.Column(db.String(255))  # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一识别码
    userlogs = db.relationship("Userlog", backref="user")  # 登陆日志
    tags = db.relationship("Tag", backref="user")  # 用户标签
    articles = db.relationship("Article", backref="user")  # 用户文章
    comments = db.relationship("Comment", backref="user")  # 评论
    articlecols = db.relationship("Articlecol", backref="user")  # 收藏文章

    def __repr__(self):
        return "<User {name}>".format(name=self.name)


# 登陆日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    ip = db.Column(db.String(100))  # 登陆ip
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登陆时间

    def __repr__(self):
        return "<Userlog {id}>".format(id=self.id)


# 分类
class Cate(db.Model):
    __tablename__ = "cate"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 标题
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间
    articles = db.relationship("Article", backref="cate")

    def __repr__(self):
        return "<Tag {name}>".format(name=self.name)


# 文章
class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255))  # 文章标题
    info = db.Column(db.Text)  # 文章简介
    content = db.Column(db.Text)  # 文章内容
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    shownum = db.Column(db.Integer)  # 阅读量
    commentnum = db.Column(db.Integer)  # 评论量
    cate = db.Column(db.Integer, db.ForeignKey('cate.id'))  # 分类
    logo = db.Column(db.String(128))  # 封面
    comments = db.relationship("Comment", backref="article_comment")  # 文章评论
    articlecols = db.relationship("Articlecol", backref="article_col")  # 用户文章
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    def __repr__(self):
        return "<Article {title}>".format(title=self.title)


# 评论
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    content = db.Column(db.Text)  # 内容
    article = db.Column(db.Integer, db.ForeignKey('article.id'))  # 所属文章
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    def __repr__(self):
        return "<Comment {id}>".format(id=self.id)


# 文章收藏
class Articlecol(db.Model):
    __tablename__ = "articlecol"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    def __repr__(self):
        return "<Articlecol {id}>".format(id=self.id)


# 权限
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    url = db.Column(db.String(255), unique=True)  # 路由地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    def __repr__(self):
        return "<Auth {name}>".format(name=self.name)


# 用户角色
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    auths = db.String(db.String(1024))  # 角色权限
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    def __repr__(self):
        return "<Role {name}>".format(name=self.name)


# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    is_super = db.Column(db.SmallInteger)  # 是否为超级管理员
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间
    adminlogs = db.relationship("Adminlog", backref="admin")  # 管理员登陆日志
    oplogs = db.relationship("Oplog", backref="admin")  # 管理员操作日志

    def __repr__(self):
        return "<Admin {name}>".format(name=self.name)


# 管理员登陆日志
class Adminlog(db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员
    ip = db.Column(db.String(100))  # 登陆ip
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登陆时间

    def __repr__(self):
        return "<Adminlog {id}>".format(id=self.id)


# 管理员操作日志
class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员
    ip = db.Column(db.String(100))  # 登陆ip
    reson = db.Column(db.String(600))  # 操作原因
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登陆时间

    def __repr__(self):
        return "<Oplog {id}>".format(id=self.id)


if __name__ == '__main__':
    db.create_all()

    # role = Role(
    #     name="超级管理员",
    #     auths=""
    # )

    # from werkzeug.security import generate_password_hash
    #
    # admin = Admin(
    #     name="海神名",
    #     pwd=generate_password_hash("Haishen123"),
    #     is_super=0,
    #     role_id=1
    # )
    #
    # db.session.add(admin)
    # db.session.commit()
