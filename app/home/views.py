from . import home


@home.route("/")
def index():
    return "<h1>Hello home<h1>"