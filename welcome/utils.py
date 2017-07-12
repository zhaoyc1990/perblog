# coding=utf-8
from project import settings
from models import Ad
import time
def articlecode(article):
    ad = None
    artjson_data = ''
    try:
        ad = Ad.objects.get(position='top')
        artjson_data = '<div class="article shadow" >' + ad.content + '</div>'
    except Ad.DoesNotExist:
        pass
    for art in article:
        t2 = str(art.timemodify)[0:19]
        t1 = time.strptime(t2,'%Y-%m-%d %H:%M:%S')
        t = list(t1)
        localtime = time.localtime(time.time()) # 本地时间
        if t[2] == list(localtime)[2]:
            ts = str(t[0]) + '年' + str(t[1]) + '月' + str(t[2]) + '日'
        else:
            ts = str(t[0]) + '年' + str(t[1]) + '月' + str(t[2]) + '日 ' + str(t[3]+8) + ':' + str(t[4])
        if art.webimg != '':
            img = art.webimg
        else:
            img= art.img.url_138x53
        artjson_data =artjson_data + '<div class="article shadow" ><div class="article-left" ><img src=" '  + img + '" alt="' + art.title + '" / ></div><div class="article-right" ><div class ="article-title" ><a href="/detail/' +  str(art.id)  + '.html">'+art.title+'</a></div><div class="article-abstract" >' + art.abstract + '</div></div> <div class="clear" > </div><div class="article-footer" ><span> <iclass ="fa fa-clock-o" > </i> &nbsp; &nbsp;'+ ts + '</span><span class="article-author"  <i class="fa fa-user" > </i> &nbsp; &nbsp;赵彦昌 </span ><span> <i class ="fa fa-tag" > </i> &nbsp; &nbsp; <a href="#" >' + art.category.name + '</a> </span><span class="article-viewinfo" > <i class ="fa fa-eye" > </i> &nbsp;'+str(art.pageviews) +'</span><span class="article-viewinfo" > <i class="fa fa-commenting" > </i> &nbsp;'+str(art.relycount)+'</span></div></div>'
    return artjson_data

def arttagstolist(tags):
    taglist = tags.split( )
    tag_tmp = []
    for tag in taglist:
        if ',' in tag:
            for t in tag.split(','):
                if len(t) < 0:
                    continue
                tag_tmp.append(t)
        else:
            tag_tmp.append(tag)
    return tag_tmp