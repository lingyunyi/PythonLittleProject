from flask import Flask, render_template, request,make_response,session,Response
import os,random,hashlib,uuid,json

from tools.sql_manager import SqlManger

from API.Public_api import public_api
from API.Houser_center import houser_center
from API.My_center import my_center
from API.Index_show import index_show

app = Flask(__name__)
app.register_blueprint(public_api)
app.register_blueprint(houser_center)
app.register_blueprint(my_center)
app.register_blueprint(index_show)

app.config['SECRET_KEY'] = os.urandom(24)

sqL_Manager_tool = SqlManger()



@app.route("/login/", methods=["GET","POST"])
def login_register():
    if request.method == "GET":
        return render_template('all_login.html', )
    if request.method == "POST":
        # 首先先判断请求的类型是什么
        ret = {"status":"false","meg":"null"}
        if request.form.get("func_type") == "login":
            ajax_input_account = request.form.get("users_account")
            ajax_input_password = request.form.get("users_passwd")
            print([{request.host},{request.method},{ajax_input_account},{ajax_input_password},{request.form.get("func_type")}])
            # 从数据库中取数据
            sql = '''select * from users_account where users_account = %s'''
            search_users_tables = sqL_Manager_tool.search(sql,[ajax_input_account])
            # 查看是否能搜索到数据如果没有数据的话就报错。
            if search_users_tables == ():
                # 直接返回结果
                print('search_users_tables == ():',[{search_users_tables}])
                return json.dumps(ret)
            elif search_users_tables != ():
                # 判断账号是否相等
                print('search_users_tables != ():', [{search_users_tables}])
                print([{search_users_tables[0][1]},{ajax_input_account},{search_users_tables[0][2]},{hashlib.md5(ajax_input_password.encode(encoding='UTF-8')).hexdigest()}])
                if search_users_tables[0][1] == ajax_input_account and search_users_tables[0][2] == hashlib.md5(ajax_input_password.encode(encoding='UTF-8')).hexdigest():
                    # 对状态进行赋值
                    ret["status"] = "true"
                    random_str = str(uuid.uuid4())
                    obj = Response(json.dumps(ret))
                    obj.set_cookie("users_id",random_str)
                    # 对全局session配置随机函数
                    session[random_str] = ajax_input_account
                    print({session.get(random_str)})
                    return obj
                else:
                    return json.dumps(ret)
        elif request.form.get("func_type") == "register":
            ajax_input_account = request.form.get("users_account")
            ajax_input_password = request.form.get("users_passwd")
            print([{request.host}, {request.method}, {ajax_input_account}, {ajax_input_password},{request.form.get("func_type")}])
            # 可以开始执行注册
            sql = '''insert into users_account(users_account,users_password) value (%s,%s)'''
            md5_password = hashlib.md5(ajax_input_password.encode(encoding='UTF-8')).hexdigest()
            register_users_account_result = sqL_Manager_tool.excute(sql,[ajax_input_account,md5_password])
            if register_users_account_result == True:
                ret["status"] = "true"
                return json.dumps(ret)
            elif register_users_account_result == False:
                return json.dumps(ret)


if __name__ == '__main__':
    app.run(debug=True)
