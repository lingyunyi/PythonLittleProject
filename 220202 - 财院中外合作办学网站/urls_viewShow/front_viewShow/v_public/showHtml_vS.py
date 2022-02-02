from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import uuid, time, os, random, datetime
import logging, hashlib, json
from unit_Tools import Base_Setting
from unit_Tools import Public_Func
from unit_Tools.Public_Func import SqlData_FuncO



def fr_index(request):
    # 学院首页
    if request.method == "GET":
        return render(request, "front_web/w_public/front_index.html", Base_Setting.Front_Common_Render)

def fr_sc_dynamic(request):
    # 学院动态页面
    if request.method == "GET":
        return render(request, "front_web/w_public/front_School_dynamic.html", Base_Setting.Front_Common_Render)

def fr_sc_login(request):
    # 学院后台登入页
    if request.method == "GET":
        return render(request, "front_web/w_public/front_School_login.html", Base_Setting.Front_Common_Render)

def fr_sc_overseas(request):
    # 学院留学生
    if request.method == "GET":
        return render(request, "front_web/w_public/front_School_overseas.html", Base_Setting.Front_Common_Render)

def fr_sc_partners(request):
    # 学院合作院校
    if request.method == "GET":
        return render(request, "front_web/w_public/front_School_partners.html", Base_Setting.Front_Common_Render)

def fr_sc_show(request):
    # 学院展示
    if request.method == "GET":
        return render(request, "front_web/w_public/front_School_show.html", Base_Setting.Front_Common_Render)


def fr_sc_student(request):
    # 学院学生留言墙
    if request.method == "GET":
        return render(request, "front_web/w_student/front_School_student.html", Base_Setting.Front_Common_Render)


def fr_sc_teacher(request):
    # 学院教师留言墙
    if request.method == "GET":
        return render(request, "front_web/w_teacher/front_School_teacher.html", Base_Setting.Front_Common_Render)
