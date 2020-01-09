import time
from flask import Blueprint, request, make_response
from main.views.wchat.ffunc import *
from main.views.wchat.constants import token

wct = Blueprint('chat', __name__, url_prefix='/wchat')


@wct.route('/msg', methods=("GET", "POST"))
def msg():
    print('this is msg')
    return make_response('this is msg')


@wct.route('/', methods=("GET", "POST"))
def hello():
    if request.method == 'POST':
        print(request)
        xml = request.stream.read()  # 接收消息 xml
        rdict = analyze_msg(xml)
        # sava msg
        save_to_file(rdict)
        save_to_sql(rdict)
        return 'pass'
    else:
        return api(token=token)

