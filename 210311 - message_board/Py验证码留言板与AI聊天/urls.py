"""Py验证码留言板与AI聊天 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url,include

from .views_map import aichat_view
from .views_map import message_board_view
from .views_map import QB_price_view
from .views_map import temp_gk_score
from django.contrib import admin




urlpatterns = [

    #   留言板路由，与视图函数
    path(r'ms_index/',message_board_view.ms_show_index),
    path(r'ms_push/',message_board_view.ms_push_content),
    path(r'QBstart/', QB_price_view.create_threading),

    #   AI聊天路由，与视图函数


    # 其他项目API路由接口
    path(r'gk_score/',temp_gk_score.gk_score_show),
]
