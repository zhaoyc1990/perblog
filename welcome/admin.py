# coding:utf-8
from django.contrib import admin

from .models import PageView, GuestBook, Announcement, Article, ArticleCategory, ArticleRely, AccessBy
from .models import TimeLine, Protagonist, Websiteinfo, Links, Share, ShareCategory, Ad, Socialaccount, Socialuser
from .models import Smtpmail
from project.sendmail import Sendmail
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
    list_display = ['getname', 'email', 'content', 'review', 'emailsend', 'timestamp']
    actions = ['make_review']
    def make_review(self, request, queryset):
        for rely in queryset:
            print rely
            #如果是给博主留言就pass
            if rely.commentid == None:
                rely.review = True
            else:
                try:
                    if rely.socialuser != None:
                        rely.name = rely.socialuser.name
                        rely.emal = rely.socialuser.email
                    if rely.commentid.socialuser != None:
                        rely.commentid.name = rely.commentid.socialuser.name
                        rely.commentid.emal = rely.commentid.socialuser.email
                    mail_notice = Sendmail()
                    if mail_notice.sendmail(0, rely.commentid, rely, rely.artid.id):
                        rely.emailsend = True
                    else:
                        print u'留言邮件没发送成功'
                except Exception, e:
                    print  u'留言邮件没发送成功:', e
                rely.review = True
            rely.save()
    make_review.short_description = "审核通过"

class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'review', 'emailsend', 'timestamp']
    actions = ['make_review']
    def make_review(self, request, queryset):
        for rely in queryset:
            print rely
            print rely.messagerely
            #如果是给博主留言就pass
            if rely.messagerely == None:
                rely.review = True
            else:
                try:
                    if rely.messagerely.email != None or rely.messagerely.email != '':
                        commentator = ArticleRely()
                        commentator.id = rely.messagerely.id
                        commentator.name = rely.messagerely.name
                        commentator.email = rely.messagerely.email
                        commentator.content = rely.messagerely.message
                        responder = ArticleRely()
                        responder.id = rely.id
                        responder.name = rely.name
                        responder.email = rely.email
                        responder.content = rely.message
                        mail_notice = Sendmail()
                        if mail_notice.sendmail(1, commentator, responder):
                            rely.emailsend = True
                        else:
                            print u'留言邮件没发送成功'
                except Exception, e:
                    print  u'留言邮件没发送成功:', e
                rely.review = True
            rely.save()
    make_review.short_description = "审核通过"

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