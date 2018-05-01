from . import admin


@admin.route("/")
def index():
    return "<h1>Hello admin<h1>"


@admin.route("/login")
def login():
    return "<h1>Hello admin login<h1>"