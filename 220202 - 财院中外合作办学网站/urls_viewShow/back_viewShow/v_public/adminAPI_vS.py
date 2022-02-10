from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import uuid, time, os, random, datetime
import logging, hashlib, json
from unit_Tools import Base_Setting
from unit_Tools import Public_Func
from unit_Tools.Public_Func import SqlData_FuncO


def infomationModify_API(request):
    redirectA, T_F = check_isLoginAPI(request, infomation=True)
    if not T_F: return redirectA
    # 接受前端数据，执行数据库插入
    OOOOO = {"modify_result": "False", "modify_tip": "", }
    if request.method == "POST":
        Base_Setting.Ad_Infomation["i_name"] = str(request.POST.get("i_name")).replace(" ", "")
        Base_Setting.Ad_Infomation["i_cardID"] = str(request.POST.get("i_cardID")).replace(" ", "")
        Base_Setting.Ad_Infomation["i_institute"] = str(request.POST.get("i_institute")).replace(" ", "")
        Base_Setting.Ad_Infomation["is_null"] = "False"
        sql = "UPDATE account_tb SET user_info_dict = %s WHERE user_iphone = %s and user_type = 'Ad'"
        Err, T_F = SqlData_FuncO.excute(sql, [json.dumps(Base_Setting.Ad_Infomation),
                                              Base_Setting.Back_Common_Render["uuid4_str_Ad"]])
        if Err:
            OOOOO["modify_tip"] = Err
        if T_F:
            OOOOO["modify_result"] = "True"
    return HttpResponse(json.dumps(OOOOO))


def contentAdd_API(request):
    redirectA, T_F = check_isLoginAPI(request, infomation=True)
    if not T_F: return redirectA
    # 接受前端数据，执行数据库插入
    OOOOO = {"insert_result": "False", "insert_tip": "", }
    if request.method == "POST":
        content_title = str(request.POST.get("content_title")).replace(" ", "")
        wx_url = str(request.POST.get("wx_url")).replace(" ", "")
        content_type = str(request.POST.get("content_type"))
        if not Public_Func.CheckArg_isNull([content_title, wx_url, content_type]):
            if content_type == "notice": sql = "insert into notice_tb values (%s,%s,%s,%s,%s,%s,%s)"
            if content_type == "news": sql = "insert into news_tb values (%s,%s,%s,%s,%s,%s,%s)"
            if content_type == "download": sql = "insert into download_tb values (%s,%s,%s,%s,%s,%s,%s)"
            if content_type == "law": sql = "insert into law_tb values (%s,%s,%s,%s,%s,%s,%s)"
            Err, T_F = SqlData_FuncO.excute(sql, Public_Func.SubContent(
                [None, Base_Setting.Back_Common_Render["uuid4_str_Ad"], Base_Setting.Ad_Infomation["i_name"],
                 content_title, wx_url,
                 Public_Func.NowTime(), 0], not_sub=[5, 3, 4]))
            if Err:
                OOOOO["insert_tip"] = Err
            if T_F:
                OOOOO["insert_result"] = "True"
    return HttpResponse(json.dumps(OOOOO))


def contentShow_API(request):
    redirectA, T_F = check_isLoginAPI(request, infomation=True)
    if not T_F: return redirectA
    # 接受前端数据，向前端提供数据库数据
    OOOOO = {"show_result": "False", "show_data": "", "show_tip": ""}
    if request.method == "POST":
        search_content = str(request.POST.get("search_content")).replace(" ", "")
        content_type = request.POST.get("content_type")
        if content_type == "notice": sql = "select * from notice_tb where is_delete = 0 order by id desc limit 1000"
        if content_type == "news": sql = "select * from news_tb where is_delete = 0 order by id desc limit 1000"
        if content_type == "download": sql = "select * from download_tb where is_delete = 0 order by id desc limit 1000"
        if content_type == "law": sql = "select * from law_tb where is_delete = 0 order by id desc limit 1000"
        GetData, T_F = SqlData_FuncO.search(sql)
        if T_F:
            return_Data = []
            if search_content != "":
                print("-" * 50, "contentShow_API：search_content", search_content)
                for row in GetData:
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
        content_type = request.POST.get("content_type")
        if content_type == "notice": sql = " UPDATE notice_tb SET is_delete = 1 WHERE id = %s "
        if content_type == "news": sql = " UPDATE news_tb SET is_delete = 1 WHERE id = %s "
        if content_type == "download": sql = " UPDATE download_tb SET is_delete = 1 WHERE id = %s "
        if content_type == "law": sql = " UPDATE law_tb SET is_delete = 1 WHERE id = %s "
        Err, T_F = SqlData_FuncO.excute(sql, [deleteID])
        if Err:
            OOOOO["delete_tip"] = Err
        if T_F:
            OOOOO["delete_result"] = "True"
    return HttpResponse(json.dumps(OOOOO))


