from . import admin


@admin.route("/")
def index():
    return "<h1>Hello admin<h1>"