# coding=utf-8
import os, time, json
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from . import database
from .models import PageView, Announcement, Article, ArticleRely, TimeLine

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
    #最热排行--浏览量
    hot_art = Article.objects.all().values('id','title').order_by('-pageviews')[0:7]
    print '热门排行', len(hot_art)
    #顶置的文章
    tmp_topart = []
    topart = Article.objects.filter(isstick=1)
    for art in topart:
        if art.stickposition > len(tmp_topart):
            tmp_topart.append(art)
        else:
            tmp_topart.insert(art.stickposition, art)
    #普通文章按时间顺序
    articles = Article.objects.filter(isstick=0)
    for art in articles:
        print art.artrely.count()
        art.relycount = art.artrely.count()
    return render(request, 'home.html',{
        'announcement': announcement,
        'articles': articles,
        "topart": tmp_topart,
        'hot_art': hot_art,
	})

def timeline(request):
    year = 2017
    timelines = []
    while (year >= 2017):
        timelines.append(list(TimeLine.objects.filter(year=year)))
        year = year - 1
    return render(request, 'timeline.html', {
        'timelines':timelines
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
    if(not path.endswith("/")):
        path = path + "/"
    file = open(path + file_name, "wb")
    file.write(data)
    file.flush()

def uploadImg(request):
    if request.method == 'POST':
        file_obj = open("log.txt", "w+")
        buf = request.FILES.get('imgFile', None)
        print >> file_obj, str(buf)
        file_buff = buf.read()
        time_format = str(time.strftime("%Y-%m-%d-%H%M%S", time.localtime()))
        file_name = "img" + time_format + ".jpg"
        save_file("welcome/static/article/images", file_name, file_buff)
        dict_tmp = {}
        dict_tmp['error'] = 0
        dict_tmp['url'] = '/static/article/images/' + file_name
        return HttpResponse(json.dumps(dict_tmp))