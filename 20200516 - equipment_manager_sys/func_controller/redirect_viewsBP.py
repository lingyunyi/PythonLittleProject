from django.http import request
from django.shortcuts import redirect, render, HttpResponse, Http404
import threading, requests
import uuid, time, os
import logging, hashlib, json




def index(request):


    return redirect('/storehouse_manager/')

