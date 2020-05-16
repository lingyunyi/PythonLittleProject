from func_tools.sql_manager import SqlManger

func_tools_sql_manager = SqlManger()

import xlrd, xlwt, random
import uuid
import os,json

os.sys.path.append(".")
'''
首先先来捋一捋思路。
写两个接口，

第一个接口，首先是导出数据库。
那么就得先从数据库取内容，然后批量写入EXCEL文件中，最后返回一个文字地址，在让前端渲染，然后下载。

第二个接口，则是，后端先接受前端传来的excel文件，并保存在某个目录中，给其重命名。将这个文件，跳转到这里。

这个接口则是需要两个值，第一个值，是仓库ID，第二个值是文件地址，

然后这个接口就读取该文件，写入数据库中。

'''


class Sql_2to2_Excel(object):

    def __init__(self):
        pass

    def return_storehouse_to_excel(self):
        '''

        :return:
        '''
        # 搜索数据库内容
        sql = '''select * from equipment_manager'''
        all_select_equipment_manager = func_tools_sql_manager.search(sql, [])
        # 得到所有数据内容
        if all_select_equipment_manager != ():
            big_infomation_list = []
            for i in all_select_equipment_manager:
                infomation_list = eval(i[3])
                infomation_list.insert(0, i[2])
                infomation_list.insert(0, i[1])
                infomation_list.insert(0, i[0])
                big_infomation_list.append(infomation_list)
        if all_select_equipment_manager == ():
            return False
        # 这时候得到的数据已经是拼接好的大数据。
        print(big_infomation_list)
        str_uuid = str(uuid.uuid4())
        excel_path = r'static\output_excel/%s.xls' % (str_uuid)
        try:
            if excel_path == None and (str(excel_path).split("."))[-1] not in ["xls", "xlsx"]:
                return False
            if excel_path != None:
                book = xlwt.Workbook(encoding='utf-8')
                table = book.add_sheet('1')
                for i in range(len(big_infomation_list)):
                    try:
                        for j in range(len(big_infomation_list[i])):
                            print(i, j, big_infomation_list[i][j])
                            table.write(i, j, big_infomation_list[i][j])
                    except BaseException as e:
                        print(e)
                        continue
            print("book.save(excel_path)")
            book.save(excel_path)
        except BaseException as e:
            print(e)
            return False
        excel_path = excel_path.split("\\")
        print(excel_path)
        return excel_path[-1]

    def get_input_excel_to_sql(self, storehouse_id, excel_path):
        '''

        :param storehouse_id:
        :param excel_path:
        :return:
        '''
        if storehouse_id != None and excel_path != None:
            # 首先先批量读取excel内容
            response_big_list = None
            if excel_path != None and (str(excel_path).split("."))[-1] in ["xls", "xlsx"]:
                book = xlrd.open_workbook(excel_path)
                table = book.sheet_by_index(0)
                nrows = table.nrows
                response_big_list = []
                for i in range(1, nrows):
                    try:
                        cell_row_value = table.row_values(i)
                        print(cell_row_value,len(cell_row_value))
                        cell_row_value_list = []
                        for i in cell_row_value:
                            if i != '':
                                cell_row_value_list.append(i)
                        response_big_list.append(cell_row_value_list)
                    except BaseException as e:
                        print(e)
                        continue
            print(response_big_list)
            sql = '''insert into equipment_manager(equipment_id,equipment_classid,equipment_infomation) values(%s,%s,%s)'''
            for i in response_big_list:
                try:
                    insert_result = func_tools_sql_manager.excute(sql, [i[0], storehouse_id,json.dumps(i[1::],ensure_ascii=False)])
                    print(insert_result)
                except BaseException as e:
                    continue
                    print(e)
        return True


if __name__ == "__main__":
    ss = Sql_2to2_Excel()
    # ss.return_storehouse_to_excel()
    # ss.get_input_excel_to_sql('1', r'../static/output_excel/eb19cb06-3744-447c-ad4b-218ce3e07e57.xls')
