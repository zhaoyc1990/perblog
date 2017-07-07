# coding:utf-8
from django.contrib import admin

from .models import PageView, GuestBook, Announcement, Article, ArticleCategory, ArticleRely, AccessBy
from .models import TimeLine, Protagonist, Websiteinfo, Links, Share, ShareCategory, Ad, Socialaccount, Socialuser
from .models import Smtpmail
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pageviews')
    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )

class PageViewAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'timestamp']

class AdAdmin(admin.ModelAdmin):
    list_display = ['advertisers', 'position']

class SmtpmailAdmin(admin.ModelAdmin):
    list_display = ['host', 'user', 'enabled']

class ArticleRelyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'content', 'review']
    list_editable = ['review', ]

class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'review']
    list_editable = ['review', ]

admin.site.register(PageView, PageViewAdmin)
admin.site.register(GuestBook, GuestBookAdmin)
admin.site.register(Announcement)
#admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)
admin.site.register(ArticleRely, ArticleRelyAdmin)
admin.site.register(AccessBy)
admin.site.register(TimeLine)
admin.site.register(Protagonist)
admin.site.register(Websiteinfo)
admin.site.register(Links)
admin.site.register(Share)
admin.site.register(ShareCategory)
admin.site.register(Ad, AdAdmin)
admin.site.register(Socialaccount)
admin.site.register(Socialuser)
admin.site.register(Smtpmail, SmtpmailAdmin)