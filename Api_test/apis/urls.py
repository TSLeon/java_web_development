from django.urls import path
from . import views

app_name = 'apis'

urlpatterns = [
    path('',views.apis,name='apis'),
    path('wechat/',views.WxServlet,name='wxservlet')
]
