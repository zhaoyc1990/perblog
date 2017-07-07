# coding=utf-8
import os, time, json, random
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from . import database
from .models import PageView, Announcement, Article, ArticleRely, TimeLine, GuestBook, Socialaccount, Socialuser
from .models import Websiteinfo, Protagonist, Links, ArticleCategory, AccessBy, Share, Ad, Smtpmail
from .utils import articlecode, arttagstolist
from qq import Qq
from django import http
from django.db.models import Q
from project.sendmail import Sendmail

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

#首页
def home(request):
    user = auth_user(request)
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
    timeline = TimeLine.objects.all().order_by('-timestamp')[0:4]
    #最热排行--浏览量
    hot_art = Article.objects.all().values('id','title').order_by('-pageviews')[0:7]
    print '热门排行', len(hot_art)
    #顶置的文章
    tmp_topart = []
    topart = Article.objects.filter(isstick=1)
    for art in topart:
        art.relycount = art.artrely.filter(review=True).count()
        if art.stickposition > len(tmp_topart):
            tmp_topart.append(art)
        else:
            tmp_topart.insert(art.stickposition, art)
    #普通文章按时间顺序
    articles = Article.objects.filter(isstick=0).order_by('-timestamp')[0:7]
    for art in articles:
        print art.artrely.count()
        art.relycount = art.artrely.filter(review=True).count()

    #广告
    ads = Ad.objects.all()
    return render(request, 'home.html',{
        'announcement': announcement,
        'articles': articles,
        "topart": tmp_topart,
        'hot_art': hot_art,
        "websiteinfo": websiteinfo,
        'protagonist': protagonist,
        'links': links,
        'timeline': timeline,
        'ads': ads,
        'user':user,
	})

#文章列表
def article(request):
    user = auth_user(request)

    # 网站信息
    websiteinfo = None
    websiteinfo_num = Websiteinfo.objects.count()
    if websiteinfo_num > 0:
        websiteinfo = Websiteinfo.objects.get()
    # 网站公告
    announcement = Announcement.objects.all()
    # 博主信息
    protagonist = None
    protagonist_num = Protagonist.objects.count()
    if protagonist_num > 0:
        protagonist = Protagonist.objects.get()
    # 文章分类导航
    art_cate = ArticleCategory.objects.all()
    # 广告
    ads = Ad.objects.all()
    # 顶置的文章
    tmp_topart = []
    topart = Article.objects.filter(isstick=1)
    for art in topart:
        art.relycount = art.artrely.filter(review=True).count()
        if art.stickposition > len(tmp_topart):
            tmp_topart.append(art)
        else:
            tmp_topart.insert(art.stickposition, art)
    # 普通文章按时间顺序
    articles = Article.objects.filter(isstick=0).order_by('-timestamp')[0:7]
    for art in articles:
        print art.artrely.count()
        art.relycount = art.artrely.filter(review=True).count()
    #最新文章评论
    art_rely = ArticleRely.objects.filter(commentid=None).filter(review=True).order_by('-timestamp')[0:6]

    #搜索
    search = None
    art_like = None
    if request.GET.get('keywords'):
        isok = True
        if request.session.get('searchtime', None) == None:
            request.session['searchtime'] = int(time.time())
            print  request.session.get('searchtime', None) , 'asdfa'
        elif int(time.time())-request.session.get('searchtime', int(time.time())) < 5:
            print  request.session.get('searchtime', None) , 'asdf'
            isok = False
        else:
            print  request.session.get('searchtime', None) , 'asdfdd'
            request.session['searchtime'] = int(time.time())
        print time.time()
        if isok:
            keywords = request.GET.get('keywords')
            print 'keywords:',keywords
            # 类似文章
            taglist = arttagstolist(keywords)
            if len(taglist) == 1:
                art_like = Article.objects.filter(title__contains=taglist[0])
            elif len(taglist) == 2:
                art_like = Article.objects.filter(Q(title__contains=taglist[0]) | Q(title__contains=taglist[1]))
            elif len(taglist) == 3:
                art_like = Article.objects.filter(
                    Q(title__contains=taglist[0]) | Q(title__contains=taglist[1]) | Q(title__contains=taglist[2]))
            elif len(taglist) == 4:
                art_like = Article.objects.filter(
                    Q(title__contains=taglist[0]) | Q(title__contains=taglist[1]) | Q(title__contains=taglist[2]) | Q(
                        title__contains=taglist[3]))
            elif len(taglist) == 5:  # 最多支持五个标签模糊查找 类似文章
                art_like = Article.objects.filter(
                    Q(title__contains=taglist[0]) | Q(title__contains=taglist[1]) | Q(title__contains=taglist[2]) | Q(
                        title__contains=taglist[3]) | Q(title__contains=taglist[4]))
            else:
                art_like = Article.objects.filter(title__contains=art.title).values('id', 'title')
            if art_like :
                for art in art_like:
                    print art.artrely.count()
                    art.relycount = art.artrely.count()
            else:
                search = '未搜索到与【<span style="color: #FF5722;">' + request.GET.get(u'keywords')  +'</span>】有关的文章，随便看看吧！'
        else:
            search = '休息一会儿再搜索吧'
    # 随机文章
    art_random = Article.objects.order_by('?').values('id', 'title')[:6]
    return render(request, 'article.html', {
        'announcement': announcement,
        'articles': articles,
        "topart": tmp_topart,
        'art_like': art_like,
        'search': search,
        'art_rely':art_rely,
        'art_random': art_random,
        'art_cate': art_cate,
        "websiteinfo": websiteinfo,
        'protagonist': protagonist,
        'timeline': timeline,
        'ads': ads,
        'user': user,
    })

