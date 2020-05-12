from flask import Blueprint, render_template, request, session, redirect, url_for,jsonify
from app.models.base import db
from app.models.course import Course
from app.models.student import Student
from app.tools.sql_manager import SqlManger
import json


oo_files_saveBP = Blueprint('Oo_files_save',__name__)


oo_sql_manager_tools = SqlManger()

@oo_files_saveBP.route('/save_files', methods=['GET'])
def save_files():
    sql = '''select * from files_temp'''
    select_files_save = oo_sql_manager_tools.search(sql,[])
    print(select_files_save)
    return render_template("flies_save.html",select_files_save=select_files_save)




@oo_files_saveBP.route('/upload_files', methods=['GET'])
def upload_files():
    return render_template("files_upload.html")




ALLOWED_EXTENSIONS = set(['txt', 'xlsx', 'xls'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@oo_files_saveBP.route('/API/insert_into', methods=['POST'])
def AJAX_insert_into_one_infomation():
    ret = {"status":"false","mesg":"null","num":"0"}
    print(jsonify(ret))
    if request.method == "POST":
        try:
            print("re",request.form.items,request.files.items)
            file_tilte = request.form.get("file_tilte",None)
            file_ratio = request.form.get("file_ratio",None)
            print(request.form.get("file_ratio",None))
            file_content = request.files["file_content"]
            print(file_content)
            path = "app/static/upload/"
            file_content_name = file_content.filename
            if file_tilte == None or file_tilte == "" or file_ratio == None or file_ratio == "" or file_content == None or file_content == "":
                ret["num"] = 1
                return json.dumps(ret)
            if (allowed_file(file_content_name)) == False:
                ret["num"] = 2
                return json.dumps(ret)
            file_path_temp = path + file_content_name
            # 保存图片
            file_content.save(file_path_temp)
            sql = '''insert into files_temp(file_title,file_ratio,file_path) value (%s,%s,%s)'''
            insert_file_path = oo_sql_manager_tools.excute(sql,[file_tilte,file_ratio,file_path_temp])
            if insert_file_path == True:
                ret["status"] = "true"
                ret["num"] = 3
                return json.dumps(ret)
        except BaseException as e:
            print("s",e)
    ret["num"] = 4
    return json.dumps(ret)


@oo_files_saveBP.route('/API/del_into', methods=['POST'])
def AJAX_delete_into_one_infomation():
    ret = {"status":"false","mesg":"null","num":"0"}
    print(jsonify(ret))
    if request.method == "POST":
        try:
            nid = request.form.get("nid",None)
            if nid == None or nid == "" :
                ret["num"] = 1
                return json.dumps(ret)
            sql = '''DELETE FROM files_temp WHERE id = %s'''
            del_files_temp = oo_sql_manager_tools.excute(sql,[nid])
            if del_files_temp == True:
                ret["status"] = "true"
                ret["num"] = 3
                return json.dumps(ret)
        except BaseException as e:
            print("s",e)
    ret["num"] = 4
    return json.dumps(ret)

@oo_files_saveBP.route('/API/save_files', methods=['POST'])
def API_save_files():
    ret = {"status":"false","mesg":"null","num":"0"}
    if request.method == "POST":
        try:
            typex = request.form.get("typex",None)
            print(typex)
            if typex != None or typex != "":
                if typex == "insert":
                    sql = '''select * from files_temp'''
                    select_files_save = oo_sql_manager_tools.search(sql, [])
                    if select_files_save != ():
                        save_files_list = []
                        for i in select_files_save:
                            save_files_list.append([i[1],i[2],i[3]])
                        sql = '''insert into files_save(file_title,file_ratio,file_path) value (%s,%s,%s)'''
                        insert_into_files_save = oo_sql_manager_tools.excutemany(sql,save_files_list)
                        if insert_into_files_save == True:
                            ret["status"] = "true"
                            ret["num"] = 3
                            sql = '''truncate table files_temp'''
                            truncate_table = oo_sql_manager_tools.excute(sql, [])
                            return json.dumps(ret)
            sql = '''truncate table files_temp'''
            truncate_table = oo_sql_manager_tools.excute(sql,[])
        except BaseException as e:
            sql = '''truncate table files_temp'''
            truncate_table = oo_sql_manager_tools.excute(sql, [])
            print("s",e)
    ret["num"] = 4
    return json.dumps(ret)