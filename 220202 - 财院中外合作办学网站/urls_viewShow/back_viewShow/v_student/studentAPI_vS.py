from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import uuid, time, os, random, datetime
import logging, hashlib, json
from unit_Tools import Base_Setting
from unit_Tools import Public_Func
from unit_Tools.Public_Func import SqlData_FuncO


def check_isLoginAPI(request, infomation=False):
    # 检查是否登入，并赋值给全局变量返回值
    uuid4_str_St = str(request.session.get(request.COOKIES.get("uuid4_str_St")))
    login_type = request.COOKIES.get("login_type")
    print("*"*50,"check_isLoginAPI",uuid4_str_St,login_type)
    Base_Setting.Back_Common_Render["uuid4_str_St"] = uuid4_str_St
    if uuid4_str_St == "None" or login_type == "None":
        return (redirect("/back/index/"), False)
    check_St_Infomation(uuid4_str_St)
    if infomation:
        return (None, True)
    if Base_Setting.St_Infomation["is_null"] == "True":
        check_St_Infomation(uuid4_str_St)
        if Base_Setting.St_Infomation["i_name"] == "":
            return (redirect("/back/st/infomation/"), False)
    return (None, True)


def check_St_Infomation(uuid4_str_St):
    # 检查是否登入，并赋值给全局变量返回值
    sql = "select user_info_dict from account_tb where user_iphone = %s and user_type = 'St'"
    Get, T_F = SqlData_FuncO.search(sql, [uuid4_str_St])
    if T_F:
        if Get[0][0] != None and Get[0][0] != "":
            Base_Setting.Back_Common_Render["St_Infomation"] = Base_Setting.St_Infomation = json.loads(Get[0][0])
    print(Base_Setting.St_Infomation)

def infomationModify_API(request):
    redirectA, T_F = check_isLoginAPI(request, infomation=True)
    if not T_F: return redirectA
    # 接受前端数据，执行数据库插入
    OOOOO = {"modify_result": "False", "modify_tip": "", }
    if request.method == "POST":
        Base_Setting.St_Infomation["i_name"] = str(request.POST.get("i_name")).replace(" ", "")
        Base_Setting.St_Infomation["i_institute"] = str(request.POST.get("i_institute")).replace(" ", "")
        Base_Setting.St_Infomation["i_cardID"] = str(request.POST.get("i_cardID")).replace(" ", "")
        Base_Setting.St_Infomation["i_class"] = str(request.POST.get("i_class")).replace(" ", "")
        Base_Setting.St_Infomation["is_null"] = "False"
        sql = "UPDATE account_tb SET user_info_dict = %s WHERE user_iphone = %s and user_type = 'St'"
        Err, T_F = SqlData_FuncO.excute(sql, [json.dumps(Base_Setting.St_Infomation),
                                              Base_Setting.Back_Common_Render["uuid4_str_St"]])
        if Err:
            OOOOO["modify_tip"] = Err
        if T_F:
            OOOOO["modify_result"] = "True"
    return HttpResponse(json.dumps(OOOOO))


def teAstWallShow_API(request):
    redirectA, T_F = check_isLoginAPI(request, infomation=True)
    if not T_F: return redirectA
    # 教室与学生留言内容展示
    OOOOO = {"show_data": "", "show_tip": ""}
    if request.method == "POST":
        search_content = str(request.POST.get("search_content")).replace(" ", "")
        sql = "select * from te_st_Wall_tb where is_delete = 0 and user_iphone = %s and te_a_st = 'St' order by id desc limit 1000"
        GetData, T_F = SqlData_FuncO.search(sql,[Base_Setting.Back_Common_Render["uuid4_str_St"]])
        if T_F:
            return_Data = []
            if search_content != "":
                for row in GetData:
                    print("-" * 50, "teAstWallShow_API：search_content", search_content)
                    if search_content in "-".join('%s' % i for i in row):
                        return_Data.append(row)
            else:
                return_Data = list(GetData)
            OOOOO["show_data"] = return_Data
        if not T_F:
            OOOOO["show_tip"] = GetData
    return HttpResponse(json.dumps(OOOOO))

def contentDelete_API(request):
    redirectA, T_F = check_isLoginAPI(request, infomation=True)
    if not T_F: return redirectA
    # 接受前端数据，将数据库内容进行删除
    OOOOO = {"delete_result": "False", "delete_tip": ""}
    if request.method == "POST":
        deleteID = str(request.POST.get("deleteID")).replace(" ", "")
        sql = " UPDATE notice_tb SET is_delete = 1 WHERE id = %s "
        Err, T_F = SqlData_FuncO.excute(sql, [deleteID])
        if Err:
            OOOOO["delete_tip"] = Err
        if T_F:
            OOOOO["delete_result"] = "True"
    return HttpResponse(json.dumps(OOOOO))