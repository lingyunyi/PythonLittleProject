import pymysql
import xlrd, xlwt,random


class SqlManger(object):

    def __init__(self):
        '''
            暂无初始化内容
        '''
        pass

    def connect(self):
        '''
            # connent(参数列表[“IP地址”，“数据库账号”， “数据库密码”， “数据库名称”])
        :return:
        '''
        self.db = pymysql.connect("127.0.0.1", "root", "root", "test")
        # 使用cursor游标，创建一个游标对象cursor
        self.cursor = self.db.cursor()
        return True

    def close(self):
        '''
        # connent(参数列表[“IP地址”，“数据库账号”， “数据库密码”， “数据库名称”])
        :return:
        '''
        self.cursor.close()
        # 数据库关闭
        self.db.close()
        return True

    def search(self, sql, args=None, show=True):
        try:
            # 连接服务器
            self.connect()
            # 执行SQL语句
            if show != False:
                print(sql, args)
            # sql语句需要接占位符,由于不使用dict传参数,所以只需要%s 用[]或者()传递参数即可.如果需要使用dict 占位符这需要,%(key)s为占位符.
            self.cursor.execute(sql, args)
            # 获取数据库中的表单
            results = self.cursor.fetchall()
            self.close()
            # 直接返回查询结果，返回的结果是一个元祖
            return results
        except:
            # 如果发生错误则回滚
            self.close()
            return False

    def excutemany(self, sql, args=None, show=True):
        try:
            # 连接数据库
            self.connect()
            # 执行sql语句
            if show != False:
                print(sql, args)
            self.cursor.executemany(sql, args)
            # 提交到数据库执行
            self.db.commit()
            # 关闭数据库
            self.close()
            return True
        except:
            self.db.rollback()
            return False

    def excute(self, sql, args=None, show=True):
        try:
            # 连接数据库
            self.connect()
            # 执行sql语句
            if show != False:
                print(sql, args)
            self.cursor.execute(sql,args)
            # 提交到数据库执行
            self.db.commit()
            # 关闭数据库
            self.close()
            return True
        except:
            self.db.rollback()
            return False

    def is_can(self):
        '''
            当别调用时，查看是否可以用
        '''
        print("this （{}）moddle is ok!!!".format(self.__class__))
        return True


class Mysql_and_excel(object):

    def __init__(self):
        self.sql_Manager_TOOS = SqlManger()

    def readme_excel(self, excel_path=None):
        '''
            读取传入的excel文件内容
        :param excel_path:
        :return:
        '''
        response_big_list = None
        if excel_path != None and (str(excel_path).split("."))[-1] in ["xls", "xlsx"]:
            book = xlrd.open_workbook(excel_path)
            table = book.sheet_by_index(0)
            nrows = table.nrows
            response_big_list = []
            for i in range(1, nrows):
                try:
                    cell_row_value = table.row_values(i)
                    print(cell_row_value)
                    response_big_list.append(cell_row_value)
                except BaseException as e:
                    print(e)
                    continue
        return response_big_list

    def excel_to_sql(self, table=None, excel_path=None):
        '''
            将获取到的大列表数据插入到数据库中。
        :param table:
        :param excel_path:
        :return:
        '''
        ret = {"status": "false"}
        if excel_path != None and table != None:
            response_big_list = self.readme_excel(excel_path)
            if response_big_list != None:
                sql = '''truncate table {}'''.format(table)
                truncate_table = self.sql_Manager_TOOS.excute(sql,[])
                if truncate_table == True:
                    sql = '''insert into {}(student_name,student_id,student_email,student_gpa,student_passwd) value (%s,%s,%s,%s,%s)'''.format(table)
                    # 这里强调一些，因为使用的是excutemany，所以传入的数据只能是大列表类型，就是一个列表，其中包含很多小列表
                    for i in response_big_list:
                        # random_ID = int(random.uniform(1, 10) * 1000000000)
                        # id_and_email = "%s%s" % (random_ID, "@mail.uic.edu.h")
                        # init_passwd = "000000"
                        sql_insert_many_list_result = self.sql_Manager_TOOS.excute(sql, [i[0],i[1],i[2],i[3],None])
                    if sql_insert_many_list_result == True:
                        ret["status"] == "true"
                        return
        return ret

    def sql_to_excel(self, table=None, excel_path=None):
        '''
            sql_to_excel
        :param table:
        :param excel_path:
        :return:
        '''
        ret = {"status": "false"}
        try:
            if excel_path == None and (str(excel_path).split("."))[-1] not in ["xls", "xlsx"]:
                print(ret)
                return ret
            if excel_path != None and table != None:
                print("if excel_path != None and table != None:", ret)
                sql = '''select student_name,student_id,student_email,student_gpa from {}'''.format(table)
                select_from_select_tables_list = self.sql_Manager_TOOS.search(sql, [])
                if select_from_select_tables_list != ():
                    print("if select_from_select_tables_list != ():", ret)
                    book = xlwt.Workbook(encoding='utf-8')
                    table = book.add_sheet('1')
                    # table.write(0, 0, "student_name")
                    # table.write(0, 1, "student_id")
                    # table.write(0, 2, 'student_email')
                    # table.write(0, 3, 'student_gpa')
                    for i in range(len(select_from_select_tables_list)):
                        try:
                            table.write(i, 0, select_from_select_tables_list[i][0])
                            table.write(i, 1, select_from_select_tables_list[i][1])
                            table.write(i, 2, select_from_select_tables_list[i][2])
                            table.write(i, 3, select_from_select_tables_list[i][3])
                        except:
                            continue
                ret["status"] = "true"
                book.save(excel_path)
        except:
            return ret
        return ret


    def auto_create_infomation(self,table=None,count=1):
        '''

        :param one:
        :param two:
        :return:
        '''
        print(count)
        for i in range(0,int(count)):
            print(i)
            if table != None:
                random_ID = int(random.uniform(1, 10)*1000000000)
                id_and_email = "%s%s"%(random_ID,"@mail.uic.edu.h")
                init_passwd = "000000"
                sql = '''select count(*) from {}'''.format(table)
                select_count = self.sql_Manager_TOOS.search(sql,[])
                print(select_count)
                student_name = "student%s"%(int(select_count[0][0])+1)
                sql = '''insert into {}(student_name,student_id,student_email,student_gpa,student_passwd) value (%s,%s,%s,%s,%s)'''.format(table)
                insert_into_users_result = self.sql_Manager_TOOS.excute(sql,[student_name,random_ID,id_and_email,None,init_passwd])
        return False




if __name__ == "__main__":
    Q = Mysql_and_excel()
    Q.excel_to_sql(table="student_one",excel_path="123.xlsx")

    # Q.sql_to_excel(table="student_one", excel_path="two3.xls")

    # table是表明，count是生成次数，默认是1次。
    # Q.auto_create_infomation(table="student_one",count=100)




    # while True:
    #     num = random.randint

    '''
    DROP TABLE IF EXISTS `数据库名`;
    CREATE TABLE `数据库名` (
      `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `student_name` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
      `student_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
      `student_email` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
      `student_gpa` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
      `student_passwd` varchar(255) DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=MyISAM AUTO_INCREMENT=92 DEFAULT CHARSET=utf8;

    '''