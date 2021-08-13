from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import uuid, time, os, random, datetime
import logging, hashlib, json

from unit_Tools.sqlData_unitTools import sqlData_unitTools

sqlData_unitToolsC = sqlData_unitTools()


def activity_show(request):
    '''
        主题展示 视图函数
    :param request:
    :return:
    '''
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    try:
        uuid4_str = request.COOKIES.get("username_id")
        user_nameQ = str(request.session.get(uuid4_str))
        user_name = hashlib.md5(str(user_nameQ).encode("utf-8")).hexdigest()
        if uuid4_str == None:
            print("-"*100)
            return redirect('/')
    except BaseException as e:
        print("-" * 50, e)
        return redirect('/')

    if request.method == "GET":
        print("-" * 15, "ViewFunc activity_show - Get", "-" * 15)
        return render(request, "admins/activity_show.html",{"user_name":user_nameQ})
    elif request.method == "POST":
        print("-" * 15, "ViewFunc activity_show - POST", "-" * 15)
        search_content = request.POST.get('search_content', "None")
        sql = '''select infoCol from infomana where accountName = %s order by id desc limit 1000 '''
        infoMalist = sqlData_unitToolsC.search(sql,[user_name],show=False)
        return_jsonList = []
        if infoMalist:
            infoMalist = [json.loads(i[0]) for i in infoMalist]
            if search_content == "search_all" or search_content == None:
                # 如果全搜索的话，不需要筛选数据，直接把所有数据返回即可
                for i in infoMalist:
                    return_jsonList.append(str(i))
            else:
                for i in infoMalist:
                    if search_content in str(i.get("title", None)):
                        return_jsonList.append(str(i))
        return HttpResponse(json.dumps(return_jsonList))


def activity_add(request):
    '''
        主题增加 视图函数
    :param request:
    :return:
    '''
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    try:
        uuid4_str = request.COOKIES.get("username_id")
        user_nameQ = str(request.session.get(uuid4_str))
        user_name = hashlib.md5(str(user_nameQ).encode("utf-8")).hexdigest()
        if uuid4_str == None:
            print("-"*100)
            return redirect('/')
    except BaseException as e:
        print("-" * 50, e)
        return redirect('/')

    if request.method == "GET":
        print("-" * 15, "ViewFunc activity_add - Get", "-" * 15)
        return render(request, "admins/activity_add.html",{"user_name":user_nameQ})
    elif request.method == "POST":
        print("-" * 15, "ViewFunc activity_add - POST", "-" * 15)
        # 对从前端接受的数组，进行处理和提取，前端传入后端时，采用str字符串的形式传入，后经过使用python动态的eval解析进行反解。
        input_array = request.POST.get("input_array", None)
        input_array = [i for i in eval(input_array) if i != '']
        add_Json_model = {
            "title": "",
            "CreateTime": "",
            "infoList": [
            ]
        }
        # 将得到的数据，根据格式写入到  格式模板中。
        if len(input_array) >= 1:
            add_Json_model["title"] = input_array[0]
            add_Json_model["CreateTime"] = time.strftime("%Y-%m-%d %H:%M:%S")
            for i in input_array[1:]:
                add_Json_model["infoList"].append({"content": str(i), "insertTime": time.strftime("%Y-%m-%d %H:%M:%S"),"uuid":str(uuid.uuid4())})
        # 设计返回类型的Json格式。用于返回前端作为响应数据。
        jsonStr = {"status": "false", "tip": ""}
        # 判断主题是否与内部的一直，如果一致则，不给予插入，并返回重复结果。
        sql = '''select infoCol from infomana where accountName = %s order by id desc limit 1000 '''
        infoMalist = sqlData_unitToolsC.search(sql, show=False)
        if infoMalist:
            for i in infoMalist:
                if add_Json_model["title"] == str(eval(i[0]).get("title", None)):
                    jsonStr["tip"] = "title已经存在，title不唯一。"
                    return HttpResponse(json.dumps(jsonStr))
        # 设计sql插入语言
        sql = '''insert into infomana values (%s,%s,%s)'''
        insert_result = sqlData_unitToolsC.excute(sql, [None, json.dumps(add_Json_model),user_name],show=False)
        if insert_result:
            jsonStr["status"] = "true"
            jsonStr["tip"] = "主题添加成功..."
        else:
            jsonStr["tip"] = "主题添加失败..."
        return HttpResponse(json.dumps(jsonStr))


