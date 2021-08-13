from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import uuid, time, os, random,datetime
import logging, hashlib, json

from unit_Tools.sqlData_unitTools import sqlData_unitTools

sqlData_unitToolsC = sqlData_unitTools()

def infoMa_logout(request):
    '''
        登出 视图函数
    :param request:
    :return:
    '''
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    if request.method == "GET":
        print("-" * 15, "ViewFunc infoMa_logout - Get", "-" * 15)
        response = redirect('/')
        try:
            uuid4_str = request.COOKIES.get("username_id")
            user_name = str(request.session.get(uuid4_str))
            request.session.flush()
            response.delete_cookie('username_id')
        except BaseException as e:
            print("-"*50,e)
            return  response
        return response
    elif request.method == "POST":
        print("-" * 15, "ViewFunc infoMa_logout - POST", "-" * 15)
        return redirect('/')

def infoMa_login(request):
    '''
        登入 视图函数
    :param request:
    :return:
    '''
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    if request.method == "GET":
        print("-" * 15, "ViewFunc infoMa_login - Get", "-" * 15)
        return render(request, "admins/admins_login.html")
    elif request.method == "POST":
        print("-" * 15, "ViewFunc infoMa_login - POST", "-" * 15)
        # 通过前端传入的 post 数据判断账号密码是否正确，正确则返回登入成功，错误则提示。
        users_account = request.POST.get("users_account")
        users_passwd = request.POST.get("users_passwd")
        users_passwd = hashlib.md5(str(users_passwd).encode("utf-8")).hexdigest()
        # 构造Json返回值，用于返回数据，返回类型，返回结果
        jsonStr = {"status": "false", "tip": ""}
        if users_account != None and users_passwd != None:
            # 如果账号不为空
            sql = '''select * from account where username = %s and passwd = %s'''
            # 通过构造sql语言，判断是否登入成功
            login_result = sqlData_unitToolsC.search(sql,[users_account,users_passwd])
            if login_result:
                jsonStr["status"] = "true"
                jsonStr["tip"] = "login success"
                uuid4_str = str(uuid.uuid4())
                request.session[uuid4_str] = users_account
                obj = HttpResponse(json.dumps(jsonStr))
                obj.set_cookie("username_id", uuid4_str, 60 * 60 * 24)
            else:
                jsonStr["tip"] = "login false"
        return obj