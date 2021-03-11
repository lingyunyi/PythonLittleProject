from ..tools_map import mysql_manager
from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import uuid, time, os, random,datetime
import logging, hashlib, json
from tools_API.get_QB_price import write_mysql
import threading



def gk_score_show(request):
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    with open('tools_API/Score_requests/data.txt', 'r',encoding="utf-8") as f:
        reader = json.loads(f.read())
        reader = [i for i in reader]
        for row in reader[1:]:
            row_innumsum = int(row[3]) + int(row[4])
            row_allnumsum = int(row[1]) + int(row[2])
            row.append("%s / %s（%s）"%(row_innumsum,row_allnumsum,((row_allnumsum-row_innumsum))))
        reader = sorted(reader[1:], key=lambda x: int(x[5].split('/')[0]), reverse=True)
        for num, row in enumerate(reader):
            row.append(int(num)+1)
        reader.insert(0,["院校名称", "普高类计划数", "中职类计划数", "普高类已报名人数", "中职类已报名人数", "总人数", "排名"])
        result_list = reader
    with open('tools_API/Score_requests/time.txt', 'r',encoding="utf-8") as f:
        timetime = json.loads(f.read())
    in_numsum = 0
    all_numsum = 0
    for i in result_list[1:]:
        in_numsum += (int(i[3]) + int(i[4]))
        all_numsum += (int(i[1]) + int(i[2]))
    tip = "%s - %s / %s（%s）" %(timetime["times"],in_numsum,all_numsum,((all_numsum-in_numsum)))
    return render(request, "../templates/html_message_board/temp_gk_score.html", {"result_list": result_list,"tip":tip})