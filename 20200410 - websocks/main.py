import bottle
from bottle import template, Bottle,request,redirect
# from arduino.rotary import Rotary
import logging
import sys,os

root = Bottle()




@root.route('/',method=["GET", "POST"])
def index():
    if request.method == "GET":
        # 如果请求是GET请求
        return template('index.html')
    elif request.method == "POST":
        # 如果请求为POST 又不是JSON数据
        if request.json == None:
            id_value = request.forms.get("id_value")
            function = request.forms.get("function")
            print("From clinet data is ",select,select2)
        elif request.json != None:
            jsonDB = request.json

        if str(function) == str(1):
            # 执行打开视频
            fr = open("","r+",encoding="utf-8")
            fw = open("temp_1.yml","w+",encoding="utf-8")
            str_fr = fr.read().replace("*****",int(id_value))
            fw.write(str_fr)
            fr.close()
            fw.close()
            cmd = '''python '''
            p = os.popen(cmd)
        elif str(function) == str(2):
            # 执行采集数据
            fr = open("","r+",encoding="utf-8")
            fw = open("temp_2.yml","w+",encoding="utf-8")
            str_fr = fr.read().replace("*****",int(id_value))
            fw.write(str_fr)
            fr.close()
            fw.close()
            cmd = '''python '''
            p = os.popen(cmd)
        elif str(function) == str(3):
            # 执行转台控制
            '''
            logging.basicConfig(level=logging.DEBUG)
            rotary = Rotary("COM3")
            rotary.open()
            try:
                rotary.get_position()
                rotary.goto(a=10)
                # for pos in get_positions_from_str("H@-2:2:1*V@-1:1:0.5"):
                #     rotary.goto(**pos)
                #     time.sleep(0.5)
            finally:
                # rotary.reset()
                rotary.close()
    
            '''
        redirect("/")







         # return template('<b>Hello {{name}}</b>!', name="Alex")


if __name__ == "__main__":
    sys.path.append(".")
    root.run(host='0.0.0.0', port=8000)