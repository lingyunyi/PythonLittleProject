from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import uuid, time, os, random, datetime
import logging, hashlib, json,xlrd,xlwt

from unit_Tools.sqlData_unitTools import sqlData_unitTools

sqlData_unitToolsC = sqlData_unitTools()

def Info_exportExcel(request):
    '''
        主题展示 视图函数
    :param request:
    :return:
    '''
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    try:
        uuid4_str = request.COOKIES.get("username_id")
        user_nameQ = str(request.session.get(uuid4_str))
        user_name = hashlib.md5(str(user_nameQ).encode("utf-8")).hexdigest()
        if uuid4_str == None:
            print("-" * 100)
            return redirect('/')
    except BaseException as e:
        print("-" * 50, e)
        return redirect('/')

    if request.method == "GET":
        print("-" * 15, "ViewFunc Info_exportExcel - Get", "-" * 15)
        sql = '''select * from infomana where accountName = %s order by id desc limit 1000'''
        infoMalist = sqlData_unitToolsC.search(sql,[user_name],show=False)
        excelInsertValue = []
        if infoMalist:
            for i in infoMalist:
                excelInsertValueCell = []
                insert_Dict = json.loads(i[1])
                excelInsertValueCell.append(insert_Dict["title"])
                for i in insert_Dict.get("infoList",None):
                    excelInsertValueCell.append(i.get("content",None))
                excelInsertValue.append(excelInsertValueCell)
            path = "static/Excel/" + time.strftime("%m-%d-%H-%M-%S") +".xls"
            write_excel_xls(path,"one",excelInsertValue)

            file = open(path, 'rb')
            response = HttpResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="%s"'%(path.split("/")[-1])
            return response
        else:
            print("-" * 15, "数据库无值，不可导出数据。", "-" * 15)
            return redirect('/activity_show')
    elif request.method == "POST":
            pass




def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(j, i, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("-" * 15, "ViewFunc write_excel_xls - Get", "-" * 15)
