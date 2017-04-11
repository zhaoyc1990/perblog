# coding=utf-8
import os, time, json
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView, Announcement
# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())

def temp(request):

    return render(request, 'temp.html',{
        'count': PageView.objects.count()
    })
	
def home(request):
	#网站公告
    announcement = Announcement.objects.all()

    return render(request, 'home.html',{
		'count': "222",
        'announcement': announcement
	})

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def save_file(path, file_name, data):
    if data == None:
            return
    mkdir(path)
    if(not path.enswith("/")):
        path = path + "/"
    file = open(path + file_name, "wb")
    file.write(data)
    file.flush()

def uploadImg(request):
    if request.method == 'POST':
        file_obj = open("log.txt", "w+")
        buf = request.FILES.get('file', None)
        print >> file_obj, str(buf)
        file_buff = buf.read()
        time_format = str(time.strftime("%Y-%m-%d-%H%M%S", time.localtime()))
        file_name = "img" + time_format + ".jpg"
        save_file("welcome/static/article/images", file_name, file_buff)
        dict_tmp = {}
        dict_tmp['error'] = 0
        dict_tmp['url'] = '/static/image/' + file_name
        return HttpResponse(json.dumps(dict_tmp))