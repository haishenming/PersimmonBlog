from functools import wraps
from flask import redirect, url_for, session, request




# 登陆装饰器
def user_login_req(f):
    @wraps(f)
    def login_req(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for('home.login', next=request.url))
        return f(*args, **kwargs)
    return login_req