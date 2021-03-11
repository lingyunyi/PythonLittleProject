import requests
import json, time, datetime, re, random, json
import feifei_checkCode_API


class Gk_score():

    def __init__(self):
        self.session = requests.session()
        self.form_header = {
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

    def get_gk_score(self):
        print(self.session.cookies.items())
        get_scorelist_url = 'https://gzwb.zk789.cn/Signup/SignupStatistics.aspx'
        response = self.session.get(get_scorelist_url, headers=self.form_header, timeout=30)
        if "考生未登录或已登录超时" in response.text:
            return {"tip": "考生未登录或已登录超时...", "response": '400'}
        score_tuple = re.findall("</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>",
                                 str(response.text), re.S)
        score_list = sorted(score_tuple, key=lambda x: int(x[4]), reverse=True)
        return {"tip": "获取成功", "data": score_list, "response": '200'}

    def write_txt(self):
        get_gk_list = self.get_gk_score()
        if get_gk_list["response"] != "200":
            print(get_gk_list["tip"])
        else:
            print(get_gk_list["data"])
            with open('./data.txt', 'w+', encoding="utf-8") as f:
                f.write(json.dumps(get_gk_list["data"]))

    def one_get_login_cookies(self):
        # 从首页获取相关参数

        index_url = 'https://gzwb.zk789.cn/Default.aspx'
        response = self.session.get(index_url, headers=self.form_header, timeout=30)
        __EVENTTARGET = ""
        __EVENTARGUMENT = ""
        __VIEWSTATE = re.findall('id="__VIEWSTATE" value="(.*?)"', response.text)[0]
        __VIEWSTATEGENERATOR = re.findall('id="__VIEWSTATEGENERATOR" value="(.*?)"', response.text)[0]
        __EVENTVALIDATION = re.findall('id="__EVENTVALIDATION" value="(.*?)"', response.text)[0]

        # 调用别人接口获取验证码
        checkCodeAPI_url = 'https://gzwb.zk789.cn/Valicode.ashx'
        response = self.session.get(checkCodeAPI_url)
        # 获取的文本实际上是图片的二进制文本
        img = response.content
        # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
        with open('check_img/a.jpg', 'wb') as f:
            f.write(img)
        feifei_checkCode = feifei_checkCode_API.GetCode()
        check_result = feifei_checkCode.discernCode(pd_id="128707", pd_passwd="mlLjQkxrl4iNAtc0NsYcBwi5KXnCj12i",
                                                    code_type="30400",
                                                    image_path="check_img/a.jpg")
        if check_result["RetCode"] != "0":
            return {"tip": "无法获取验证码..."}
        __CHECKCODE = eval(check_result['RspData']).get("result")
        print(__CHECKCODE)

        # 开始登入
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

        self.form_header["Cookie"] = "ASP.NET_SessionId=%s;" % (self.session.cookies.get('ASP.NET_SessionId'))

        response = self.session.post(login_url, headers=self.form_header, data=form_data, timeout=30,
                                     allow_redirects=False)

        print(self.session.cookies, response.status_code)
        if response.status_code == 302:
            try:
                self.write_txt()
                return {"Tip": "一切正常...", "state_code": "200"}
            except BaseException as e:
                return {"Tip": "异常状况...%s" % (e), "state_code": "4444"}
        else:
            return {"Tip": "登录失败...", "state_code": "444"}


if __name__ == "__main__":
    Gk_score = Gk_score()
    while True:
        try:
            result = Gk_score.one_get_login_cookies()
            print(result)
            timetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime((time.time())))
            with open('./time.txt', 'w+', encoding="utf-8") as f:
                f.write(json.dumps({"times": timetime}))
            time.sleep(60 * random.choice([3, 5, 8, 9, 13]))
        except BaseException as e:
            print("循环异常", e)
            time.sleep(60 * random.choice([1, 2, 3]))
