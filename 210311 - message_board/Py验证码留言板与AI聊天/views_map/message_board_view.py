from ..tools_map import mysql_manager
from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import uuid, time, os, random
import logging, hashlib, json
from tools_API.find_IP_location import IP_location

tool_mysql = mysql_manager.SqlManger()


# uuid4_str = str(uuid.uuid4())
# request.session[uuid4_str] = users_account
# obj = HttpResponse("200")
# obj.set_cookie("username_id", uuid4_str, 60 * 60 * 24)


def ms_show_index(request):
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    sql = '''select * from message_board'''
    board_list_dict = []
    tool_select_result = tool_mysql.search(sql,show=False)
    if tool_select_result != ():
        # 对元祖进行抽取，和逆排序
        board_dict_values = [i[1] for i in tool_select_result]
        for i in board_dict_values:
            # 将i 反序列化回来
            i = json.loads(i)
            i["color"] = random.choice(["success", "info", "warning", "danger"])
            board_list_dict.append(i)
        board_list_dict = sorted(board_list_dict, key=lambda x : x["times"], reverse=True)
    return render(request, "../templates/html_message_board/index_message_board.html", {"board_list_dict": board_list_dict[0:51]})


def ms_push_content(request):
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    if request.method == "GET":
        return render(request, "../templates/html_message_board/push_message_content.html", {})
    elif request.method == "POST":
        # 如果携带cookies将不急于发布
        try:
            if request.POST.get("check_code") != "lingyunyi00":
                return HttpResponse(json.dumps({"result": "False", "tip": "Check_code false"}))

            uuid4_str = str(uuid.uuid4())
            # 返回设置cookies的响应
            obj = HttpResponse(json.dumps({"result": "True"}))
            obj.set_cookie("random_cookies", uuid4_str, 60 * 30)
            # 如果不携带cookies发布后将设置cookies
            if not request.COOKIES.get('random_cookies'):
                insert_data_json = json.dumps({
                    "ip": ip,
                    "location":IP_location(ip),
                    "board_content": request.POST.get("board_content"),
                    "times": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime((time.time()))),
                })
                sql = '''insert into message_board (dict_values) values (%s)'''
                excute_zero = tool_mysql.excute(sql, [insert_data_json], show=True)
                if excute_zero == True:
                    return obj
                else:
                    return HttpResponse(json.dumps({"result": "False", "tip": "insert false"}))
            # 如果携带cookies发布后将设置cookies
            else:
                return HttpResponse(json.dumps({"result": "Wait"}))
        except BaseException as error:
            # 返回设置cookies的响应
            return HttpResponse(json.dumps({"result": "False", "tip": "Except false"}))
