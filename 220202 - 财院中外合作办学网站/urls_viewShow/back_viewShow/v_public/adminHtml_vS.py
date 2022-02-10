from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import uuid, time, os, random, datetime
import logging, hashlib, json
from unit_Tools import Base_Setting
from unit_Tools import Public_Func
from unit_Tools.Public_Func import SqlData_FuncO
from urls_viewShow.back_viewShow.v_public import adminAPI_vS



def bc_ad_infomation(request):
    redirectA,T_F = adminAPI_vS.check_isLoginAPI(request,infomation=True)
    if not T_F:return redirectA
    # 管理员信息
    if request.method == "GET":
        return render(request, "back_web/w_public/ad_infomation.html", Base_Setting.Back_Common_Render)

def bc_ad_notice(request):
    redirectA,T_F = adminAPI_vS.check_isLoginAPI(request)
    if not T_F:return redirectA
    # 通知公告
    if request.method == "GET":
        return render(request, "back_web/w_public/ad_notice.html", Base_Setting.Back_Common_Render)

def bc_ad_news(request):
    redirectA,T_F = adminAPI_vS.check_isLoginAPI(request)
    if not T_F:return redirectA
    # 新闻动态
    if request.method == "GET":
        return render(request, "back_web/w_public/ad_news.html", Base_Setting.Back_Common_Render)

def bc_ad_download(request):
    redirectA,T_F = adminAPI_vS.check_isLoginAPI(request)
    if not T_F:return redirectA
    # 下载中心
    if request.method == "GET":
        return render(request, "back_web/w_public/ad_download.html", Base_Setting.Back_Common_Render)

def bc_ad_law(request):
    redirectA,T_F = adminAPI_vS.check_isLoginAPI(request)
    if not T_F:return redirectA
    # 法规制度
    if request.method == "GET":
        return render(request, "back_web/w_public/ad_law.html", Base_Setting.Back_Common_Render)

def bc_ad_teAstWall(request):
    redirectA,T_F = adminAPI_vS.check_isLoginAPI(request)
    if not T_F:return redirectA
    # 法规制度
    if request.method == "GET":
        return render(request, "back_web/w_public/ad_teAstWall.html", Base_Setting.Back_Common_Render)

def bc_ad_contentAdd(request):
    redirectA,T_F = adminAPI_vS.check_isLoginAPI(request)
    if not T_F:return redirectA
    # 法规制度
    if request.method == "GET":
        return render(request, "back_web/w_public/ad_content_add.html", Base_Setting.Back_Common_Render)