def check_isLoginAPI(request, infomation=False):
    # 检查是否登入，并赋值给全局变量返回值
    uuid4_str_Ad = str(request.session.get(request.COOKIES.get("uuid4_str_Ad")))
    login_type = request.COOKIES.get("login_type")
    Base_Setting.Back_Common_Render["uuid4_str_Ad"] = uuid4_str_Ad
    if uuid4_str_Ad == "None" or login_type == "None":
        print("*" * 50, "ADcheck_isLoginAPI", uuid4_str_Ad, login_type, '"redirect("/back/index/")"')
        return (redirect("/back/index/"), False)
    check_Ad_Infomation(uuid4_str_Ad)
    if infomation:
        print("*" * 50, "ADcheck_isLoginAPI", uuid4_str_Ad, login_type, "None")
        return (None, True)
    if Base_Setting.Ad_Infomation["is_null"] == "True":
        check_Ad_Infomation(uuid4_str_Ad)
        if Base_Setting.Ad_Infomation["i_name"] == "":
            print("*" * 50, "ADcheck_isLoginAPI", uuid4_str_Ad, login_type, '"/back/ad/infomation/"')
            return (redirect("/back/ad/infomation/"), False)
    return (None, True)


def check_Ad_Infomation(uuid4_str_Ad):
    # 检查是否登入，并赋值给全局变量返回值
    sql = "select user_info_dict from account_tb where user_iphone = %s and user_type = 'Ad'"
    Get, T_F = SqlData_FuncO.search(sql, [uuid4_str_Ad])
    if T_F:
        if Get[0][0] != None and Get[0][0] != "":
            Base_Setting.Back_Common_Render["Ad_Infomation"] = Base_Setting.Ad_Infomation = json.loads(Get[0][0])
    print(Base_Setting.Ad_Infomation)


def teAstWallShow_API(request):
    redirectA, T_F = check_isLoginAPI(request, infomation=True)
    if not T_F: return redirectA
    # 教室与学生留言内容展示
    OOOOO = {"show_data": "", "show_tip": ""}
    if request.method == "POST":
        search_content = str(request.POST.get("search_content")).replace(" ", "")
        sql = "select * from te_st_Wall_tb where is_delete = 0 order by id desc limit 1000"
        GetData, T_F = SqlData_FuncO.search(sql)
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


def teAstWallDelete_API(request):
    # redirectA, T_F = check_isLoginAPI(request, infomation=True)
    # if not T_F: return redirectA
    # 留言墙内容删除
    login_type = request.COOKIES.get("login_type")
    OOOOO = {"delete_result": "False", "delete_tip": ""}
    if not login_type: return HttpResponse(json.dumps(OOOOO))
    if request.method == "POST":
        deleteID = str(request.POST.get("deleteID")).replace(" ", "")
        if login_type == "Ad":
            sql = " UPDATE te_st_wall_tb SET is_delete = 1 WHERE id = %s "
            Err, T_F = SqlData_FuncO.excute(sql, [deleteID])
        else:
            sql = " UPDATE te_st_wall_tb SET is_delete = 1 WHERE id = %s and te_a_st = %s"
            Err, T_F = SqlData_FuncO.excute(sql, [deleteID, login_type])
        if Err:
            OOOOO["delete_tip"] = Err
        if T_F:
            OOOOO["delete_result"] = "True"
    return HttpResponse(json.dumps(OOOOO))


def all_teAstWallAdd_API(request):
    OOOOO = {"insert_result": "False", "insert_tip": "", }
    login_type = request.COOKIES.get("login_type")
    if request.method == "POST":
        try:
            content_title = request.POST.get("content_title", None)
            InputFile = request.FILES.get('InputFile', None)
            if InputFile:
                inputFile_nameE = str(InputFile.name).split(".")[-1]
                files_path = r'static/back_static/s_public/imgs_files/%s.%s' % (str(uuid.uuid4()), inputFile_nameE)
                if not inputFile_nameE in ["jpg", "jpge", "png"]:
                    OOOOO["insert_tip"] = "（Ooo  非法文件，非图像文件  ooO）"
                    return HttpResponse(json.dumps(OOOOO))

            print(content_title, InputFile, login_type)

            if login_type == "Te":
                user_iphone = Base_Setting.Back_Common_Render["uuid4_str_Te"]
                user_name = Base_Setting.Te_Infomation["i_name"]
            if login_type == "St":
                user_iphone = Base_Setting.Back_Common_Render["uuid4_str_St"]
                user_name = Base_Setting.St_Infomation["i_name"]

            if content_title != None and InputFile == None:
                print("*" * 50, "：如果不上传文件，紧紧只有留言内容。")
                files_path = ""
                sql = "insert into te_st_wall_tb values (%s,%s,%s,%s,%s,%s,%s,%s)"
                Err, T_F = SqlData_FuncO.excute(sql, [None, user_iphone, user_name, content_title, files_path,
                                                      Public_Func.NowTime(), login_type, 0])
                if T_F:
                    OOOOO["insert_result"] = "True"
                if not T_F:
                    OOOOO["insert_tip"] = Err

            if content_title != None and InputFile != None and login_type != "None":
                print("*" * 50, "：如果上传文件。")
                with open(files_path, 'wb') as f:
                    for line in InputFile.chunks():
                        f.write(line)
                    f.close()
                sql = "insert into te_st_wall_tb values (%s,%s,%s,%s,%s,%s,%s,%s)"
                Err, T_F = SqlData_FuncO.excute(sql, [None, user_iphone, user_name, content_title, files_path,
                                                      Public_Func.NowTime(), login_type, 0])
                if T_F:
                    OOOOO["insert_result"] = "True"
                if not T_F:
                    OOOOO["insert_tip"] = Err
        except BaseException as e:
            OOOOO["insert_tip"] = str(e)
    return HttpResponse(json.dumps(OOOOO))
