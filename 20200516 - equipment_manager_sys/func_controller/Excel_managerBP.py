from django.http import request
from django.shortcuts import redirect,render,HttpResponse,Http404
import threading,requests
import uuid,time,os
import logging,hashlib,json
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from func_tools.sql_manager import SqlManger
from func_tools.sql_and_excel import Sql_2to2_Excel


func_tools_sql_manager = SqlManger()
func_tools_sql_and_excel = Sql_2to2_Excel()

def excel_manager_show(request):
    ret = {"status": "false", "mesg": "Null"}
    if request.method == "GET":
        sql = '''select * from storehouse_manager where storehouse_is_del = 0 ORDER BY storehouse_id DESC'''
        select_storehouse_list = func_tools_sql_manager.search(sql, [])
        if select_storehouse_list != ():
            return render(request, 'Users/excel_manager.html', {
                'select_storehouse_list': select_storehouse_list
            })
    # 如果使用POST请求返回JSON的字符串
    return HttpResponse(json.dumps(ret))


def API_excel_manager_output_excel(request):
    ret = {"status": "false", "mesg": "Null","excel_path":""}
    if request.method == "GET":
        excel_path = func_tools_sql_and_excel.return_storehouse_to_excel()
        if excel_path != False:
            ret["status"] = "true"
            ret["excel_path"] =  excel_path
            return HttpResponse(json.dumps(ret))
    # 如果使用POST请求返回JSON的字符串
    return HttpResponse(json.dumps(ret))

def API_excel_manager_excel_input_sql(request):
    ret = {"status": "false", "mesg": "Null","excel_path":""}
    str_uuid = str(uuid.uuid4())
    if request.method == "POST":
        storehouse_id = request.POST.get("storehouse_id", None)
        file_content = request.FILES.get('file_content', None)
        files_path = r'static/input_excel/%s.xlsx'%(str_uuid)
        try:
            if storehouse_id != None and file_content != None:
                with open(files_path, 'wb') as f:
                    for line in file_content.chunks():
                        f.write(line)
                    f.close()
                insert_data = func_tools_sql_and_excel.get_input_excel_to_sql(storehouse_id=storehouse_id,excel_path=files_path)
                if insert_data != False:
                    ret["status"] = "true"
                    return HttpResponse(json.dumps(ret))
        except BaseException as e :
            print(e)
    # 如果使用POST请求返回JSON的字符串
    return HttpResponse(json.dumps(ret))

