# msg.hello
token = 'qwertyuiopqwertyuiop'


# ffunc.analyze_msg
msg_map = {
    'text': ['ToUserName', 'FromUserName', 'CreateTime', 'MsgType', 'Content', 'MsgId'],
    'image': ['ToUserName', 'FromUserName', 'CreateTime', 'MsgType', 'PicUrl', 'MediaId', 'MsgId'],
    'voice': ['ToUserName', 'FromUserName', 'CreateTime', 'MsgType', 'MediaId', 'Format', 'MsgId'],
    'video': ['ToUserName', 'FromUserName', 'CreateTime', 'MsgType', 'MediaId', 'ThumbMediaId', 'MsgId'],
    'shortvideo': ['ToUserName', 'FromUserName', 'CreateTime', 'MsgType', 'MediaId', 'ThumbMediaId', 'MsgId'],
    'location': ['ToUserName', 'FromUserName', 'CreateTime', 'MsgType', 'Location_X', 'Location_Y', 'Scale', 'Label', 'MsgId'],
    'link': ['ToUserName', 'FromUserName', 'CreateTime', 'MsgType', 'Title', 'Description', 'Url', 'MsgId'],
}

# ffunc.save_file
asc_token = '28_-w0YPCX-u-CgW2p6HmiQWgOtVL1JxrFNY3E-8E90QsfldW2QwLRf_tUSVoWHmwo7ySMKjFdg64OzAwyPRpklUbcoUNe87teNJ7ci703GwkDH68CZqr-pVYqfwCBm-JJdg4sjOAh8x0DPG8YrEMHaADAOWR'
post_fix = {
    'text': 'txt',
    'image': 'jpg',
    'video': 'mp4',
    'shortvideo': 'mp4'
}
