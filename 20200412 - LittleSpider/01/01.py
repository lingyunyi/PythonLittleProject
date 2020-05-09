# 导入urllib网络请求库，re正则库，json序列化库。
from urllib import request
import re,json,random,os


class Xuetangx_Spider(object):

    def __init__(self):
        self.url = "http://www.xuetangx.com/partners"
        self.like_jsonDB = {}


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

    def get_all_university(self):
        '''
            使用urllib，与re正则函数获取并处理数据
        :return:
        '''
        reGet = request.Request(url=self.url, headers=self.get_request_headers(), method='GET')
        # 发送一个get请求，并获取其返回值
        response = request.urlopen(reGet)
        # 对返回值进行数据清洗
        wait_str = str(response.read().decode('utf-8')).replace("\n", "").replace("门课程","")
        # 获取所有的院校及课程数目
        wait_str_tuple = re.findall('<h3>(.*?)</h3><p>(.*?)</p>', wait_str)[3::]
        # 清洗数据，删除重复数据
        wait_str_set = set(wait_str_tuple)
        wait_str_tuple_sorted = sorted(wait_str_set, key=lambda x: eval(x[1]),reverse=True)
        # 初始化一个字典
        for i in wait_str_tuple_sorted:
            if i[0] != "":
                self.like_jsonDB['{}'.format(i[0])] = eval(i[1])
        return self.like_jsonDB



    def save_json_flie(self):
        '''
            将类字典hash文件进行序列号json存储
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
        self.get_all_university()
        self.save_json_flie()


if __name__ == "__main__":

    # 实例化爬虫对象，实例化同时对象会同时调用__init__初始化函数
    spider = Xuetangx_Spider()
    spider.main()






