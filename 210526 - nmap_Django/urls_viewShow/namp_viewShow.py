from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import uuid, time, os, random,datetime
import logging, hashlib, json

from unit_Tools.sqlData_unitTools import sqlData_unitTools
from unit_Tools.nmap_unitTools import nmap_unitTools

sqlData_unitToolsC = sqlData_unitTools()
nmap_unitToolsC = nmap_unitTools()
def nmap_search(request):
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    if request.method == "GET":
        print("-"*15,"ViewFunc nmap_search - Get","-"*15)
        return render(request, "admins/nmap_search.html")
    elif request.method == "POST":
        print("-" * 15, "ViewFunc nmap_search - Post", "-" * 15)
        sql = '''select nmapRow from nampscan order by id desc limit 10'''
        search_nmapscan = sqlData_unitToolsC.search(sql, show=True)
        return_jsonList = []
        if search_nmapscan:
            for i in search_nmapscan:
                return_jsonList.append(i[0])
        return HttpResponse(json.dumps({"return_jsonList":return_jsonList}))


def nmap_searchDB(request):
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    if request.method == "GET":
        print("-"*15,"ViewFunc nmap_searchDB - Get","-"*15)
        return render(request, "admins/namp_searchDB.html")
    elif request.method == "POST":
        print("-"*15,"ViewFunc nmap_searchDB - Post","-"*15)
        search_content = request.POST.get('search_content', "None")
        print("-"*15,"ViewFunc nmap_searchDB - search_content：%s" %(search_content),"-"*15)
        if search_content == "search_all" or search_content == None:
            sql = '''select nmapRow from nmapscan order by id desc limit 1000'''
            search_nmapscan = sqlData_unitToolsC.search(sql, show=False)
            return_jsonList = []
            if search_nmapscan:
                for i in search_nmapscan:
                    return_jsonList.append(i[0])
        else:
            sql = '''select nmapRow from nampscan order by id desc limit 1000'''
            search_nmapscan = sqlData_unitToolsC.search(sql, show=False)
            return_jsonList = []
            if search_nmapscan:
                for i in search_nmapscan:
                    if search_content in str(eval(i[0])[0]) or search_content in str(list(eval(i[0])[2].keys())):
                        return_jsonList.append(i[0])
        return HttpResponse(json.dumps({"return_jsonList":return_jsonList}))


def namp_scanAPI(request):
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    if request.method == "GET":
        print("-" * 15, "ViewFunc namp_scanAPI - Get", "-" * 15)
        return HttpResponse(404)
    elif request.method == "POST":
        ipAddress = request.POST.get('ipAddress', "None")
        ipPort = request.POST.get('ipPort', "None")
        print("-" * 15, "ViewFunc namp_scanAPI - ipAd:%s ipPo:%s"%(ipAddress,ipPort), "-" * 15)
        result = nmap_unitToolsC.scanRe_insertDB(ipAddress,ipPort)
        if result:
            return HttpResponse(200)
        else:
            return HttpResponse(400)