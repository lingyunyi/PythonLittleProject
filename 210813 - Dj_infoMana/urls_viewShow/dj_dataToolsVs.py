from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import uuid, time, os, random, datetime
import logging, hashlib, json
from Dj_infoMana.settings import *

from unit_Tools.sqlData_unitTools import sqlData_unitTools

sqlData_unitToolsC = sqlData_unitTools()


def API_db_backups_save(request):
    '''
    :param request:
    :return:
    '''

    try:
        TODAY_DIR = BACK_DIR + str(time.strftime('%Y-%m-%d-%H-%M-%S'))
        # 如果目录不存在，新建目录
        # 执行mysql命令，导出数据库到新建的文件
        sqlcmd = mysql_dump_dir + " --single-transaction -u" + DB_USER + " -p" + DB_PASSWORD + " " + DB_NAME + " > " + TODAY_DIR + ".sql"
        print(sqlcmd)
        res = os.popen(sqlcmd)
        time.sleep(5)
        try:

            file = open('%s.sql' % (TODAY_DIR), 'rb')
            response = HttpResponse(file)
            file.close()
            response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
            response['Content-Disposition'] = 'attachment;filename="%s.sql"' % (TODAY_DIR.split('/')[-1])
            return response
        except BaseException as e:
            return HttpResponse(e)
    except BaseException as e:
        return HttpResponse(e)
