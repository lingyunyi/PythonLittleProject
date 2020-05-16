from django.http import request
from django.shortcuts import redirect,render,HttpResponse,Http404
import threading,requests
import uuid,time,os
import logging,hashlib,json
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from func_tools.sql_manager import SqlManger

func_tools_sql_manager = SqlManger()



def storehouse_manager_show(request):
    '''
        展示目前存在在数据仓库
    :param request:
    :return:
    '''
    ret = {"status":"flase","mesg":"Null"}
    if request.method == "GET":
        # 查询数据库SQL
        sql = '''select * from storehouse_manager where storehouse_is_del = 0 ORDER BY storehouse_id DESC'''
        select_storehouse = func_tools_sql_manager.search(sql,[])
        logger.warning(select_storehouse)
        return render(request,'Users/storehouse_manager.html',{
            'storehouse_list':select_storehouse
        })
    # 如果使用POST请求返回JSON的字符串
    return HttpResponse(json.dumps(ret))

