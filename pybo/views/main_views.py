from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main',__name__, url_prefix='/')

@bp.route('/hellos')
def hello_pybo():
    return 'Hello, PYbo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list')) # question._list => question은 등록된 블루프린트 이름, _list는 블루프린트에 등록된 함수명이라고 생각하면 된다.