def activity_modify(request):
    '''
        主题修改 视图函数
    :param request:
    :return:
    '''
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    try:
        uuid4_str = request.COOKIES.get("username_id")
        user_nameQ = str(request.session.get(uuid4_str))
        user_name = hashlib.md5(str(user_nameQ).encode("utf-8")).hexdigest()
        if uuid4_str == None:
            print("-"*100)
            return redirect('/')

    except BaseException as e:
        print("-" * 50, e)
        return redirect('/')

    if request.method == "GET":
        print("-" * 15, "ViewFunc activity_modify - Get", "-" * 15)
        title = request.GET.get("title", None)
        render_dict = {}
        if title:
            sql = '''select * from infomana where accountName = %s order by id desc limit 1000 '''
            infoMalist = sqlData_unitToolsC.search(sql,[user_name], show=False)
            if infoMalist:
                for i in infoMalist:
                    if title == json.loads(i[1]).get("title", None):
                        render_dict = json.loads(i[1])
                        render_dict.get("infoList").reverse()
                        if len(render_dict.get("infoList")) >=10:
                            render_dict["infoList"] = render_dict.get("infoList")[0:10]
        return render(request, "admins/activity_modify.html", {"render_dict": render_dict,"user_name":user_nameQ})
    elif request.method == "POST":
        print("-" * 15, "ViewFunc activity_modify - POST", "-" * 15)
        title = request.POST.get("title", None)
        operate = request.POST.get("operate", None)
        uuidX = request.POST.get("uuid", None)
        newContent = request.POST.get("newContent", None)
        jsonStr = {"status": "false", "tip": ""}
        if operate  and title:
            sql = '''select * from infomana where accountName = %s order by id desc limit 1000 '''
            infoMalist = sqlData_unitToolsC.search(sql, [user_name],show=False)
            if infoMalist:
                for i in infoMalist:
                    if title == json.loads(i[1]).get("title", None):
                        modify_id = i[0]
                        modify_dict = json.loads(i[1])
            if uuidX:
                sql = '''UPDATE infomana SET infoCol = %s WHERE id = %s and accountName = %s'''
                if operate == "delete":
                    for i in modify_dict.get("infoList",None):
                        if uuidX == i.get("uuid"):
                            uuid_index = modify_dict.get("infoList",None).index(i)
                            del modify_dict.get("infoList",None)[uuid_index]
                    updata_result = sqlData_unitToolsC.excute(sql,[json.dumps(modify_dict),modify_id,user_name])
                    if updata_result:
                        jsonStr["status"] = "true"
                        jsonStr["tip"] = "内容删除成功..."
                    else:
                        jsonStr["tip"] = "内容删除失败..."
                elif operate == "modify":
                    for i in modify_dict.get("infoList",None):
                        if uuidX == i.get("uuid"):
                           if newContent == i.get("content",None):
                               jsonStr["tip"] = "内容修改失败，请求修改内容后重试..."
                               return HttpResponse(json.dumps(jsonStr))
                           i["content"] = newContent
                    updata_result = sqlData_unitToolsC.excute(sql,[json.dumps(modify_dict),modify_id,user_name],show=False)
                    if updata_result:
                        jsonStr["status"] = "true"
                        jsonStr["tip"] = "内容修改成功..."
                    else:
                        jsonStr["tip"] = "内容修改失败..."
            else:
                if operate == "add":
                    modify_dict["infoList"].append({"content":newContent, "insertTime": time.strftime("%Y-%m-%d %H:%M:%S"),"uuid": str(uuid.uuid4())})
                    sql = '''UPDATE infomana SET infoCol = %s WHERE id = %s and accountName = %s'''
                    updata_result = sqlData_unitToolsC.excute(sql, [json.dumps(modify_dict), modify_id,user_name], show=False)
                    if updata_result:
                        jsonStr["status"] = "true"
                        jsonStr["tip"] = "内容添加成功..."
                    else:
                        jsonStr["tip"] = "内容添加失败..."
        return HttpResponse(json.dumps(jsonStr))




def activity_delete(request):
    '''
        主题修改 视图函数
    :param request:
    :return:
    '''
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    try:
        uuid4_str = request.COOKIES.get("username_id")
        user_nameQ = str(request.session.get(uuid4_str))
        user_name = hashlib.md5(str(user_nameQ).encode("utf-8")).hexdigest()
        if uuid4_str == None:
            print("-"*100)
            return redirect('/')

    except BaseException as e:
        print("-" * 50, e)
        return redirect('/')

    if request.method == "GET":
        print("-" * 15, "ViewFunc activity_modify - Get", "-" * 15)
        title = request.GET.get("title",None)
        jsonStr = {"status": "false", "tip": ""}
        if title:
            sql = '''select * from infomana where accountName = %s order by id desc limit 1000 '''
            infoMalist = sqlData_unitToolsC.search(sql,[user_name] ,show=False)
            if infoMalist:
                for i in infoMalist:
                    if title == json.loads(i[1]).get("title", None):
                        delete_id = i[0]
                        sql = '''DELETE FROM infomana WHERE id = %s and accountName = %s'''
                        delete_result = sqlData_unitToolsC.excute(sql, [delete_id,user_name],show=False)
                        if delete_result:
                            jsonStr["status"] = "true"
                            jsonStr["tip"] = "主题删除成功..."
                        else:
                            jsonStr["tip"] = "主题删除失败..."
        return HttpResponse(json.dumps(jsonStr))
    elif request.method == "POST":
        print("-" * 15, "ViewFunc activity_modify - POST", "-" * 15)
        pass


def activity_details(request):
    '''
        主题修改 视图函数
    :param request:
    :return:
    '''
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    try:
        uuid4_str = request.COOKIES.get("username_id")
        user_nameQ = str(request.session.get(uuid4_str))
        user_name = hashlib.md5(str(user_nameQ).encode("utf-8")).hexdigest()
        if uuid4_str == None:
            print("-"*100)
            return redirect('/')

    except BaseException as e:
        print("-" * 50, e)
        return redirect('/')

    if request.method == "GET":
        print("-" * 15, "ViewFunc activity_details - Get", "-" * 15)
        title = request.GET.get("title",None)
        render_dict = {}
        if title:
            sql = '''select * from infomana where accountName = %s order by id desc limit 1000 '''
            infoMalist = sqlData_unitToolsC.search(sql, [user_name],show=False)
            if infoMalist:
                for i in infoMalist:
                    if title == json.loads(i[1]).get("title", None):
                        render_dict = json.loads(i[1])
                        render_dict.get("infoList",None).reverse()
        return render(request, "admins/activity_details.html",{"render_dict":render_dict,"user_name":user_nameQ})
    elif request.method == "POST":
        print("-" * 15, "ViewFunc activity_details - POST", "-" * 15)
        pass