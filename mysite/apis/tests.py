from django.test import TestCase

# Create your tests here.
XmlFrom = """
<xml>
<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
<FromUserName><![CDATA[{FromUserName}]]</FromUserName>
</xml>
"""
print(XmlFrom.format(ToUserName='leon',FromUserName='william'))
