from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from welcome.views import index, health, temp, home, uploadImg, timeline, detail, homenext, articlerely, message
from welcome.views import about, share, page_not_found
from django.conf.urls import handler404, handler500

import settings
from django.conf.urls.static import static
handler404 = page_not_found
urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home),
    url(r'index', index),
    url(r'^health$', health),
    url(r'^temp$', temp),
	url(r'^home', home),
    url(r'^timeline.html', timeline),
    url(r'^about', about),
    url(r'^share', share),
    url(r'^detail/(?P<aid>\d+).html/$', detail),
    url(r'^api/article/next', homenext),
    url(r'^api/article/rely', articlerely),
    url(r'^api/message', message),
    url(r'^kin/uploadImg/$', uploadImg),
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += staticfiles_urlpatterns()