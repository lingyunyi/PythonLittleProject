"""qr_code_create URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from views_func import main
from views_func import API

urlpatterns = [
    #path('admin/', admin.site.urls),
    # 主界面生成页面
    path("",main.index),
    #请求生成页面
    path("qr_code_create/",main.create_qrcode),
    # 个人信息系统界面
    path("infomation_db/",main.infomation_db),
    # 扫描展示的个人信息
    path("show_my_info/",API.show_my_info),

]
