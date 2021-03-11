import requests
import json, time,datetime
import Py验证码留言板与AI聊天.tools_map.mysql_manager as mysql_manager
tool_mysql = mysql_manager.SqlManger()

def get_96_hourVolume_and_hourPrice():
    form_header = {
        "Host": "a.91666.cloud",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "0",
        "Origin": "https://www.91666.cloud",
        "Connection": "keep-alive",
        "Referer": "https://www.91666.cloud/",
        "Cache-Control": "max-age=0"}
    one_url = '	https://a.91666.cloud/coinsale/coinsaleinfo'
    one_r = requests.post(one_url, headers=form_header, timeout=30)
    dict_data = one_r.json().get('data', None)
    volume = dict_data.get("volume",None)
    two_url = '	https://a.91666.cloud/coinsale/coinmysalelist'
    data = {
        "type": "2",
        "memberid": "",
        "beginprice": "",
        "endprice": "",
        "page": "1",
        "pageSize": "10",
        "beginnums": "",
        "endnums": "",
        "endId": "",
        "endPrice": ""
    }
    two_r = requests.post(two_url, headers=form_header, timeout=30, data=data)
    dataList = two_r.json().get('dataList', None)
    unitprice = dataList[3].get("unitprice", None)
    hourVolume_and_hourPrice = {}
    hourVolume_and_hourPrice["times"] =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    hourVolume_and_hourPrice["unitprice"] = unitprice
    hourVolume_and_hourPrice["volume"] = int(float(volume))
    return hourVolume_and_hourPrice


def write_txt():
    with open('volume.txt', 'a+') as f:
        content = get_96_hourVolume_and_hourPrice()
        f.write(json.dumps(content))
        f.write("\n")


def write_mysql():
    content = get_96_hourVolume_and_hourPrice()
    print(content)
    insert_data_json = json.dumps({
        "ip": "8.8.8.8",
        "location": "中国",
        "times": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime((time.time()))),
        "unitprice":"%.2f"%(float(content.get("unitprice",None))*7),
        "volume":content.get("volume",None),
    })
    sql = '''insert into message_board (dict_values) values (%s)'''
    excute_zero = tool_mysql.excute(sql, [insert_data_json], show=True)






