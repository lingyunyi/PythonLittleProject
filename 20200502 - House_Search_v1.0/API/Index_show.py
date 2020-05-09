from flask import Flask, render_template, request, make_response, session, Response, Blueprint, redirect
import os, random, hashlib, uuid, json
from tools.sql_manager import SqlManger

sqL_Manager_tool = SqlManger()

index_show = Blueprint("index_show", __name__)

@index_show.route("/", methods=["GET", "POST"])
def index_show_house():
    users_id = request.cookies.get("users_id")
    session_users_name = session.get(users_id, None)
    if request.method == "GET":
        search = request.form.get("search")
        house_infos_list = None
        sql = '''select * from house_infomation'''
        house_infos = sqL_Manager_tool.search(sql, [])
        if search == "" or search == None:
            if house_infos != ():
                house_infos_list = []
                for i in house_infos:
                    print({search},{"else"},{i[6]}, {i[7]})
                    if i[6] != "预订":
                        house_infos_list.append(i)
        else:
            if house_infos != ():
                house_infos_list = []
                for i in house_infos:
                    print({search},{"else"},{i[6]}, {i[7]})
                    if search in i[2] or search in i[3] or i[6] != "预订":
                        house_infos_list.append(i)
        print(house_infos_list)
        return render_template("Index_show/index_show.html", house_infos=house_infos_list)
    elif request.method == "POST":
        search = request.form.get("search")
        house_infos_list = None
        sql = '''select * from house_infomation'''
        house_infos = sqL_Manager_tool.search(sql, [])
        if search == "" or search == None:
            print("if search == "" or search == None:")
            if house_infos != ():
                house_infos_list = []
                for i in house_infos:
                    print({i[6]},{i[7]})
                    if i[6] != "预订":
                        house_infos_list.append(i)
        else:
            print("if search != "" or search != None:")
            if house_infos != ():
                house_infos_list = []
                for i in house_infos:
                    print({i[6]}, {i[7]})
                    if search in i[2] or search in i[3] and i[6] != "预订":
                        house_infos_list.append(i)
        print({search},house_infos_list)
        return render_template("Index_show/index_show.html", house_infos=house_infos_list)





@index_show.route("/house_show_detail/", methods=["GET", "POST"])
def house_show_detail():
    users_id = request.cookies.get("users_id")
    session_users_name = session.get(users_id, None)
    if session_users_name == None:
        return redirect("/login/")
    if request.method == "GET":
        nid = request.args.get("nid")
        if nid == None or nid == "":
            nid = 0
        sql = '''select * from house_infomation where id = %s'''
        house_infos_list = sqL_Manager_tool.search(sql,[nid])
        if house_infos_list != ():
            house_infos_listX = house_infos_list[0]
        else:
            house_infos_listX = None
        return render_template("Index_show/house_show_detail.html", house_infos=house_infos_listX,session_users_name=session_users_name)


@index_show.route("/house_show_detail/book/", methods=["GET", "POST"])
def house_show_detail_book():
    ret = {"status": "false", "meg": "null"}
    users_id = request.cookies.get("users_id")
    session_users_name = session.get(users_id, None)
    if session_users_name == None:
        return redirect("/login/")
    if request.method == "GET":
        return redirect("/login/")
    if request.method == "POST":
        nid = request.args.get("nid")
        sql = '''UPDATE house_infomation SET users = %s,house_status = %s WHERE id = %s '''
        updata_house_infomation_users = sqL_Manager_tool.excute(sql,[session_users_name,"预订",nid])
        if updata_house_infomation_users == True:
            ret["status"] = "true"
            return json.dumps(ret)
    return json.dumps(ret)