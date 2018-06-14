# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^upload.html/$',views.upload),
]

