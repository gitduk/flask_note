# 设计理念：功能/APP
一个功能下有多个应用（联想LINUX设计理念）

is:

views
  + APP1
  + APP2
 
not:

APP1
  + views
 
APP2
  + views

# 临时素材库获取api
img = requests.get('https://api.weixin.qq.com/cgi-bin/media/get?access_token=' + asc_token + '&MediaID=' + mdid)
# 保存文件很棒的代码
file_path = '{0}/{1}.{2}'.format(os.getcwd(), tp, type)
if not os.path.exists(file_path):
    with open(file_path, 'wb') as f:
        f.write(data.content)
