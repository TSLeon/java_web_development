import requests
import json

appid     = ''
appSecret = ''

def getAccessToken():
    try:
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appid,appSecret)
        r = requests.get(url)
        return json.loads(r.text)['access_token']

    except Exception as e:
        print(e)


def add():
    s = getAccessToken()
    jsondata = {
        'button':[
            {
                'name':'历史答题',
                'sub_button':[
                    {
                        'type':'view',
                        'name':'开始答题',
                        'url':'http://5sjvn5.natappfree.cc/dati/'
                    }
                ]
            },
            {
                'name':'帮助',
                'sub_button':[
                    {
                        'type':'view',
                        'name':'答题手册',
                        'url':'https://www.baidu.com/'
                    }
                ]
            }
        ]
    }
    data = json.dumps(jsondata,ensure_ascii=False)
    print(data)
    url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s'%s
    r = requests.post(url=url,data=data.encode('utf-8'))
    print(r.text)

if __name__ == "__main__":
    add()
