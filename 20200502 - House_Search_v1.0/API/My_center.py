from flask import Flask, render_template, request, make_response, session, Response, Blueprint, redirect
import os, random, hashlib, uuid, json
from tools.sql_manager import SqlManger

sqL_Manager_tool = SqlManger()

my_center = Blueprint("my_center", __name__)


@my_center.route("/my_center/users_infomation/", methods=["GET", "POST"])
def users_infomation():
    if request.method == "GET":
        users_id = request.cookies.get("users_id")
        session_users_name = session.get(users_id, None)
        print({request.cookies.values()}, {users_id}, {session_users_name}, {session.values()})
        if session_users_name == None:
            return redirect("/login")
        else:
            sql = '''select * from users_infomation_json where users_name = %s'''
            search_users_infomation_json_result = sqL_Manager_tool.search(sql, [session_users_name])
            users_show_infomation_json = {
                "users_name": 'None',
                "users_phone": 'None',
                "users_city": 'None',
                "users_email": 'None',
            }
            if search_users_infomation_json_result != ():
                users_infomation_json = search_users_infomation_json_result[0][2]
                users_show_infomation_json = json.loads(users_infomation_json)
            return render_template("My_center/users_infomation.html", session_users_name=session_users_name,user_info=users_show_infomation_json)
    elif request.method == "POST":
        pass


@my_center.route("/my_center/users_orders/", methods=["GET", "POST"])
def users_orders():
    if request.method == "GET":
        users_id = request.cookies.get("users_id")
        session_users_name = session.get(users_id, None)
        print({request.cookies.values()}, {users_id}, {session_users_name}, {session.values()})
        if session_users_name == None:
            return redirect("/login")
        else:
            sql = '''select * from house_infomation where users = %s'''
            search_house_infomation_houser_result = sqL_Manager_tool.search(sql, [session_users_name])
            if search_house_infomation_houser_result == ():
                search_house_infomation_houser_result = None
            return render_template("My_center/users_orders.html", session_users_name=session_users_name, my_house=search_house_infomation_houser_result)
    elif request.method == "POST":
        pass




@my_center.route("/my_center/users_change_infomation/", methods=["GET", "POST"])
def users_change_infomation():
    if request.method == "GET":
        users_id = request.cookies.get("users_id")
        session_users_name = session.get(users_id, None)
        print({request.cookies.values()}, {users_id}, {session_users_name}, {session.values()})
        if session_users_name == None:
            return redirect("/login")
        else:
            return render_template("My_center/users_change_infomation.html", session_users_name=session_users_name)
    elif request.method == "POST":
        ret = {"status": "false", "meg": "null"}
        session_users_name = request.form.get("session_users_name")
        ajax_users_name = request.form.get("users_name")
        ajax_users_phone = request.form.get("users_phone")
        ajax_users_city = request.form.get("users_city")
        ajax_users_email = request.form.get("users_email")
        # 这里查询数据是否已经出现过记录
        sql = '''select * from users_infomation_json where users_name = %s'''
        print({session_users_name}, {ajax_users_name}, {ajax_users_phone}, {ajax_users_city}, {ajax_users_email})
        search_users_infomation_json_result = sqL_Manager_tool.search(sql, [session_users_name])
        wait_user_infomation_json = json.dumps({
            "users_name": ajax_users_name,
            "users_phone": ajax_users_phone,
            "users_city": ajax_users_city,
            "users_email": ajax_users_email,
        },ensure_ascii=False)
        if ajax_users_name == "" or ajax_users_phone == "" or ajax_users_city == "" or ajax_users_email == "":
            return json.dumps(ret)
        if search_users_infomation_json_result == ():
            # 代表没有数据，所以给他插入数据
            sql = '''insert into users_infomation_json(users_name,users_infomation_json) value (%s,%s)'''
            insert_user_infomation_json_result = sqL_Manager_tool.excute(sql, [session_users_name, wait_user_infomation_json])
            if insert_user_infomation_json_result == True:
                ret["status"] = "true"
                return json.dumps(ret)
            elif insert_user_infomation_json_result == False:
                return json.dumps(ret)
        elif search_users_infomation_json_result != ():
            # 这里代表有数据更新数据即可
            sql = '''UPDATE users_infomation_json SET users_infomation_json = %s WHERE users_name = %s '''
            updata_users_infomation_json_result = sqL_Manager_tool.excute(sql,[wait_user_infomation_json,session_users_name])
            if updata_users_infomation_json_result == True:
                ret["status"] = "true"
                return json.dumps(ret)
            elif updata_users_infomation_json_result == False:
                return json.dumps(ret)

