# -*- coding:utf-8 -*-
from django.urls import path,include,re_path
from . import views

urlpatterns = [
	# 登录页面
	re_path(r'^$', views.recommend_view, name='Recommend'),
 ]
