from django.http import request
from django.shortcuts import redirect,render,HttpResponse,Http404
import threading,requests
import uuid,time,os,json

from qr_code_create import settings
from tools.sql_manager import  SqlManger
import logging,hashlib

import qrcode

sql_manager_tools = SqlManger()

def index(request):
    '''
    :param request:
    :return:
    '''
    # 如果是GET请求直接返回页面
    if request.method == "GET":
        return render(request,'index.html',{
            "session_users_name":"loging"
        })
    #其余请求返回404
    return HttpResponse(404)

def create_qrcode(request,ip="192.168.0.103"):
    '''

    :param request:
    :return:
    '''

    ret = {"status":"false","mesg":"null","qrcode_url":""}

    if request.method == "POST":
        # 获取所有post请求的数据
        school_content = request.POST.get("school_content",None)
        class_content = request.POST.get("class_content", None)
        iphone_content = request.POST.get("iphone_content", None)
        name_content = request.POST.get("name_content", None)
        apartment_content = request.POST.get("apartment_content", None)
        sex_content = request.POST.get("sex_content", None)
        #判断其是否为空
        if school_content != "" and class_content != "":
            if iphone_content != "" and name_content != "":
                if apartment_content != "" and sex_content != "":
                    sql = '''SELECT max(id) from school_apartment'''
                    count = sql_manager_tools.search(sql,[])
                    if count[0][0] == None:
                        count_num = 0
                    else:
                        count_num = int(count[0][0])+1
                    print(count)
                    img_infomation = 'http:/%s/show_my_info/?nid=%s'%(ip,count_num)
                    # 生成伪随机随机字符串
                    try:
                        str_uuid = str(uuid.uuid4())
                        img_file = r'static/qrcode_img/{}.png'.format(str_uuid)
                        # 实例化QRCode生成qr对象
                        qr = qrcode.QRCode(
                            version=1,
                            error_correction=qrcode.constants.ERROR_CORRECT_H,
                            box_size=10,
                            border=4
                        )
                        # 传入数据
                        qr.add_data(img_infomation)
                        qr.make(fit=True)
                        # 生成二维码
                        img = qr.make_image()
                        # 保存二维码
                        print("img.save(img_file)")
                        img.save(img_file)
                        # 传入数据库插入语句
                        sql = '''insert into school_apartment(id,name_content,
                        sex_content,
                        school_content,
                        class_content,
                        iphone_content,
                        apartment_content,
                        qrcode_img,is_del) value (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                        # 插入数据库
                        insert_school_apartment = sql_manager_tools.excute(sql,[
                            count_num,
                            name_content,sex_content,
                            school_content,class_content,
                            iphone_content,apartment_content,
                            img_file.strip(".."),0])
                        if insert_school_apartment == True:
                            ret["status"] = "true"
                            ret["qrcode_url"] = img_file.strip("..")
                            return HttpResponse(json.dumps(ret))
                    except BaseException as e:
                        print("验证码生成异常:",e)
    return HttpResponse(json.dumps(ret))


def infomation_db(request):
    '''

    :param request:
    :return:
    '''
    if request.method == "GET":
        sql = '''select * from school_apartment where is_del = 0'''

        db_list = sql_manager_tools.search(sql,[])

        return render(request,"infomation_db.html",{
            "db_list":db_list
        })
    return  HttpResponse(404)
