from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import uuid, time, os, random, datetime
import logging, hashlib, json
from unit_Tools import Base_Setting
from unit_Tools import Public_Func
from unit_Tools.Public_Func import SqlData_FuncO


def Fr_contentShow_API(request):
    # 接受前端数据，向前端提供数据库数据
    OOOOO = {"show_result": "False", "show_data": "", "show_tip": ""}
    if request.method == "POST":
        search_content = str(request.POST.get("search_content")).replace(" ", "")
        number = str(request.POST.get("number")).replace(" ", "")
        content_type = request.POST.get("content_type")
        #获取需要抽取的数据库结果数量，用于limit
        fir, end = count_firEnd(number,init=15)
        if content_type == "notice": sql = "select * from notice_tb where is_delete = 0 order by id desc limit {}".format("%s,%s"%(fir,end))
        if content_type == "news": sql = "select * from news_tb where is_delete = 0 order by id desc limit {}".format("%s,%s"%(fir,end))
        if content_type == "download": sql = "select * from download_tb where is_delete = 0 order by id desc limit {}".format("%s,%s"%(fir,end))
        if content_type == "law": sql = "select * from law_tb where is_delete = 0 order by id desc limit {}".format("%s,%s"%(fir,end))
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


def Fr_teWallShow_API(request, te_a_st='Te'):
    # 教室与学生留言内容展示
    OOOOO = {"show_data": "", "show_tip": ""}
    if request.method == "POST":
        number = request.POST.get("number")
        #获取需要抽取的数据库结果数量，用于limit
        fir, end = count_firEnd(number)
        sql = "select * from te_st_Wall_tb where is_delete = 0 and te_a_st = %s order by id desc limit {}".format("%s,%s"%(fir,end))
        GetData, T_F = SqlData_FuncO.search(sql, [te_a_st])
        if T_F:
            OOOOO["show_data"] = list(GetData)
        if not T_F:
            OOOOO["show_tip"] = GetData
    return HttpResponse(json.dumps(OOOOO))


def Fr_stWallShow_API(request, te_a_st='St'):
    # 教室与学生留言内容展示
    OOOOO = {"show_data": "", "show_tip": ""}
    if request.method == "POST":
        number = request.POST.get("number")
        #获取需要抽取的数据库结果数量，用于limit
        fir, end = count_firEnd(number)
        sql = "select * from te_st_Wall_tb where is_delete = 0 and te_a_st = %s order by id desc limit {}".format("%s,%s"%(fir,end))
        GetData, T_F = SqlData_FuncO.search(sql, [te_a_st])
        if T_F:
            return_Data = []
            return_Data = list(GetData)
            OOOOO["show_data"] = return_Data
        if not T_F:
            OOOOO["show_tip"] = GetData
    return HttpResponse(json.dumps(OOOOO))





def count_firEnd(number,init=32):
    if number: number = int(number)
    if number == 1:
        fir, end = str(0), str(init)
    else:
        fir, end = str(init * (number-1)), str(init)
    return fir, end
