# chain\demo5\blue_prints\crm.py
from flask import Blueprint, render_template

crm_bp = Blueprint('crm', __name__, subdomain="crm")


# 这个/是必须的，不能有其它的字符了
@crm_bp.route("/")
def crm():
    return render_template('index.html')