#时光线 时间线
def timeline(request):
    user = auth_user(request)

    # 网站信息
    websiteinfo = None
    websiteinfo_num = Websiteinfo.objects.count()
    if websiteinfo_num > 0:
        websiteinfo = Websiteinfo.objects.get()
    year = 2017
    nowyear = int(time.strftime('%Y', time.localtime(time.time())))
    timelines = []
    while (year <= nowyear):
        timelines.append(list(TimeLine.objects.filter(year=year).order_by('-timestamp')))
        nowyear = nowyear - 1
    return render(request, 'timeline.html', {
        'timelines':timelines,
        'websiteinfo': websiteinfo,
        'user': user,
    })



#文章内容展示页
def detail(request, aid):
    user = auth_user(request)

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
    #文章回复
    art_rely = ArticleRely.objects.filter(artid=aid).filter(review=True)
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
    # 广告
    ads = Ad.objects.all()
    return render(request, 'detail.html',{
        'count': PageView.objects.count(),
        'art': art,
        'art_rely': art_rely,
        "websiteinfo": websiteinfo,
        'protagonist': protagonist,
        'art_cate': art_cate,
        'art_like': art_like[0:4],
        'art_random': art_random,
        'ads': ads,
        'user': user,
    })

def about(request):
    user = auth_user(request)

    # 网站信息
    websiteinfo = None
    websiteinfo_num = Websiteinfo.objects.count()
    guestbook = GuestBook.objects.filter(messagerely=None).filter(review=True)
    if websiteinfo_num > 0:
        websiteinfo = Websiteinfo.objects.get()
    return render(request, 'about.html',{
        'websiteinfo': websiteinfo,
        'guestbook': guestbook,
        'user': user,
    })

#分享页面
def share(request):
    user = auth_user(request)

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
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        shares = Share.objects.all()[:7]
        pass
    return render(request, 'resource.html', {
        'websiteinfo': websiteinfo,
        'shares': shares,
        'protagonist': protagonist,
        'user': user,
    })


