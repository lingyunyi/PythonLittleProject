from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import threading, requests
import uuid, time, os
import logging, hashlib, json
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def download_files(request):
    '''
        获取指定下载文件
    :param request:
    :return:
    '''
    '''
        得从请求中获取到文件路径
    '''
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    logger.warning("%s - function read_file" % (ip))
    try:
        filename = request.GET["download_files"]
        file = open('static/backups_dir/%s'%(filename), 'rb')
        response = HttpResponse(file)
        file.close()
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="%s"'%(filename)
        return response
    except BaseException as e:
        logging.exception('function users_disk_manager  - %s - requests method post - except' % (e), exc_info=True)
        return HttpResponse(404)

def download_files_all(request):
    '''
        获取指定下载文件
    :param request:
    :return:
    '''
    '''
        得从请求中获取到文件路径
    '''
    # 获取远程访问IP
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 输出日志
    logger.warning("%s - function read_file" % (ip))
    try:
        filename = request.GET["download_files"]
        file = open('static/%s'%(filename), 'rb')
        response = HttpResponse(file)
        file.close()
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="%s"'%(filename)
        return response
    except BaseException as e:
        logging.exception('function users_disk_manager  - %s - requests method post - except' % (e), exc_info=True)
        return HttpResponse(404)