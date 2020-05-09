# 导入urllib网络请求库，re正则库，json序列化库。
#coding:utf-8
from urllib import request
import re,json,random,os


class Lianjia_Spider(object):

    def __init__(self):
        self.url = "https://bj.fang.lianjia.com/loupan/pg{}/"
        self.like_jsonDB = {}
        self.page = 5

    def get_request_headers(self):
        '''
            返回随机的请求头中的user-agent
        :return:
        '''
        USER_AGENTS = [
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"
        ]

        headers = {
            "User-Agent": random.choice(USER_AGENTS),
        }
        return headers

    def get_all_homes(self):
        '''
            使用urllib，与re正则函数获取并处理数据
        :return:
        '''
        # 需要循环的页面数
        for i in range(1, self.page+1):
            try:
                url = self.url.format(i)
                print(url)
                reGet = request.Request(url=url, headers=self.get_request_headers(), method='GET')
                # 发送一个get请求，并获取其返回值
                response = request.urlopen(reGet,timeout=1)
                # 对返回值进行数据清洗
                wait_str = str(response.read().decode('utf-8')).replace("\n", "").replace(" ","").replace("\\","").replace("'","").replace('"',"")
                # 开始分批次获取数据
                # print(wait_str)
                all_li = re.findall('<liclass=resblock-list.*?<divclass=resblock-desc-wrapper>(.*)</div></li>',wait_str)[0]
                # print(all_li)
                homename_type_salestatus = re.findall("<divclass=resblock-name><a.*?>(.*?)</a><span.*?>(.*?)</span><span.*?>(.*?)</span></div>", all_li)[:-1]
                resblock_location = re.findall("<divclass=resblock-location><span>(.*?)</span>.*?<span>(.*?)</span>.*?<a.*?>(.*?)</a></div>", all_li)[:-1]
                resblock_area = re.findall("<divclass=resblock-area><span>(.*?)</span></div>", all_li)[:-1]
                resblock_tag = re.findall("<divclass=resblock-tag><span>(.*?)</span><span>(.*?)</span>", all_li)
                main_price = re.findall("<divclass=main-price><spanclass=number>(.*?)</span><spanclass=desc>&nbsp;(.*?)</span>", all_li)

                for i in range(len(homename_type_salestatus)):
                    self.like_jsonDB[homename_type_salestatus[i][0]] = {
                        "type": homename_type_salestatus[i][1],
                        "salestatus": homename_type_salestatus[i][2],
                        "resblock_location": resblock_location[i],
                        "resblock_area":resblock_area[i],
                        "main_price": "%s%s" % (main_price[i][0], main_price[i][1]),
                        "resblock_tag": resblock_tag[i],
                    }
            except BaseException as e :
                print("for is false",e)
                continue


        return self.like_jsonDB



    def save_json_flie(self):
        '''

        :return:
        '''
        if self.like_jsonDB != {}:
            # os.getcwd() 获取当前工作路径
            with open("%s\%s.json"%(os.getcwd(),"DataBase"),"w",encoding='utf-8') as f:
                json.dump(self.like_jsonDB, f,ensure_ascii=False)
                # 别忘记关闭文件
                f.close()
        return True

    def main(self):
        '''
            启动文件
        :return:
        '''
        self.get_all_homes()
        self.save_json_flie()


if __name__ == "__main__":

    # 实例化爬虫对象，实例化同时对象会同时调用__init__初始化函数
    spider = Lianjia_Spider()
    spider.main()







