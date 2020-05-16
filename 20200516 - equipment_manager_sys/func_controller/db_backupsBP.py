from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import threading, requests
import uuid, time, os
import logging, hashlib, json


def db_backups_show(request):
    '''

    :param request:
    :return:
    '''
    recv_list = all_path('static/backups_dir')
    backups_list = []
    for n,i in enumerate(recv_list):
        file_name = i.split("\\")[-1]
        backups_list.append([n,file_name])
    backups_list.sort(reverse=True)
    return render(request,'Backups/DB_backups.html',{
        'backups_list':backups_list[:10]
    })


def all_path(dirname):

    result = []#所有的文件

    for maindir, subdir, file_name_list in os.walk(dirname):

        print("1:",maindir) #当前主目录
        print("2:",subdir) #当前主目录下的所有目录
        print("3:",file_name_list)  #当前主目录下的所有文件

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#合并成一个完整路径
            if apath.split('.')[-1] == "sql":
                result.append(apath)
    return result