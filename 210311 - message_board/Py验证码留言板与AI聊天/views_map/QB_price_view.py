from ..tools_map import mysql_manager
from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import uuid, time, os, random,datetime
import logging, hashlib, json
from tools_API.get_QB_price import write_mysql
import threading

tool_mysql = mysql_manager.SqlManger()



def create_threading(request):
    print(threading.enumerate())
    if threading.active_count() >= 4:
        return HttpResponse("已启动线程...")
    else:
        print("------------------------------------------")
        t1 = threading.Thread(target=start_get_qb_price)
        t1.start()
        return HttpResponse("第一次启动中...")

def start_get_qb_price():
    try:
        write_mysql()
    except BaseException as e:
        print(e)
        time.sleep(1)
        write_mysql()

    while True:
        now = datetime.datetime.now()
        # 到达设定时间，结束内循环
        if now.minute == 59:
            try:
                write_mysql()
                time.sleep(60)
            except BaseException as e:
                write_mysql()
        # 等20秒之后再次检测
        time.sleep(28)
    return HttpResponse(200)



