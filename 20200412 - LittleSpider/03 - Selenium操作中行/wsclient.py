from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time,json,csv,os,uuid,copy,threading
from websocket import create_connection
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s  - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Seleniums(object):

    def __init__(self):
        pass

    def login_spider(self):
        '''

        :return:
        '''
        url = 'https://bank.pingan.com.cn/m/main/index.html'


        browser = webdriver.Firefox(executable_path="./geckodriver.exe")
        browser.get(url)

        time.sleep(5)
        try:
            browser.switch_to.frame("newbankframe")
        except BaseException as e:
            logger.warning(e)
        # 等待登入界面出现
        WebDriverWait(browser, 5000).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '/html/body/div[2]/section/div[4]/div[1]/div/div[2]/div[1]/div[2]')
            )
        )
        browser.find_element_by_xpath('/html/body/div[2]/section/div[4]/div[1]/div/div[2]/div[1]/div[2]').click()
        # 点击登入
        logger.warning("点击登入")
        browser.switch_to.window(browser.window_handles[0])
        # 等待安全退出出现
        WebDriverWait(browser, 50000).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '/html/body/div[2]/section/div[3]/div[1]/div/ul/li/a')
            )
        )
        browser.switch_to.window(browser.window_handles[0])
        try:
            browser.switch_to.frame("newbankframe")
        except BaseException as e:
            logger.warning(e)
        # 点击登入
        # 尝试寻找是否已登入，如果已登入可以直接进行下一步，否则返回FALSE
        try:
            logout_text = browser.find_element_by_xpath("/html/body/div[2]/section/div[3]/div[1]/div/ul/li/a").text
        except BaseException as e:
            # 出错返回FALSE
            print(e)
            return False
        while True:
            try:
                if logout_text == "安全退出":
                    try:
                        # 尝试去掉需要升级界面
                        time.sleep(5)
                        browser.find_element_by_xpath('/html/body/div[4]/div[3]/a').click()
                        browser.find_element_by_xpath('/html/body/div[4]/span[1]/a').click()
                    except BaseException as e:
                        logger.warning(e)
                    try:
                        # 尝试去掉需要升级界面
                        browser.switch_to.frame("newbankframe")
                        browser.find_element_by_xpath('/html/body/div[4]/div[3]/a').click()
                        browser.find_element_by_xpath('/html/body/div[4]/span[1]/a').click()
                    except BaseException as e:
                        logger.warning(e)
                    # 点击转账
                    logger.warning("点击转账")
                    browser.find_element_by_xpath("/html/body/div[2]/section/div[4]/div/div/ul/li[3]/a").click()
                    # 等待批量转账出现
                    WebDriverWait(browser, 5000).until(
                        EC.presence_of_all_elements_located(
                            (By.XPATH, '/html/body/div[2]/section/div[5]/div/div[2]/div/div/div[1]/div/ul/li[3]')
                        )
                    )
                    # 点击批量转账
                    browser.find_element_by_xpath('/html/body/div[2]/section/div[5]/div/div[2]/div/div/div[1]/div/ul/li[3]').click()
                    # 开始连接数据
                    pay_for_list_golbal = []
                    # 获取数据后批量循环
                    ws = create_connection("ws://127.0.0.1:8080/websocket/123123")
                    ws.send('{"data":{"descp":""},"message":"","status":5}')
                    count = 5
                    while True:
                        # ws 接受数据异常处理 ----------------------------------------------------------------
                        pay_for_list_golbal.clear()
                        try:
                            time.sleep(3)
                            count -= 5
                            if count == 0:
                                count = 5
                                ws.send('{"data":{"descp":""},"message":"","status":0}')
                            result = ws.recv()
                            logger.warning("%s%s" % ("My_RECV  = ", result))
                            result_JSON = json.loads(result)
                            if result_JSON.get("status", 0) == 2:
                                logger.warning('if result_JSON.get("status", 0) == 2:{}'.format(result_JSON.get("status", 0)))
                                if result_JSON.get("data", None) != None:
                                    logger.warning('if result_JSON.get("data", None) != None:')
                                    for little_dict in result_JSON.get("data", None):
                                        if type(little_dict) == str:
                                            little_dict = json.loads(little_dict)
                                        money = little_dict.get('money',None)
                                        name = little_dict.get('name',None)
                                        accid = little_dict.get('accid',None)
                                        order = little_dict.get('order',None)
                                        logger.warning(little_dict)
                                        if money != None and name != None and accid != None:
                                            logger.warning(little_dict)
                                            pay_for_list_golbal.append([money, name, accid,order])
                        except BaseException as e:
                            ws = create_connection("ws://127.0.0.1:8080/websocket/123123")
                            ws.send('{"data":{"descp":""},"message":"","status":5}')
                            logger.warning("数据接收异常：%s"%(e))
                        # ws 接受数据异常处理 ----------------------------------------------------------------
                        if pay_for_list_golbal != []:
                            logger.warning('pay_for_list != []:{}'.format(pay_for_list_golbal))
                            # 在这里批量写入导入数据
                            # 数据导入阶段异常处理 ----------------------------------------------------------------
                            for pay_user in pay_for_list_golbal:
                                try:
                                    time.sleep(1.5)
                                    try:
                                        browser.switch_to.frame("newbankframe")
                                    except BaseException as e:
                                        logger.warning("for pay_user in pay_for_list:except BaseException as e:newbankframe")
                                    # 等待新添收款人出现
                                    WebDriverWait(browser, 5000).until(
                                        EC.presence_of_all_elements_located(
                                            (By.XPATH, '/html/body/div[2]/section/div[5]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div[3]/ul/li/div/div/a[3]')
                                        )
                                    )
                                    logger.warning("等待新添收款人出现")
                                    # 点击新增收款人
                                    browser.find_element_by_xpath('/html/body/div[2]/section/div[5]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div[3]/ul/li/div/div/a[3]').click()
                                    # 等待转账金额输入框出现
                                    WebDriverWait(browser, 5000).until(
                                        EC.presence_of_all_elements_located(
                                            (By.XPATH, '//*[@id="transAmt"]')
                                        )
                                    )
                                    # 对需要传入传值(金额)
                                    browser.find_element_by_xpath('//*[@id="transAmt"]').send_keys(pay_user[0])
                                    # 对需要传入传值(收款人)
                                    browser.find_element_by_xpath('/html/body/div[2]/section/div[5]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/ul/li[2]/div/div/div[1]/div/input').send_keys(pay_user[1])
                                    # 对需要传入传值(收款账号)
                                    browser.find_element_by_xpath('//*[@id="payeeBankCardInput"]').send_keys(pay_user[2])
                                    time.sleep(1)
                                    browser.find_element_by_xpath('/html/body/div[2]/section/div[5]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/ul/li[4]/div/a[1]').click()
                                    logger.warning("点击确认")
                                    try:
                                        logger.warning("----------------------强行异常处理")
                                        # 数据导入阶段异常处理（详细异常处理） ----------------------------------------------------------------
                                        try:  # 判断是否重复导入异常
                                            browser.find_element_by_xpath('/html/body/div[5]/div[2]/p[2]/a[1]').click()
                                            logger.warning("----------------------强行异常处理,出现账号重复导致异常")
                                        except:  # 判断是否重复导入异常
                                            logger.warning("----------------------强行异常处理,没有出现账号重复异常")

                                        try:  # 判断是否输入卡号错误
                                            browser.find_element_by_xpath('/html/body/div[2]/section/div[5]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/ul/div/div/li[1]/div/div/div/input')
                                            logger.warning("----------------------强行异常处理,出现输入卡号错误异常")
                                            browser.find_element_by_xpath('/html/body/div[2]/section/div[5]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/ul/li[4]/div/a[2]').click()
                                            ws.send('{"data":{"order":"%s"},"message":"","status":0}' % (pay_user[4]))
                                            logger.warning('ws.send {"data":{"order":"%s"},"message":"","status":0}' % (pay_user[4]))
                                        except:  # 判断是否输入卡号错误
                                            logger.warning("----------------------强行异常处理,没有输入卡号错误异常")
                                        try:  # 尝试再次确认
                                            browser.find_element_by_xpath('/html/body/div[2]/section/div[5]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/ul/li[4]/div/a[1]').click()
                                            logger.warning("----------------------强行异常处理,出错了，我想再点击确认一次")
                                        except:  # 尝试再次确认
                                            logger.warning("----------------------强行异常处理,出错了，我想再点击确认一次，但是没有点击确认")
                                    except BaseException as e:
                                        logger.warning("----------------------强行异常处理,真的异常%s"%(e))
                                except BaseException as e:
                                # 数据导入阶段异常处理 ----------------------------------------------------------------
                                    logger.warning("数据导入阶段异常处理,%s"%e)
                                    # 数据导入阶段异常处理（详细异常处理） ----------------------------------------------------------------
                                    try:# 判断是否重复导入异常
                                        browser.find_element_by_xpath('/html/body/div[5]/div[2]/p[2]/a[1]').click()
                                        logger.warning("出现账号重复导致异常")
                                    except:# 判断是否重复导入异常
                                        logger.warning("没有出现账号重复异常")

                                    try:# 判断是否输入卡号错误
                                        browser.find_element_by_xpath('/html/body/div[2]/section/div[5]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/ul/div/div/li[1]/div/div/div/input')
                                        logger.warning("出现输入卡号错误异常")
                                        browser.find_element_by_xpath('/html/body/div[2]/section/div[5]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/ul/li[4]/div/a[2]').click()
                                        ws.send('{"data":{"order":"%s"},"message":"","status":0}'%(pay_user[4]))
                                        logger.warning('ws.send {"data":{"order":"%s"},"message":"","status":0}'%(pay_user[4]))
                                    except:# 判断是否输入卡号错误
                                        browser.find_element_by_xpath('/html/body/div[2]/section/div[5]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/ul/li[4]/div/a[2]').click()
                                        logger.warning("没有输入卡号错误异常")
                                    try:# 尝试再次确认
                                        browser.find_element_by_xpath('/html/body/div[2]/section/div[5]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/ul/li[4]/div/a[1]').click()
                                        logger.warning("出错了，我想再点击确认一次")
                                    except:# 尝试再次确认
                                        logger.warning("出错了，我想再点击确认一次，但是没有点击确认")
                                    # 任何导入异常都需要，循环到底，直至循环结束
                                    time.sleep(3)
                                    continue
                                    # 数据导入阶段异常处理（详细异常处理） ----------------------------------------------------------------
                                # 数据导入阶段异常处理 ----------------------------------------------------------------
                        else:
                            logger.warning('pay_for_list == []:{}'.format(pay_for_list_golbal))
                            time.sleep(1)
            except BaseException as e:
                logger.warning("登入之前的异常%s"%(e))
                time.sleep(5)
                continue





if __name__ == '__main__':
    s = Seleniums()
    s.login_spider()
