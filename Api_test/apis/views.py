from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
import base64
import xml.etree.ElementTree as ET

# Create your views here.


def apis(request):
    date = {
    'name':'william',
    }
    if request.method == 'POST':
        print(request.POST['key'])
    else:
        print(request.GET['key'])

    return JsonResponse(date)

def SHA1(sortString):
    s1 = hashlib.sha1(bytes(sortString,encoding='utf-8')).hexdigest()
    #s2 = hashlib.sha1(s1).digest()
    #s3 = base64.b64encode(s2).decode('utf-8')

    return s1

def sort(token,timestamp,nonce):
    lists = [token,timestamp,nonce]
    print('[*]the list is',lists)
    lists.sort()

    sbuilder = ''
    for i in lists:
        sbuilder += i

    print('[*]sortString is',sbuilder)
    return sbuilder

@csrf_exempt
def WxServlet(request):
    token = 'hnust'

    if request.method == "GET":
        print("[*]开始签名校检")
        signature  = request.GET['signature']
        timestamp  = request.GET['timestamp']
        nonce      = request.GET['nonce']
        echostr    = request.GET['echostr']

        #排序
        sortString = sort(token,timestamp,nonce)

        #加密
        mytoken    = SHA1(sortString)

        #校验签名
        if mytoken != None and mytoken != '' and mytoken == signature:
            print("校验签名通过")
            return  HttpResponse(echostr)
        else:
            print('校验签名失败')
    else:
        othercontent = autoreply(request)
        return HttpResponse(othercontent)
    return HttpResponse("[*]Failed")

def autoreply(request):
    try:
        print('into post')
        webData = request.body
        print("[*]webDate is",webData)
        xmlData = ET.fromstring(webData)

        msg_type = xmlData.find('MsgType').text
        ToUserName = xmlData.find('ToUserName').text
        FromUserName = xmlData.find('FromUserName').text
        CreateTime   = xmlData.find('CreateTime').text
        MsgID = xmlData.find('MsgId').text

        toUser = FromUserName
        fromUser = ToUserName

        if msg_type == "text":
            content = 'hello, welcome to python stage.'
            replyMsg= TextMsg(toUser,fromUser,content)
            print('[*]Successful!!!')
            print(replyMsg)
            return replyMsg.send()
        elif msg_type == "image":
            content = 'recieved image,thanks'
            replyMsg= TextMsg(toUser,fromUser,content)
            return replyMsg.send()
        elif msg_type == 'voice':
            content = 'recieved voice message,thanks'
            replyMsg= TextMsg(toUser,fromUser,content)
            return replyMsg.send()
        elif msg_type == 'shortvideo':
            content = 'recieved shortvideo,thanks'
            replyMsg = TextMsg(toUser,fromUser,content)
            return replyMsg.send()

    except Exception as e:
        return e
class Msg(object):
    def __init__(self,xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime   = xmlData.find('CreateTime').text
        self.MsgType      = xmlData.find('MsgType').text
        self.MsgId        = xmlData.find('MsgId').text


import time
class TextMsg(Msg):
    def __init__(self,toUserName,fromUserName,content):
        self.__dict__ = dict()
        self.__dict__['ToUserName'] = toUserName
        self.__dict__['FromUserName'] = fromUserName
        self.__dict__['CreateTime']   = int(time.time())
        self.__dict__['Content']      = content

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        
        """
        return XmlForm.format(**self.__dict__)