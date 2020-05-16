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


def API_equipment_manager_insert(request):
    '''
        展示目前存在在数据仓库
    :param request:
    :return:
    '''
    ret = {"status": "false", "mesg": "Null", "DB": ""}
    if request.method == "POST":
        recv_db_list = request.POST.items
        print(recv_db_list)
        # 如果使用GET请求返回JSON的字符串
        print(recv_db_list != None)
        print(recv_db_list != "")
        if recv_db_list != None and recv_db_list != "":
            infomation_list = []
            for k, v in request.POST.items():
                if int(k) >= 2:
                    infomation_list.append(v)
                if int(k) == 0:
                    eq_id = v
                if int(k) == 1:
                    storehouse_id = v
            logger.warning([eq_id, storehouse_id, infomation_list])

            sql = '''insert into equipment_manager(equipment_id,equipment_classid,equipment_infomation) value (%s,%s,%s)'''
            insert_into_equipment_manager = func_tools_sql_manager.excute(sql, [eq_id, storehouse_id, json.dumps(infomation_list, ensure_ascii=False)])
            ret["status"] = "true"
            return HttpResponse(json.dumps(ret))
    return HttpResponse(json.dumps(ret))


def API_equipment_manager_show(request):
    '''
        展示目前存在在数据仓库
    :param request:
    :return:
    '''
    inner_html = ''
    if request.method == "GET":
        # 定义三个获取数据的方式
        # API接口 {
        # 仓库名称：storehouse_id
        # 搜索内容：search_content
        # }
        storehouse_id = request.GET.get('storehouse_id', None)
        search_content = request.GET.get('search_content', None)
        # 如果仓库名字不为空，
        logger.warning([storehouse_id, search_content])
        sql = '''select * from storehouse_manager where storehouse_id = %s'''
        storehouse_name = func_tools_sql_manager.search(sql, [storehouse_id])
        logger.warning(storehouse_name)
        storehouse_name = storehouse_name[0][1]
        logger.warning(storehouse_name)
        if storehouse_id != "" and storehouse_id != None:
            # 返回全局内容
            sql = '''select * from equipment_manager eq 
                                    WHERE equipment_classid = %s and not exists 
                                    (
                                    select * from equipment_manager 
                                    where equipment_id = eq.equipment_id and inside_id > eq.inside_id
                                    ) '''
            if search_content == None or search_content == "":
                logger.warning('if search_content == None or search_content == "":')
                # 搜索属于这个仓库的所有设备信息，到时候，在进行组合排序
                all_select_equipment_manager = func_tools_sql_manager.search(sql, [storehouse_id])
                if all_select_equipment_manager != ():
                    big_infomation_list = []
                    for i in all_select_equipment_manager:
                        infomation_list = eval(i[3])
                        infomation_list.insert(0, storehouse_name)
                        infomation_list.insert(0, i[1])
                        infomation_list.insert(0, i[0])
                        big_infomation_list.append(infomation_list)
                    for i in big_infomation_list:
                        temp_str = '''<tr>'''
                        for n, j in enumerate(i):
                            if n == 1:
                                equipment_id = j
                            temp_str += '<td>%s</td>' % (j)
                        temp_str += '''
                        <td><a href="/equipment_manager/equipment_manager_details/?equipment_id=%s&search_content=">
                        <span class="glyphicon glyphicon-eye-open" aria-hidden="true"></span></a></td>''' % (equipment_id)
                        temp_str += '''
                        <td><a onclick="return DELETE_ID('%s')">
                        <span class="glyphicon glyphicon-off" aria-hidden="true"></span></a></td>''' % (equipment_id)
                        temp_str += '''</tr>'''
                        inner_html += temp_str
                    logger.warning(inner_html)
                    return HttpResponse(inner_html)
            if search_content != None and search_content != "":
                logger.warning('if search_content != None and search_content != "":')
                # 搜索属于这个仓库的所有设备信息，到时候，在进行组合排序
                all_select_equipment_manager = func_tools_sql_manager.search(sql, [storehouse_id])
                search_content_hit_list = []
                if all_select_equipment_manager != ():
                    logger.warning(all_select_equipment_manager)
                    for i in all_select_equipment_manager:
                        '''
                            这时候的列表的数据格式是这样的[id,eq_id,eq_class,[1,1,1,,,,,,]]
                        '''
                        if str(search_content) in str(i[0]) or str(search_content) in str(i[1]) or search_content in str(i[2]):
                            search_content_hit_list.append(i)
                            continue
                        # 如果存入的时候为字符串，最好在这里进行eval一次
                        for j in eval(i[3]):
                            if search_content in str(j):
                                search_content_hit_list.append(i)
                                break
                    if search_content_hit_list != []:
                        logger.warning(['search_content_hit_list', search_content_hit_list])
                        big_infomation_list = []
                        logger.warning(["big_infomation_list", big_infomation_list])
                        for i in search_content_hit_list:
                            infomation_list = eval(i[3])
                            infomation_list.insert(0, storehouse_name)
                            infomation_list.insert(0, i[1])
                            infomation_list.insert(0, i[0])
                            big_infomation_list.append(infomation_list)
                        logger.warning(["big_infomation_list", big_infomation_list])
                        for i in big_infomation_list:
                            temp_str = '''<tr>'''
                            for n, j in enumerate(i):
                                if n == 1:
                                    equipment_id = j
                                temp_str += '<td>%s</td>' % (j)
                            temp_str += '''
                            <td><a href="/equipment_manager/equipment_manager_details/?equipment_id=%s&search_content=">
                            <span class="glyphicon glyphicon-eye-open" aria-hidden="true"></span></a></td>''' % (equipment_id)
                            temp_str += '''
                            <td><a onclick="return DELETE_ID('%s')">
                            <span class="glyphicon glyphicon-off" aria-hidden="true"></span></a></td>''' % (equipment_id)
                            temp_str += '''</tr>'''
                            inner_html += temp_str
                        logger.warning(["inner_html", inner_html])

                        return HttpResponse(inner_html)
    # 如果使用GET请求返回JSON的字符串
    return HttpResponse(inner_html)


