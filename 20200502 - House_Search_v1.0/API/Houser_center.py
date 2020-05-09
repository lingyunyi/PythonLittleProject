from flask import Flask, render_template, request,make_response,session,Response,Blueprint,redirect
import os,random,hashlib,uuid,json
from tools.sql_manager import SqlManger

sqL_Manager_tool = SqlManger()
houser_center = Blueprint("houser_center",__name__)





@houser_center.route("/houser_center/houser_infomation/", methods=["GET", "POST"])
def houser_infomation():
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
            return render_template("Houser_center/hosuer_infomation.html", session_users_name=session_users_name,user_info=users_show_infomation_json)
    elif request.method == "POST":
        pass

@houser_center.route("/houser_center/houser_change_infomation/", methods=["GET", "POST"])
def houser_change_infomation():
    if request.method == "GET":
        users_id = request.cookies.get("users_id")
        session_users_name = session.get(users_id, None)
        print({request.cookies.values()}, {users_id}, {session_users_name}, {session.values()})
        if session_users_name == None:
            return redirect("/login")
        else:
            return render_template("Houser_center/houser_change_infomation.html", session_users_name=session_users_name)
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


@houser_center.route("/houser_center/houser_my_house/", methods=["GET", "POST"])
def houser_my_house():
    if request.method == "GET":
        users_id = request.cookies.get("users_id")
        session_users_name = session.get(users_id, None)
        print({request.cookies.values()}, {users_id}, {session_users_name}, {session.values()})
        if session_users_name == None:
            return redirect("/login")
        else:
            sql = '''select * from house_infomation where houser = %s'''
            search_house_infomation_houser_result = sqL_Manager_tool.search(sql,[session_users_name])
            if search_house_infomation_houser_result == ():
                search_house_infomation_houser_result = None
            return render_template("Houser_center/hosuer_my_house.html", session_users_name=session_users_name,my_house=search_house_infomation_houser_result)
    elif request.method == "POST":
        pass

@houser_center.route("/houser_center/hosuer_add_one_house/", methods=["GET", "POST"])
def hosuer_add_one_house():
    if request.method == "GET":
        users_id = request.cookies.get("users_id")
        session_users_name = session.get(users_id, None)
        print({request.cookies.values()}, {users_id}, {session_users_name}, {session.values()})
        if session_users_name == None:
            return redirect("/login")
        else:
            return render_template("Houser_center/hosuer_add_one_house.html", session_users_name=session_users_name)
    elif request.method == "POST":
        ret = {"status": "false", "meg": "null"}
        users_id = request.cookies.get("users_id")
        session_users_name = session.get(users_id, None)
        if session_users_name != None:
            house_title = request.form.get("house_title")
            house_village = request.form.get("house_village")
            house_address = request.form.get("house_address")
            house_price = request.form.get("house_price")
            house_describe = request.form.get("house_describe")
            house_status = "待预订"
            house_show_img = request.form.get("house_show_img")
            print({house_title},{house_village},{house_address},{house_price},{house_describe},{house_status},{house_show_img},{session_users_name},{},{})
            if house_title != None:
                if house_village != None:
                    if house_address != None:
                        if house_price != None:
                            if house_describe != None:
                                if house_show_img != None:
                                    sql = '''insert into house_infomation(house_title,house_village,house_address,house_price,house_describe,house_status,house_show_img,houser,users,response) 
                                    value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                                    insert_house_infomation_rusult = sqL_Manager_tool.excute(sql,[house_title,house_village,house_address,house_price,house_describe,house_status,house_show_img,session_users_name,None,None])
                                    if insert_house_infomation_rusult == True:
                                        ret["status"] = "true"
                                        return json.dumps(ret)
        return json.dumps(ret)



@houser_center.route("/houser_center/change_response/", methods=["GET", "POST"])
def change_response():
    if request.method == "GET":
        return redirect("/login/")
    elif request.method == "POST":
        ret = {"status": "false", "meg": "null"}
        users_id = request.cookies.get("users_id")
        session_users_name = session.get(users_id, None)
        if session_users_name != None:
            res = request.form.get("res")
            nid = request.form.get("nid")
            if res != None and nid != None:
                sql = '''UPDATE house_infomation SET response = %s WHERE id = %s '''
                updata_house_infomation_response_result = sqL_Manager_tool.excute(sql,[res,nid])
                if updata_house_infomation_response_result == True:
                    ret["status"] = "true"
                    return json.dumps(ret)
        return json.dumps(ret)
