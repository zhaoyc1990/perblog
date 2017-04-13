# coding:utf-8
from django.contrib import admin

from .models import PageView, GuestBook, Announcement, Article, ArticleCategory, ArticleRely, AccessBy
from .models import TimeLine
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )

class PageViewAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'timestamp']

admin.site.register(PageView, PageViewAdmin)
admin.site.register(GuestBook)
admin.site.register(Announcement)
#admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)
admin.site.register(ArticleRely)
admin.site.register(AccessBy)
admin.site.register(TimeLine)