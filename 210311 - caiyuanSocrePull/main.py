import requests, re, time

base_url = 'http://jwglxt.gxufe.edu.cn/taglib/DataTable.jsp?tableId=6393005'
all_list = []
form_header = {

    "Host": "jwglxt.gxufe.edu.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "81",
    "Origin": "http://jwglxt.gxufe.edu.cn",
    "Connection": "keep-alive",
    "Referer": "http://jwglxt.gxufe.edu.cn/student/xscj.ckcjrdjl.jsp?menucode=JW130705",
    "Cookie": "JSESSIONID=BAB443A704019A24636F46F770438C9E.kingo154; route=1bd07bc875c8a52f1c3c52d172cecff1",
    "Upgrade-Insecure-Requests": "1",
    'Connection': 'close'

}  # 设置请求头，字典格式

# 2023 202024149, 202024205+1
# 2022 202024089, 202024147+1
# 2021 202024087-55, 2020242087+1

for id in range(202024149, 202024205 + 1):
    form_data = {
        "dxan": "3",
        "xh": "{}".format(id),
        "xn": "2020",
        "xn1": "2021",
        "xq": "0",
        "sjxzS": "on",
        "yd": "0",
        "menucode_current": "JW130713"
    }
    r = requests.post(base_url, data=form_data, headers=form_header, )
    courese_name = re.findall("name='kchj'  align='left' >(.*?)<", r.text)
    courese_score = re.findall("name='yscj'  align='right' >(.*?)<", r.text)
    temp_list = []
    sum_score = 0
    for i in range(0, len(courese_name)):
        temp_list.append(courese_name[i])
        temp_list.append(courese_score[i])
        try:
            temp_num = float(courese_score[i])
            sum_score += temp_num
        except:
            pass
    temp_list.append(sum_score)
    temp_list.append(id)
    all_list.append(temp_list)
    print(all_list)



if __name__ == '__main__':
    pass
