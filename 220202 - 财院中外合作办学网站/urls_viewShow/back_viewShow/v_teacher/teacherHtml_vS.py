from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import uuid, time, os, random, datetime
import logging, hashlib, json
from unit_Tools import Base_Setting
from unit_Tools import Public_Func
from unit_Tools.Public_Func import SqlData_FuncO
from urls_viewShow.back_viewShow.v_teacher import teacherAPI_vS


def bc_te_infomation(request):
    redirectA,T_F = teacherAPI_vS.check_isLoginAPI(request,infomation=True)
    if not T_F:return redirectA
    # 管理员信息
    if request.method == "GET":
        return render(request, "back_web/w_teacher/te_infomation.html", Base_Setting.Back_Common_Render)

def bc_te_teAstWall(request):
    redirectA,T_F = teacherAPI_vS.check_isLoginAPI(request)
    if not T_F:return redirectA
    # 管理员信息
    if request.method == "GET":
        return render(request, "back_web/w_teacher/te_teAstWall.html", Base_Setting.Back_Common_Render)

def bc_te_contentAdd(request):
    redirectA,T_F = teacherAPI_vS.check_isLoginAPI(request)
    if not T_F:return redirectA
    # 管理员信息
    if request.method == "GET":
        return render(request, "back_web/w_teacher/te_content_add.html", Base_Setting.Back_Common_Render)