from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import uuid, time, os, random, datetime
import logging, hashlib, json
from unit_Tools import Base_Setting
from unit_Tools import Public_Func
from unit_Tools.Public_Func import SqlData_FuncO


def login_check_Api(login_iphone, login_passwd, login_checkCode, login_type):
    # login_type["Ad","Te","St"]
    # 注册视图，注册成功返回相应数值，注册失败输出失败原因
    try:
        sql = '''select * from accounttables where user_iphone = %s and user_passwd = %s and user_type = %s'''
        Get, T_F = SqlData_FuncO.search(sql, Public_Func.SubContent([login_iphone, login_passwd, login_type]))
        if T_F:
            return (None, True)
        # 我以将iphone设置成唯一索引，如果注册的账号不唯一，将引发1062数据库错误。
    except BaseException as e:
        print(">" * 30 + " login_check_Api: " + str(e))
    return (None, False)


def register_check_Api(regis_iphone, regis_passwd, regis_checkCode, regis_type):
    # regis_type["Ad","Te","St"]
    # 注册视图，注册成功返回相应数值，注册失败输出失败原因
    # 判断账号是否存在，判断是否注册成功
    try:
        sql = '''insert into AccountTables values (%s,%s,%s,%s,%s,%s)'''
        Err, T_F = SqlData_FuncO.excute(sql, Public_Func.SubContent([None, regis_iphone, regis_passwd, regis_type, Public_Func.NowTime(), 0]))
        if T_F:
            return (None, True)
        # 我以将iphone设置成唯一索引，如果注册的账号不唯一，将引发1062数据库错误。
        if eval(Err)[0] == 1062:
            return ("AcUnque", False)
    except BaseException as e:
        print(">" * 30 + " register_check_Api: " + str(e))
    return (None, False)


def login_vS(request):
    # 登入视图函数，判断是否登入成功，设置相应的cookies参数，并返回相应数值用于跳转。
    if request.method == "GET":
        return render(request, "back_web/w_public/admins_login.html", Base_Setting.Back_Common_Render)
    if request.method == "POST":
        model = request.POST.get("model")
        OOOOO = {"login_result": "False", "login_tip": "", "login_type": "", "regis_result": "False", "regis_tip": "",
                 "regis_type": "", }
        # 登入模块的视图处理
        if model == "Lo":
            login_iphone = request.POST.get("login_iphone")
            login_passwd = hashlib.md5(str(request.POST.get("login_passwd")).encode("utf-8")).hexdigest()
            login_checkCode = request.POST.get("login_checkCode")
            login_type = request.POST.get("login_type")
            login_argsList = [login_iphone, login_passwd, login_checkCode, login_type]
            # 检查传入的参数是否包含空
            if not Public_Func.CheckArg_isNull(login_argsList):
                OOOOO["login_type"] = login_type
                Err, T_F = login_check_Api(login_iphone, login_passwd, login_checkCode, login_type)
                if T_F:
                    OOOOO["login_result"] = "True"
                    OOOOO["login_tip"] = "login_success"
                    uuid4_str_Ad, uuid4_str_Te, uuid4_str_St = str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())
                    obj = HttpResponse(json.dumps(OOOOO))
                    if login_type == "Ad":
                        request.session[uuid4_str_Ad] = login_iphone
                        obj.set_cookie("uuid4_str_Ad", uuid4_str_Ad, 60 * 60 * 12)
                    if login_type == "Te":
                        request.session[uuid4_str_Te] = login_iphone
                        obj.set_cookie("uuid4_str_Te", uuid4_str_Te, 60 * 60 * 12)
                    if login_type == "St":
                        request.session[uuid4_str_St] = login_iphone
                        obj.set_cookie("uuid4_str_St", uuid4_str_St, 60 * 60 * 12)
                    Base_Setting.Common_Render["user_iphone"] = login_iphone
                    return obj
                if not T_F:
                    OOOOO["login_tip"] = "AnP_False"
        # 注册模块的视图处理
        elif model == "Re":
            regis_iphone = request.POST.get("regis_iphone")
            regis_passwd = hashlib.md5(str(request.POST.get("regis_passwd")).encode("utf-8")).hexdigest()
            regis_checkCode = request.POST.get("regis_checkCode")
            regis_type = request.POST.get("regis_type")
            regis_argsList = [regis_iphone, regis_passwd, regis_checkCode, regis_type]
            # 检查传入的参数是否包含空
            if not Public_Func.CheckArg_isNull(regis_argsList):
                OOOOO["regis_type"] = regis_type
                Err, T_F = register_check_Api(regis_iphone, regis_passwd, regis_checkCode, regis_type)
                if T_F:
                    OOOOO["regis_result"] = "True"
                    OOOOO["regis_tip"] = "register_success"
                if Err == "AcUnque":
                    OOOOO["regis_tip"] = "AcUnque"
        return HttpResponse(json.dumps(OOOOO))


def logout_anyone(request):
    #所有用户退出时清空所有cookies和session
    Public_Func.IsLogin_isClear(is_clear=True)