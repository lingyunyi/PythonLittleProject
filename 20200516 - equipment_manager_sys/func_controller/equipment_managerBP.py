from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import threading, requests
import uuid, time, os
import logging, hashlib, json

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from func_tools.sql_manager import SqlManger
from equipment_manager_sys.settings import Domain_url

func_tools_sql_manager = SqlManger()


def equipment_manager_show(request):
    '''
        展示目前存在在数据仓库
    :param request:
    :return:
    '''
    ret = {"status": "false", "mesg": "Null"}
    # 定义三个获取数据的方式
    # API接口 {
    # 仓库名称：storehouse_id
    # 搜索内容：search_content
    # }
    if request.method == "GET":
        try:
            storehouse_id = request.GET.get("storehouse_id", None)
        except BaseException as e:
            ret["mesg"] = "获取args错误"
            return HttpResponse(json.dumps(ret))
        return render(request, 'Users/equipment_manager.html', {
            'storehouse_id': storehouse_id
        })
    # 如果使用POST请求返回JSON的字符串
    return HttpResponse(json.dumps(ret))


def equipment_manager_show_insert(request):
    '''
        需要对接API
    :param request:
    :return:
    '''
    ret = {"status": "false", "mesg": "Null"}
    if request.method == "GET":
        sql = '''select * from storehouse_manager where storehouse_is_del = 0'''
        select_storehouse_list = func_tools_sql_manager.search(sql, [])
        if select_storehouse_list != ():
            return render(request, 'Users/equipment_manager_insert.html', {
                'select_storehouse_list': select_storehouse_list
            })
    # 如果使用POST请求返回JSON的字符串
    return HttpResponse(json.dumps(ret))



def equipment_manager_details(request):
    '''
        需要对接API
    :param request:
    :return:
    '''
    ret = {"status": "false", "mesg": "Null"}
    if request.method == "GET":
        try:
            equipment_id = request.GET.get('equipment_id',None)
        except BaseException as e :
            return HttpResponse(json.dumps(ret))
            print(e)

        return render(request, 'Users/equipment_manager_details.html', {
            'equipment_id':equipment_id
        })
    # 如果使用POST请求返回JSON的字符串
    return HttpResponse(json.dumps(ret))