def messagenext(request):
    guestbook = GuestBook.objects.all()[7:14]
    return JsonResponse({'Success':True, guestbook:guestbook})

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
            start = (currentIndex-1)*pagesize
            end = currentIndex*pagesize
        print "currentIndex", currentIndex
        art = Article.objects.filter(isstick=0).order_by('-timestamp')[start:end]
        art_count = Article.objects.filter(isstick=0).count()
        if art_count%pagesize != 0:
            art_count = art_count/pagesize+ 1
        else:
            art_count = art_count / pagesize
        response_data = {}
        response_data['Data'] = articlecode(art)
        response_data['Success'] = True
        response_data['SubCode'] = art_count
        return JsonResponse(response_data)
    else:
        return JsonResponse({'Success':False})

#文章评论
def articlerely(request):
    if request.method == 'POST':
        #提交间隔判断
        if submit_verification(request) == False:
            return JsonResponse({'Success': False, 'message': u'着什么急'})
        req_data = json.loads(request.body.decode())
        try:
            artid = req_data.get('artid', None)
            art_rely = req_data.get('art_rely', None)
            content = req_data['content']
            name = req_data['name']
            email = req_data['email']
            website = req_data.get('website', None)
            if email.strip() == ''or content.strip() == '':
                raise  KeyError
        except KeyError:  # 获取数据 不完整时 ，返回错误
            return JsonResponse({'Success': False, 'message': u'你是否漏了什么重要的东西'})
        if artid != None and content != None:
            response_data = {}
            response_data['Success'] = True
            openid = request.session.get('openid', None)
            user = None
            try:

                if request.session.get('logout',None) == False or request.session.get('logout',None) == None:
                    user = Socialuser.objects.get(qqopenid=openid)
                    response_data['avatar'] = user.photo
                    user.email = email
                    if website != None:
                        user.website = website
                    user.save()
                else:
                    raise Socialuser.DoesNotExist
            except Socialuser.DoesNotExist:
                if request.session.get('avatar', None):
                    response_data['avatar'] = request.session.get('avatar', None)
                else:
                    avatar = settings.STATIC_URL + 'avatar/' + str(random.randint(1, 19)) + '.png'
                    request.session['avatar'] = avatar
                    response_data['avatar'] = avatar
            request.session['name'] = name
            request.session['email'] = email
            if website!= None and website != '':
                request.session['website'] = website
            response_data['content'] = content
            response_data['website'] = website
            response_data['name'] = name
            response_data['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if artid == 0:
                art = None
            else:
                art = Article()
                art.id = int(artid)
            if user != None:
                responder = ArticleRely.objects.create(content=content, artid=art, socialuser = user,
                                           photo=response_data['avatar'], commentid_id=art_rely)
                responder.name = name
                print '社交用户回复成功'
            else:
                responder = ArticleRely.objects.create(content=content, artid=art, name=name, email=email, website=website,
                                           photo=response_data['avatar'], commentid_id=art_rely)
                print '游客用户回复成功'
            response_data['id'] = responder.id
            #发送邮件通知
            # commentator = None
            # try:
            #     if art_rely != None:
            #         commentator = ArticleRely.objects.get(id=art_rely)
            # except ArticleRely.DoesNotExist:
            #     pass
            # mail_notice = Sendmail()
            # mail_notice.sendmail(0,commentator, responder, artid)
            return JsonResponse(response_data)

    return JsonResponse({'Success': False})

#网站留言
def message(request):
    if request.method == 'POST':
        if submit_verification(request) == False:
            return JsonResponse({'Success': False, 'message': u'着什么急'})
        req_data = json.loads(request.body.decode())
        try:
            message_reply_id = req_data.get('id',None)
            name = req_data['name']
            content = req_data['content']
            email = req_data['email']
            website = req_data.get('website', None)
            if email.strip() == '' or content.strip() == '':
                raise  KeyError
        except KeyError:  # 获取数据 不完整时 ，返回错误
            print '网站留言，提交数据不完整', req_data
            return JsonResponse({'Success': False, 'message': u'你是否漏了什么重要的东西'})
        if website != None and website != '':
            if website[:7] != 'http://':
                website = 'http://' + website
        user = None
        openid = request.session.get('openid', None)
        try:
            if openid != None:
                user = Socialuser.objects.get(qqopenid=str(request.session.get('openid', None)))
                user.email = email
                user.website = website
                user.save()
            else:
                print '非社交互联用户'
        except Socialuser.DoesNotExist:
            print '没此用户'
            pass
        avatar = None
        #qq互联登陆用户
        if openid != None and request.session.get('logout', None) != True:
            response_data = {}
            #此情况是在管理员在后台把此用户信息删除，但session里面还有此用户openid
            if user != None:
                avatar = user.photo
            else:
                avatar = settings.STATIC_URL + 'avatar/' + str(random.randint(1, 19)) + '.png'
        #如果 avatar == None 那是就不是互联用户，再判断是否session里面有他的提交时头像的记录，没有就随机生成
        if avatar == None:
            if request.session.get('avatar', None) == None:
                avatar = settings.STATIC_URL + 'avatar/' + str(random.randint(1, 19)) + '.png'
            else:
                avatar = request.session.get('avatar')
        responder_guestbook = GuestBook.objects.create(message=content, name=name, email=email, messagerely_id= message_reply_id, website=website, avatar=avatar)
        print name + '留言,成功,回复ID:', message_reply_id
        response_data = {}
        response_data['Success'] = True
        response_data['id'] = responder_guestbook.id
        response_data['name'] = name
        response_data['email'] = email
        response_data['website'] = website
        response_data['avatar'] = avatar
        response_data['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #把记录放入session
        request.session['name'] = name
        request.session['email'] = email
        request.session['website'] = website
        request.session['avatar'] = avatar
        #发送邮件通知
        # commentator = None
        # try:
        #     if message_reply_id != None:
        #         commentator_guestbook = GuestBook.objects.get(id=message_reply_id)
        #         commentator = ArticleRely()
        #         commentator.id = commentator_guestbook.id
        #         commentator.name = commentator_guestbook.name
        #         commentator.email = commentator_guestbook.email
        #         commentator.content = commentator_guestbook.message
        # except ArticleRely.DoesNotExist:
        #     pass
        # mail_notice = Sendmail()
        # if mail_notice.host != '':
        #     responder = ArticleRely()
        #     responder.name = responder_guestbook.name
        #     responder.id = responder_guestbook.id
        #     responder.content = responder_guestbook.message
        #     mail_notice.sendmail(1, commentator, responder)
        return JsonResponse(response_data)
    return JsonResponse({'Success': False})

def codeqq(request):

    openid = request.session.get('openid', None)
    try:
        com_qq = Socialaccount.objects.get(company='qq')
    except Socialaccount.DoesNotExist:
        return http.HttpResponseRedirect('/404')
    qq = Qq(com_qq)
    if openid == None or openid == '':
        qqurl = qq.get_code_url('test')
        print 'qqurl:', qqurl
        return http.HttpResponseRedirect(qqurl)
    else:
        try:
            user = Socialuser.objects.get(qqopenid=str(openid))
        except Socialuser.DoesNotExist:
            qqurl = qq.get_code_url('test')
            print 'qqurl:', qqurl
            request.session['logout'] = False
            print '登陆状态更新为True'
            return http.HttpResponseRedirect(qqurl)

        expires_in = request.session.get('expires_in', None)
        #判断 accesstoken 是否过期 否则自动续期
        if expires_in < int(time.time()):
            user = qq.refresh_get_token(user.refresh_token, user)
            request.session['expires_in'] = user.expires_in
            request.session['accesstoken'] = user.access_token

        data = qq.get_user_info(user.access_token, user.qqopenid)
        user.photo = data.get('figureurl_qq_1') #QQ头像40*40
        user.name = data.get('nickname')
        print 'gender:', data.get('gender'), 'type():', type(data.get('gender'))
        if data.get('gender') == u'男':
            print u'u男'
        if data.get('gender') == '男':
            user.sex = 1
        else:
            user.sex = 0
        user.save()
        if request.session.get('logout', None) == True:
            request.session['logout'] = False
            print '登陆状态更新为True'
        return http.HttpResponseRedirect('/')

def qq(request):
    com_qq = Socialaccount.objects.get(company='qq')
    qq = Qq(com_qq)

    code = qq.get_code(request)
    print 'code', code
    socialuser = qq.get_token(code)
    if socialuser == None:
        print '返回用户为空'
    print socialuser
    openid = qq.get_openid(socialuser.access_token)
    request.session['openid'] = openid
    print 'qq:', openid
    data = qq.get_user_info(socialuser.access_token, openid)
    request.session['accesstoken'] = socialuser.access_token
    request.session['expires_in'] = socialuser.expires_in
    user = None
    try:
        user = Socialuser.objects.get(qqopenid=openid)
        socialuser.id = user.id
    except Socialuser.DoesNotExist:
        print '新用户登陆'
    if user == None:
        user = Socialuser()
    socialuser.name = data.get('nickname')
    socialuser.city = data.get('city')
    socialuser.photo = data.get('figureurl_qq_1')
    socialuser.qqopenid = openid
    print 'province:', data.get('province')
    if data.get('gender') == u'男':
        socialuser.sex = 1
    else:
        socialuser.sex = 0
    print 'gender:', data.get('gender')
    socialuser.save()

    return http.HttpResponseRedirect('/')

def logout(request):
    if request.method == 'POST':
        request.session['logout'] = True
        dict_tmp = {}
        dict_tmp['error'] = 0
        return JsonResponse(dict_tmp)
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

def page_not_found(request):
    return render(request, '404.html')

def auth_user(request):
    if request.user.id != None:
        user = Socialuser()
        try:
            webinfo = Websiteinfo.objects.get()
            user.uploadphoto = webinfo.photo
            user.name = webinfo.title
            user.email = request.user.email
            user.website = ''
        except Websiteinfo.DoesNotExist:
            user = None
        return user
    if request.session.get('logout', None) == True:
        user = Socialuser()
        user.name = request.session.get('name', '')
        user.email = request.session.get('email', '')
        user.website = request.session.get('website', '')
        user.uploadphoto = request.session.get('avatar', '')
        return user
    openid = request.session.get('openid', None)
    user = None
    if openid != None:
        com_qq = Socialaccount.objects.get(company='qq')
        if com_qq == None:
            return http.HttpResponseRedirect('/404')
        qq = Qq(com_qq)
        print 'qq号:', openid, type(openid)
        try:
            user = Socialuser.objects.get(qqopenid=str(openid))

            expires_in = request.session.get('expires_in', None)
            # 判断 accesstoken 是否过期 否则自动续期
            if expires_in < int(time.time()):
                user = qq.refresh_get_token(user.refresh_token, user)
                request.session['expires_in'] = user.expires_in
                request.session['accesstoken'] = user.access_token
                data = qq.get_user_info(user.access_token, user.openid)
                user.photo = data.get('figureurl_qq_1')  # QQ头像40*40
                user.name = data.get('nickname')
                print 'gender:', data.get('gender'), 'type():', type(data.get('gender'))
                if data.get('gender') == u'男':
                    print u'u男'
                if data.get('gender') == '男':
                    user.sex = 1
                else:
                    user.sex = 0
                user.save()
        except Socialuser.DoesNotExist:
            print '查询qqopenid为空'
    if user == None:
        user = Socialuser()
        user.name = request.session.get('name', '')
        user.email = request.session.get('email', '')
        user.website = request.session.get('website', '')
        user.uploadphoto = request.session.get('avatar', '')
    return user

def submit_verification(request):
    if request.session.get('submit_time', None) == None:
        request.session['submit_time'] = int(time.time())
        return True
    else:
        if int(time.time()) - request.session.get('submit_time', 0) < 10:
            request.session['submit_time'] = int(time.time())
            return False
        else:
            request.session['submit_time'] = int(time.time())
            return True