def API_equipment_manager_details(request):
    '''
        展示目前存在在数据仓库
    :param request:
    :return:
    '''
    inner_html = ''
    if request.method == "GET":
        # 定义三个获取数据的方式
        # API接口 {
        # 仓库名称：storehouse_id
        # 搜索内容：search_content
        # }
        equipment_id = request.GET.get('equipment_id', None)
        search_content = request.GET.get('search_content', None)
        # 如果仓库名字不为空，
        logger.warning([equipment_id, search_content])
        if equipment_id != "" and equipment_id != None:
            # 返回全局内容
            sql = '''select * from equipment_manager where equipment_id = %s ORDER BY inside_id DESC'''
            if search_content == None or search_content == "":
                logger.warning('if search_content == None or search_content == "":')
                # 搜索属于这个仓库的所有设备信息，到时候，在进行组合排序
                all_select_equipment_manager = func_tools_sql_manager.search(sql, [equipment_id])
                if all_select_equipment_manager != ():
                    big_infomation_list = []
                    for i in all_select_equipment_manager:
                        infomation_list = eval(i[3])
                        infomation_list.insert(0, i[2])
                        infomation_list.insert(0, i[1])
                        infomation_list.insert(0, i[0])
                        big_infomation_list.append(infomation_list)
                    for i in big_infomation_list:
                        temp_str = '''<tr>'''
                        for n, j in enumerate(i):
                            if n == 1:
                                equipment_id = j
                            temp_str += '<td>%s</td>' % (j)
                        temp_str += '''</tr>'''
                        inner_html += temp_str
                    logger.warning(inner_html)
                    return HttpResponse(inner_html)
            if search_content != None and search_content != "":
                logger.warning('if search_content != None and search_content != "":')
                # 搜索属于这个仓库的所有设备信息，到时候，在进行组合排序
                all_select_equipment_manager = func_tools_sql_manager.search(sql, [equipment_id])
                search_content_hit_list = []
                if all_select_equipment_manager != ():
                    logger.warning(all_select_equipment_manager)
                    for i in all_select_equipment_manager:
                        '''
                            这时候的列表的数据格式是这样的[id,eq_id,eq_class,[1,1,1,,,,,,]]
                        '''
                        if str(search_content) in str(i[0]) or str(search_content) in str(i[1]) or search_content in str(i[2]):
                            search_content_hit_list.append(i)
                            continue
                        # 如果存入的时候为字符串，最好在这里进行eval一次
                        for j in eval(i[3]):
                            if search_content in str(j):
                                search_content_hit_list.append(i)
                                break
                    if search_content_hit_list != []:
                        logger.warning(['search_content_hit_list', search_content_hit_list])
                        big_infomation_list = []
                        logger.warning(["big_infomation_list", big_infomation_list])
                        for i in search_content_hit_list:
                            infomation_list = eval(i[3])
                            infomation_list.insert(0, i[2])
                            infomation_list.insert(0, i[1])
                            infomation_list.insert(0, i[0])
                            big_infomation_list.append(infomation_list)
                        logger.warning(["big_infomation_list", big_infomation_list])
                        for i in big_infomation_list:
                            temp_str = '''<tr>'''
                            for n, j in enumerate(i):
                                if n == 1:
                                    equipment_id = j
                                temp_str += '<td>%s</td>' % (j)
                            temp_str += '''</tr>'''
                            inner_html += temp_str
                        logger.warning(["inner_html", inner_html])
                        return HttpResponse(inner_html)
    # 如果使用GET请求返回JSON的字符串
    return HttpResponse(inner_html)


def API_equipment_manager_delete(request):
    '''

    :param request:
    :return:
    '''
    ret = {"status": "false", "mesg": "Null"}
    if request.method == "POST":
        try:
            equipment_id = request.POST.get('equipment_id',None)
            print(equipment_id)
            if equipment_id != None and equipment_id != "":
                sql = '''DELETE FROM equipment_manager WHERE equipment_id = %s '''
                delete_result = func_tools_sql_manager.excute(sql,[equipment_id])
                if delete_result == True:
                    ret["status"] = "true"
        except BaseException as e:
            print(e)

    return HttpResponse(json.dumps(ret))