from flask import Flask, render_template, request,make_response,session,Response,Blueprint,redirect
import os,random,hashlib,uuid,json

public_api = Blueprint("public_api",__name__)


@public_api.route('/public_api/get_captcha/', methods=['GET'])
def get_captcha():
    img_list = os.listdir("./static/Public/img/temp")
    img = img_list[random.randint(0, 100)]
    return os.path.join("/static/Public/img/temp", img)


@public_api.route('/public_api/logout/', methods=['GET'])
def logout():
    ret = {"status":"success","meg":"null"}
    if request.method == "GET":
        users_id = request.cookies.get("users_id")
        session[users_id] = None
        return redirect("/login/")


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@public_api.route('/public_api/upload_img/', methods=['GET',"POST"])
def upload_img():
    ret = {"status":"true","img_src":"null"}
    if request.method == "POST":
        # 通过表单中name值获取图片
        imgData = request.files["uploadImg"]
        print({imgData},{request.form.get("uploadImg")})
        # 设置图片要保存到的路径
        path = "static/House_img/"
        # 获取图片名称及后缀名
        imgName = imgData.filename
        # 图片path和名称组成图片的保存路径
        if(allowed_file(imgName)) == False:
            ret["status"] = "false"
            return json.dumps(ret)
        file_path = path + imgName
        # 保存图片
        imgData.save(file_path)
        # url是图片的路径
        img_src = "/static/House_img/" + imgName
        ret["img_src"] = img_src
        return json.dumps(ret)


