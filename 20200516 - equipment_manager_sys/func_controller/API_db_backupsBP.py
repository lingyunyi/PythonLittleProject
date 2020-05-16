from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import threading, requests
import uuid, time, os
import logging, hashlib, json



def API_db_backups_save(request):
    '''
    :param request:
    :return:
    '''
    ret = {"status": "fales", "mesg": "Null"}
    try:
        DB_USER = 'root'
        DB_PASSWORD = 'root'
        DB_NAME = 'equipment_manager'
        TODAY = time.strftime('%Y-%m-%d-%H-%M-%S')  #
        BACK_DIR= r'E:\PythonProject\equipment_manager_sys\static\backups_dir/'
        TODAY_DIR = BACK_DIR + TODAY
        # 如果目录不存在，新建目录
        # 执行mysql命令，导出数据库到新建的文件
        mysql_dump_dir = r'D:\xampp\MySQL\bin\mysqldump.exe'
        sqlcmd = mysql_dump_dir + " --single-transaction -u" + DB_USER + " -p" + DB_PASSWORD + " " + DB_NAME + " > " + TODAY_DIR  + ".sql"
        print(sqlcmd)
        res = os.popen(sqlcmd)
        print(res)
        ret["status"] = "true"
    except BaseException as e:
        ret["mesg"] = e
    return HttpResponse(json.dumps(ret))






