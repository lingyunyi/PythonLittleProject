import re, requests, random, csv,json

'''
form_header = {
    "Host": "gzwb.zk789.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://gzwb.zk789.cn/Main.aspx",
    "Connection": "keep-alive",
    "Cookie": "ASP.NET_SessionId=noohoqnjyla2vhlgsvz0hzuu;",
    "Upgrade-Insecure-Requests": "1",
}


def get_gk_score():
    get_scorelist_url = 'https://gzwb.zk789.cn/Signup/SignupStatistics.aspx'
    response = requests.get(get_scorelist_url, headers=form_header, timeout=30)
    if "考生未登录或已登录超时" in response.text:
        return {"tip": "考生未登录或已登录超时...", "response": response.status_code}
    score_tuple = re.findall("</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>",
                             str(response.text), re.S)
    score_list = sorted(score_tuple, key=lambda x: int(x[4]), reverse=True)
    return {"tip": "获取成功", "data": score_list, "response": response.status_code}

a = get_gk_score()
print(a)
'''
'''
session = requests.session()

form_header = {
    "Host": "gzwb.zk789.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://gzwb.zk789.cn/Default.aspx",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "https://gzwb.zk789.cn",
}

index_url = 'https://gzwb.zk789.cn/Default.aspx'
response = session.get(index_url, headers=form_header, timeout=30)
__EVENTTARGET = ""
__EVENTARGUMENT = ""
__VIEWSTATE = re.findall('id="__VIEWSTATE" value="(.*?)"', response.text)[0]
__VIEWSTATEGENERATOR = re.findall('id="__VIEWSTATEGENERATOR" value="(.*?)"', response.text)[0]
__EVENTVALIDATION = re.findall('id="__EVENTVALIDATION" value="(.*?)"', response.text)[0]


# 调用别人接口获取验证码
checkCodeAPI_url = 'https://gzwb.zk789.cn/Valicode.ashx'
response = session.get(checkCodeAPI_url)
# 获取的文本实际上是图片的二进制文本
img = response.content
# 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
with open('check_img/a.jpg', 'wb') as f:
    f.write(img)

__CHECKCODE = input(":")
login_url = 'https://gzwb.zk789.cn/Default.aspx'
form_data = {
    '__EVENTTARGET': __EVENTTARGET,
    '__EVENTARGUMENT': __EVENTARGUMENT,
    '__VIEWSTATE': __VIEWSTATE,
    '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
    '__EVENTVALIDATION': __EVENTVALIDATION,
    'ctl00$ContentPlaceHolder1$tbSignupNumber': '21510109604157',
    'ctl00$ContentPlaceHolder1$tbIdentityNumber': '510182200203261419',
    'ctl00$ContentPlaceHolder1$tbPassword': 'a*654321',
    'ctl00$ContentPlaceHolder1$tbValicode': __CHECKCODE,
    'ctl00$ContentPlaceHolder1$btnLogin': '登++录',
}

form_header["Cookie"] = "ASP.NET_SessionId=%s;" % (session.cookies.get('ASP.NET_SessionId'))

response = session.post(login_url, headers=form_header, data=form_data, timeout=30,
                             allow_redirects=False)
print(response.text)
print(session.cookies, response.status_code)
'''

with open('data.txt', 'r') as f:
    reader = json.loads(f.read())
    reader = [i for i in reader]
    for row in reader[1:]:
        row.append(int(row[1]) + int(row[2]) + int(row[3]) + int(row[4]))
    reader = sorted(reader[1:], key=lambda x: int(x[5]), reverse=True)
    for num, row in enumerate(reader):
        row.append(int(num))
    reader[0] = ["院校名称", "普高类计划数", "中职类计划数", "普高类已报名人数", "中职类已报名人数", "总人数", "排名"]
    result_list = reader
    print(result_list)