from django.urls import path
from . import views

app_name = 'dati'

urlpatterns = [
    path('',views.index,name='index'),
    path('get_score/',views.Get_score,name='get_score'),
]
