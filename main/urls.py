from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('kak_je_xochetsa_kanikuli', views.about, name='quest1'), #поменять views.index на следующую и name также
    re_path('0Y/RgtC10LHRj9C70Y7QsdC70Y4=', views.quest2, name='quest2'),
    re_path('lalop', views.quest3, name='quest3')
]