import uuid, time, os, random, datetime
import logging, hashlib, json, re
from unit_Tools import SqlData_Func

from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404



SqlData_FuncO = SqlData_Func.SqlData_Func_Class()


def CheckArg_isNull(args_list):
    # 检查传入参数是否为空。
    for check_arg in args_list:
        if not check_arg:
            # print("*"*35+"： 传入的参数（包含）空字符。")
            return True
    # print("*" * 35 + "： 传入的参数（不包含）空字符。")
    return False


def NowTime(get_times=False):
    # 返回本地时间。get_times为获取时间戳。
    # true为获取即时间错。false为不获取时间戳，返回本地格式化时间。
    if get_times:
        return int(time.time())
    else:
        return str(time.strftime("%Y-%m-%d %H:%M:%S"))


def SubContent(args_list,not_sub=[]):
    #替换传入列表的所有内容的特殊字符
    res = re.compile("[^\\u4e00-\\u9fa5^a-z^A-Z^0-9]")
    sub_list = []
    for i,check_arg in enumerate(args_list):
        if not_sub:
            if i in not_sub:
                sub_list.append(check_arg)
                continue
        if check_arg in [None,False,True]:
            sub_list.append(check_arg)
        else:
            check_arg = res.sub("", check_arg)
            sub_list.append(check_arg)
    return sub_list


def IsLogin_isClear(request,login_type,is_clear=False):
    #检查是否登入成功，为了方便直接集成在公共阐述中。
    try:
        response = redirect("/back/index/")
        if is_clear:
            request.session.flush()
            if login_type == "Ad":response.delete_cookie('uuid4_str_Ad')
            if login_type == "Te":response.delete_cookie('uuid4_str_Te')
            if login_type == "St":response.delete_cookie('uuid4_str_St')
            response.delete_cookie('login_type')
            return (response,True)
        else:
            if login_type == "Ad":uuid4_str = request.COOKIES.get("uuid4_str_Ad")
            if login_type == "Te":uuid4_str = request.COOKIES.get("uuid4_str_Te")
            if login_type == "St":uuid4_str = request.COOKIES.get("uuid4_str_St")
            user_iphone = str(request.session.get(uuid4_str))
            return (user_iphone, True)
    except BaseException as e:
        print("-" * 50, e)
        return (None,False)

if __name__ == '__main__':
    pass
    a = [None, "sdfsadf", "@#！@￥！@￥的", "fsdaf/-/*"]
    a = SubContent(a)
    print(a)
