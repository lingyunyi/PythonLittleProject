from django.http import request
from django.shortcuts import redirect,render,HttpResponse,Http404
import threading,requests
import uuid,time,os,json

from qr_code_create import settings
from tools.sql_manager import  SqlManger
import logging,hashlib

sql_manager_tools = SqlManger()

def show_my_info(request):
    '''

    :param request:
    :return:
    '''
    if request.method == "GET":
        try:
            nid = request.GET.get("nid",None)
            if nid != None and nid != "":
                sql = "select * from school_apartment where id = %s"
                select_my_info = sql_manager_tools.search(sql,[nid])
                print(select_my_info)
                if select_my_info != ():
                    return render(request,"myinfo.html",{
                        "select_my_info" : select_my_info[0]
                    })
        except BaseException as e:
            pass
    return HttpResponse(404)