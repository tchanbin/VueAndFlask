from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth
from ..models import User
from . import api
from .errors import unauthorized, forbidden
from flask_login import  current_user

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username_or_token, password):
    if username_or_token == '':
        return False
    if password == '':
        g.current_user = User.verify_auth_token(username_or_token)
        # 下面为true，我们可以记录是使用令牌登录
        g.token_used = True
        return g.current_user is not None
    #
    user = User.query.filter_by(username=username_or_token).first()
    if not user:
        return False
    g.current_user = user
    g.token_used = False
    return user.verify_password(password)



# @auth.verify_password
# def verify_password(email_or_token, password):
#     if email_or_token == '':
#         return False
#     if password == '':
#         g.current_user = User.verify_auth_token(email_or_token)
#         g.token_used = True
#         return g.current_user is not None
#     user = User.query.filter_by(email=email_or_token.lower()).first()
#     if not user:
#         return False
#     g.current_user = user
#     g.token_used = False
#     return user.verify_password(password)


@auth.error_handler
def auth_error():
    return unauthorized('非法用户')


# 在所有请求前都加上登录认证
@api.before_request
@auth.login_required
def before_request():
   pass


# # 在所有请求前都加上登录认证
# @api.before_request
# @auth.login_required
# def before_request():
#     if g.current_user.is_anonymous:
#         return forbidden('匿名用户禁止登录')

# # 在所有请求前都加上登录认证
# @api.before_request
# @auth.login_required
# def before_request():
#     if not g.current_user.is_anonymous and \
#             not g.current_user.confirmed:
#         return forbidden('没有确认的账户')


@api.route('/tokens/', methods=['POST'])
def get_token():
    if g.current_user.is_anonymous or g.token_used:
        return unauthorized('未授权')
    return jsonify({'token': g.current_user.generate_auth_token(
        expiration=3600), 'expiration': 3600})
