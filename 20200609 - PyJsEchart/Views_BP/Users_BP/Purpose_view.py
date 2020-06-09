from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import threading, requests
import uuid, time, os
import logging, hashlib, json
from Tools_BP.sql_tools import SqlManger

qqq_sql_manager = SqlManger()

def re_show(request):
    return redirect('/place_show/?nid=none')


def index_show(request):
    if request.method == "GET":
        try:
            nid = request.GET.get("nid", None)
            select_time = request.GET.get("select_time", None)
            print(nid)
        except BaseException as e:
            print(e)

        '''
            这里是初步进入，所以直接推荐给他，当前时间，最好的饭堂。
        '''


        if nid == "none" or nid == "":
            sql = "select * from location"
            select_list = qqq_sql_manager.search(sql, [])
            max_list = []
            for i in select_list:
                up_time = str(i[-1]).split("-")[0].split(":")[0]
                down_time = str(i[-1]).split("-")[1].split(":")[0]
                select_timex = time.strftime("%H", time.localtime())
                print("up_time", up_time, "down_time", down_time, "select_timex", select_timex)
                if int(select_timex) <= int(down_time) and int(select_timex) >= int(up_time):
                    less_num = int(i[2]) - int(i[3])
                    max_list.append([i[0], i[1], less_num])
                if max_list != []:
                    max_list = sorted(max_list, key=(lambda x: x[2]), reverse=True)
                    nid = max_list[0][0]
                else:
                    nid = i[0]
                    select_time = "暂无推荐 - 请选择"

        '''
            这里是通过选择进入，选择进入的就按照选择进入的推荐
        '''

        if nid != None and nid != "":
            sql = "select * from location where id = %s"
            select_nid = qqq_sql_manager.search(sql,[nid])
            if select_nid == ():
                select_nid == [None]
            return render(request, 'index.html', {
                "select_nid":select_nid[0],
                "select_time":select_time
            })

    '''
        选择时间，是如何推荐的。
        也是一样，首先判断选择的时间，是否在已经拥有的饭堂的开放时间呢。
        如果是，进行第二部。
        判断这些这些饭堂的剩余人数，剩余的人数越多，越能体现。就是进行调到人数最多的饭堂中。
    
    '''
    if request.method == "POST":
        '''
            如果是POST请求，那么这个一定是通过选择时间过来的。
            那么既然是通过选择时间过来的，就得获取他选择的世界。
            然后通过简单决策去判断。然后得出结果。
            这样的话，就可以根据他选择的时间返回其结果。
        '''
        ret = {"status":"false","nid":"None","time":"None"}
        try:
            select_time = request.POST.get("select_time",None)
            sql = "select * from location"
            select_list = qqq_sql_manager.search(sql, [])
        except BaseException as e:
            print(e)
        print("select_time",select_time)
        if select_time != None and select_time != "" and select_list != ():
            max_list = []
            for i in select_list:
                up_time = str(i[-1]).split("-")[0].split(":")[0]
                down_time = str(i[-1]).split("-")[1].split(":")[0]
                print("up_time",up_time,"down_time",down_time)
                if int(select_time) <= int(down_time) and int(select_time) >= int(up_time):
                    less_num = int(i[2]) - int(i[3])
                    max_list.append([i[0], i[1], less_num])
                if max_list != []:
                    max_list = sorted(max_list, key=(lambda x: x[2]), reverse=True)
                    ret["status"]="true"
                    ret["nid"] = max_list[0][0]
                    ret["time"] = select_time+":00 - "+str(int(select_time)+1)+":00"
        return HttpResponse(json.dumps(ret))


def other_place_show(request):
    '''
        推荐页面。
        这里有两个推荐要素。
        首先时间，就是当前时间，必须在饭堂的开放时间内。如果不在饭堂的开放时间内的话，是不会推荐的。
        其次，是人数，是按照剩余人数来进行推荐的，剩余人数越多，其排名越高。
    :param request:
    :return:
    '''
    sql = "select * from location"
    select_list = qqq_sql_manager.search(sql,[])

    if select_list != ():

        # 在这里判断剩余站位人数
        max_list = []
        for i in select_list:
            up_time = str(i[-1]).split("-")[0].split(":")[0]
            down_time = str(i[-1]).split("-")[1].split(":")[0]
            print("up_time", up_time, "down_time", down_time)
            select_time =  time.strftime("%H", time.localtime())
            if int(select_time) <= int(down_time) and int(select_time) >= int(up_time):
                less_num = int(i[2]) - int(i[3])
                max_list.append([i[0],i[1],less_num])

        max_list = sorted(max_list,key=(lambda x:x[2]),reverse=True)

        print(max_list)
        if max_list == []:
            max_list =None

    return render(request, 'other_place.html', {
        "select_list":max_list
    })
