from flask import Blueprint, request

bp = Blueprint('crm', __name__, subdomain='crm')


@bp.route('/')
def index():
    username = request.cookies.get('username')
    return username or '没有获取到cookie!'