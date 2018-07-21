from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
import base64
import xml.etree.ElementTree as ET
import time

# Create your views here.

@csrf_exempt
def WxServlet(request):
    token = 'william'

    if request.method == "GET":
        print('[*]开始校验签名')
        signature = request.GET['signature']
        timestamp = request.GET['timestamp']
        nonce     = request.GET['nonce']
        echostr   = request.GET['echostr']

        #排序
        lists = [token,timestamp,nonce]
        lists.sort()
        sortString = ''
        for i in lists:
            sortString += i

        #加密
        mytoken = hashlib.sha1(bytes(sortString,encoding='utf-8')).hexdigest()

        if mytoken != None and mytoken != '' and mytoken == signature:
            print('签名校验通过')
            return HttpResponse(echostr)
        else:
            print('签名校验失败')
    else:
        othercontent = autoreply(request)
        return HttpResponse(othercontent)
    return HttpResponse('[*]Failed')


def autoreply(request):
    try:
        webData = request.body
        print(webData)
        xmlData = ET.fromstring(webData)

        msg_type    = xmlData.find('MsgType').text
        ToUserName  = xmlData.find('ToUserName').text
        FromUserName= xmlData.find('FromUserName').text
        CreateTime  = xmlData.find('CreateTime').text
        MsgId       = xmlData.find('MsgId').text

        toUser   = FromUserName
        fromUser = ToUserName

        if msg_type == 'text':
            content = 'hello, welcome to python stage'
            replyMsg= TextMsg(toUser,fromUser,content)
            return replyMsg.send()
            print('[*]Successful')
        elif msg_type == 'voice':
            content = '[!!]Can not deal with voice message. Please send message with text.'
            replyMsg= TextMsg(toUser,fromUser,content)
            return replyMsg.send()
        elif msg_type == 'image':
            imgUrl  = xmlData.find('PicUrl').text
            content = 'recieved image,thanks!'
            replyMsg= TextMsg(toUser,fromUser,content)
            return replyMsg.send()
    except Exception as e:
        return e

class TextMsg:
    def __init__(self,toUser,fromUser,content):
        self.toUser   = toUser
        self.fromUser = fromUser
        self.content  = content
        self.time     = int(time.time())

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime><![CDATA[{CreateTime}]]></CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(ToUserName=self.toUser,FromUserName=self.fromUser,CreateTime=self.time,Content=self.content)
