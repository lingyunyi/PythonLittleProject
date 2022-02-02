# 数据库配置
HOST_IP = "127.0.0.1"
USER_NAME = "root"
USER_PASSWD = "root"
USE_DATABASE = "newsmodel_college"
# SQL命令备用
'''
    Truncate Table accounttables
    select * from account where username = %s and passwd = %s
    insert into AccountTables values (%s,%s,%s,%s,%s,%s)
    UPDATE infomana SET infoCol = %s WHERE id = %s and accountName = %s
    select * from infomana where accountName = %s order by id desc limit 1000
'''
#通用Django渲染内容
#user_iphone已经在登入成功函数中传入
AD_ShowContent = "（OpqO 广告位 OpqO）"
Back_Common_Render = {"AD_Show":AD_ShowContent,"user_iphone":""}
Front_Common_Render = {}