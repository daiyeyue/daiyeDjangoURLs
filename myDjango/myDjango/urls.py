"""myDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as tv
from teacher import teacher_url

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # 视图函数名称只有名称，无括号和参数
    # http://127.0.0.1:8000/normalmap/
    url(r'^normalmap/', tv.do_normalmap),
    # 第一个参数是year，第二个参数是month,http://127.0.0.1:8000/withparam/2011/09
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',tv.withparam),

# 比如约定，凡是以teacher模块处理的视图url都以teacher开头
    url(r'^teacher/', include(teacher_url)),

# book例子
    url(r'^book/(?:page-(?P<page_number>\d+)/)$', tv.do_param2),

#参数不仅仅来自以URL,还可能是我们自己定义的内容,参数是字典形式出现
    url(r'^yourname/$', tv.extremParam, {'name':"liuying"}),

#反向解析
    url(r'mayiknowyourname/$', tv.revParse, name="askname"),

]
