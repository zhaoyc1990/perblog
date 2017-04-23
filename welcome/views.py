# coding=utf-8
import os, time, json, random
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from . import database
from .models import PageView, Announcement, Article, ArticleRely, TimeLine
from .models import Websiteinfo, Protagonist, Links, ArticleCategory, AccessBy
from .utils import articlecode, arttagstolist
from django.db.models import Q

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
    #网站信息
    websiteinfo = None
    websiteinfo_num = Websiteinfo.objects.count()
    if websiteinfo_num > 0:
        websiteinfo = Websiteinfo.objects.get()
	#网站公告
    announcement = Announcement.objects.all()
    #博主信息
    protagonist = None
    protagonist_num = Protagonist.objects.count()
    if protagonist_num > 0:
        protagonist = Protagonist.objects.get()
    #友情链接
    links = Links.objects.all()
    #时间线
    timeline = TimeLine.objects.all()[0:4]
    #最热排行--浏览量
    hot_art = Article.objects.all().values('id','title').order_by('-pageviews')[0:7]
    print '热门排行', len(hot_art)
    #顶置的文章
    tmp_topart = []
    topart = Article.objects.filter(isstick=1)
    for art in topart:
        art.relycount = art.artrely.count()
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
        "websiteinfo": websiteinfo,
        'protagonist': protagonist,
        'links': links,
        'timeline': timeline,
	})

def timeline(request):
    # 网站信息
    websiteinfo = None
    websiteinfo_num = Websiteinfo.objects.count()
    if websiteinfo_num > 0:
        websiteinfo = Websiteinfo.objects.get()
    year = 2017
    nowyear = int(time.strftime('%Y', time.localtime(time.time())))
    timelines = []
    while (year <= nowyear):
        timelines.append(list(TimeLine.objects.filter(year=year)))
        nowyear = nowyear - 1
    return render(request, 'timeline.html', {
        'timelines':timelines,
        'websiteinfo': websiteinfo,
    })



#文章内容展示页
def detail(request, aid):
    # 网站信息
    websiteinfo = None
    websiteinfo_num = Websiteinfo.objects.count()
    if websiteinfo_num > 0:
        websiteinfo = Websiteinfo.objects.get()
    # 博主信息
    protagonist = None
    protagonist_num = Protagonist.objects.count()
    if protagonist_num > 0:
        protagonist = Protagonist.objects.get()

    #文章分类导航
    art_cate = ArticleCategory.objects.all()
    print "文章ID:", aid
    #文章回复量
    art = Article.objects.get(id=aid)
    art_rely = ArticleRely.objects.filter(artid=aid)
    print '文章回复:', art_rely
    # 类似文章
    taglist = arttagstolist(art.tags)
    if len(taglist) == 1:
        art_like = Article.objects.filter(title__contains=taglist[0]).values('id','title')
    elif len(taglist) == 2:
        art_like = Article.objects.filter(Q(title__contains=taglist[0])|Q(title__contains=taglist[1])).values('id','title')
    elif len(taglist) == 3:
        art_like = Article.objects.filter(Q(title__contains=taglist[0])|Q(title__contains=taglist[1])|Q(title__contains=taglist[2])).values('id','title')
    elif len(taglist) == 4:
        art_like = Article.objects.filter(Q(title__contains=taglist[0])|Q(title__contains=taglist[1])|Q(title__contains=taglist[2])|Q(title__contains=taglist[3])).values('id','title')
    elif len(taglist) == 5: #最多支持五个标签模糊查找 类似文章
        art_like = Article.objects.filter(Q(title__contains=taglist[0])|Q(title__contains=taglist[1])|Q(title__contains=taglist[2])|Q(title__contains=taglist[3])|Q(title__contains=taglist[4])).values('id','title')
    else:
        art_like = Article.objects.filter(title__contains=art.title).values('id','title')
    #随机文章
    art_random = Article.objects.order_by('?').values('id','title')[:6]
    isread =  request.session.get('art'+str(art.id),None)
    print '文章浏览量:', art.pageviews
    if isread == None or int(time.time())-request.session.get('art'+str(art.id)+'dir',int(time.time())) > 3600:
        print '没有COOKIE或阅读时间过期'
        art.pageviews = art.pageviews+1
        art.save()
        request.session['art' + str(art.id)] = True
        request.session['art' + str(art.id) + 'dir'] = int(time.time())
    else:
        print '有COOKIE',isread
        request.session['art' + str(art.id) + 'dir'] = int(time.time())
    return render(request, 'detail.html',{
        'count': PageView.objects.count(),
        'art': art,
        'art_rely': art_rely,
        "websiteinfo": websiteinfo,
        'protagonist': protagonist,
        'art_cate': art_cate,
        'art_like': art_like[0:4],
        'art_random': art_random,
    })

def about(request):
    # 网站信息
    websiteinfo = None
    websiteinfo_num = Websiteinfo.objects.count()
    if websiteinfo_num > 0:
        websiteinfo = Websiteinfo.objects.get()
    return render(request, 'about.html',{
        'websiteinfo': websiteinfo,
    })

#动态获取下一页
def homenext(request):
    if request.method == 'POST':
        art_index = json.loads(request.body.decode())
        try:
            currentIndex = art_index['currentIndex']
            pagesize = art_index['pageSize']
            type = art_index['type']
        except KeyError: #获取数据 不完整时 ，返回错误
            return JsonResponse({'Success':False})
        if type == 1: # 1 代表首页, 2 代表文章专栏
            start = (currentIndex-1)*7 +1
            end = currentIndex*7 +1
        print "currentIndex", currentIndex
        art = Article.objects.filter(isstick=0)[start:end]
        art_count = Article.objects.count()
        response_data = {}
        response_data['Data'] = articlecode(art)
        response_data['Success'] = True
        response_data['SubCode'] = art_count
        return JsonResponse(response_data)
    else:
        return JsonResponse({'Success':False})

def articlerely(request):
    if request.method == 'POST':
        req_data = json.loads(request.body.decode())
        try:
            artid = req_data['artid']
            content = req_data['content']
        except KeyError:  # 获取数据 不完整时 ，返回错误
            return JsonResponse({'Success': False})
        if artid != None and content != None:
            response_data = {}
            response_data['Success'] = True
            response_data['avatar'] = settings.STATIC_URL + 'avatar/' + str(random.randint(1, 19)) + '.png'
            response_data['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            art = Article()
            art.id = int(artid)
            ArticleRely.objects.create(content=content, artid=art, name='未知', email='asdf@aa.com', photo=response_data['avatar'])
            return JsonResponse(response_data)

    return JsonResponse({'Success': False})

def message(request):
    if request.method == 'POST':
        req_data = json.loads(request.body.decode())
        try:
            name = req_data['name']
            content = req_data['content']
            email = req_data['email']
        except KeyError:  # 获取数据 不完整时 ，返回错误
            print '网站首页留言，提交数据不完整', req_data
            return JsonResponse({'Success': False})
        if name != None and content != None and email != None:
            response_data = {}
            response_data['Success'] = True
            ArticleRely.objects.create(content=content,name= name, email=email)
            print '有人留言,成功'
            return JsonResponse(response_data)
    return JsonResponse({'Success': False})

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