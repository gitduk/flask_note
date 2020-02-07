import os
import requests
from flask import request, make_response
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.utils import check_signature
import xml.etree.ElementTree as ET
from main.views.wchat.constants import asc_token, msg_map
from main.views.tfunc import to_localtime
from main.models.wchat.msg_model import *


def api(token):
    data = request.args
    print(data)
    if data:
        signature = data.get('signature')
        timestamp = data.get('timestamp')
        nonce = data.get('nonce')
        echostr = data.get('echostr')
        with open('signature', 'a') as f:
            f.write('signature: ' + signature + '\n')
            f.write('timestamp: ' + timestamp + '\n')
            f.write('nonce: ' + nonce + '\n')
            f.write('echostr: ' + echostr + '\n')
        try:
            check_signature(token, signature, timestamp, nonce)
        except InvalidSignatureException:
            pass
        return make_response(echostr)
    else:
        return


def analyze_msg(msg):
    '''return a dict'''
    rt = ET.fromstring(msg)
    type = rt.findtext('.//MsgType')
    result = {}
    for r in msg_map[type]:
        result[r] = rt.findtext('.//%s' % r)
    return result


def save_to_file(r_dict):
    tp = r_dict['MsgType']
    if tp in ['image', 'voice', 'voice', 'video', 'shortvideo']:
        mdid = r_dict['MediaId']
        data = requests.get(
            'https://api.weixin.qq.com/cgi-bin/media/get?access_token=' + asc_token + '&MediaID=' + mdid)
        file_path = ('{}/{}/{}/{}'.format('main', 'files', 'wchat', 'message.txt'))
        if not os.path.exists(file_path):
            with open(file_path, 'wb') as f:
                f.write(data.content)
        print('save file in {path}'.format(path=file_path))
    elif tp == 'text':
        file_path = '{0}/main/files/wchat/{1}.{2}'.format(os.getcwd(), 'message', 'txt')
        data = r_dict['Content']
        timestamp = r_dict['CreateTime']
        local_time = to_localtime(timestamp)
        fmt = '{}: {} \n'
        with open(file_path, 'a') as f:
            f.write(fmt.format(str(local_time), data))
        print('save message in {path}'.format(path=file_path))


def save_to_sql(r_dict):
    tp = r_dict['MsgType']
    attr_list = msg_map[tp]

    if tp == 'text':
        data = Text(ToUserName=r_dict[attr_list[0]], FromUserName=r_dict[attr_list[1]], CreateTime=r_dict[attr_list[2]], MsgType=r_dict[attr_list[3]],
                    Content=r_dict[attr_list[4]], MsgId=r_dict[attr_list[5]])
        db.session.add(data)
        db.session.commit()
        print('Saved')
    return 'pass'

