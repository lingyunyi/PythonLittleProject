import sqlData_unitTools,json
sqlData_unitToolsC = sqlData_unitTools.sqlData_unitTools()
sql = '''insert into infomana values (%s,%s)'''

a = {'title': '21312321', 'CreateTime': '2021-08-08 18:10:02', 'infoList': [{'centent': 'fsad', 'insertTime': '2021-08-08 18:10:02'}, {'centent':'asdf', 'insertTime': '2021-08-08 18:10:02'}, {'centent': 'sdafasd', 'insertTime': '2021-08-08 18:10:02'}]}
insert_result = sqlData_unitToolsC.excute(sql,[None,json.dumps(a)])
print(insert_result)
