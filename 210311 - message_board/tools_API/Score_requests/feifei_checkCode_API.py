from re import match
from io import BytesIO
from time import time
import base64
import hashlib
import requests


class GetCode():
    def __init__(self):
        self.stamp = str(int(time()))
        self.s = requests.session()
        self.api_url = "http://pred.fateadm.com/api/capreg"  # 图文验证码识别接口

    def calcSign(self, pd_id, passwd, timestamp):
        """
         # MD5加密获取sign
        :param pd_id: 斐斐打码PD账号
        :param passwd: 斐斐打码PD密钥
        :param timestamp: 当前时间戳
        :return: 返回md5加密结果
        """
        md5 = hashlib.md5()
        md5.update((timestamp + passwd).encode())  # 转码后加密
        csign = md5.hexdigest()  # 返回摘要，作为十六进制数据字符串值
        md5 = hashlib.md5()
        md5.update((pd_id + timestamp + csign).encode())
        csign = md5.hexdigest()
        return csign

    def imageBase64(self, image_path):
        """
         #image转换base64
        :param image_path: image路径，本地绝对路径或URL
        :return: 返回base64
        """
        if match(r'^http://', image_path) or match(r'^https://', image_path):  # 判断image路径是否URL
            r = self.s.get(image_path, verify=False)  # 图片保存在内存
            base64_data = base64.b64encode(BytesIO(r.content).read())  # 内存中打开图片并获取图片base64编码
        else:
            with open(image_path, "rb") as f:  # open方式打开本地图片
                base64_data = base64.b64encode(f.read())  # 获取图片转换的base64编码
        return base64_data

    def discernCode(self, pd_id, pd_passwd, code_type, image_path):
        """
         # 第三方接口识别图文验证码
         # 开发者文档：http://docs.fateadm.com/web/#/1?page_id=6
        :param pd_id: 斐斐打码PD账号
        :param pd_passwd: 斐斐打码PD秘钥
        :param code_type: 识别类型,参考：http://www.fateadm.com/price.html
        :param image_path: 图片地址，本地或者url
        :return: 返回识别结果
        """
        headers = {
            "Content-type": "application/x-www-form-urlencoded"  # 参数类型，写死不可修改
        }

        payload = {
            "user_id": pd_id,  # 斐斐账户pd_id
            "timestamp": self.stamp,  # 整数型当前时间戳
            "sign": self.calcSign(pd_id=pd_id, passwd=pd_passwd, timestamp=self.stamp),  # md5加密密钥
            "predict_type": code_type,  # 识别的字符类型(参考斐斐打码文档)
            "img_data": self.imageBase64(image_path)  # 验证码图片转换成的base64
        }

        r = self.s.post(data=payload, url=self.api_url, headers=headers, verify=False)
        return r.json()


if __name__ == "__main__":
    print(GetCode().discernCode(
        pd_id="128707", pd_passwd="mlLjQkxrl4iNAtc0NsYcBwi5KXnCj12i", code_type="30400",
        image_path="https://gzwb.zk789.cn/Valicode.ashx")
    )
