# coding: utf-8
import smtplib
import sys
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header
from email import encoders
from welcome.models import Smtpmail, Article, Websiteinfo, ArticleRely

class Sendmail:
    mail_username = ''
    mail_password = ''
    host = ''
    port = 0
    tls = False
    def __init__(self):
        try:
            smtpmail = Smtpmail.objects.get(enabled=True)
        except Smtpmail.DoesNotExist:
            return None
        self.mail_username = smtpmail.user
        self.mail_password = smtpmail.password
        self.host = smtpmail.host
        self.port = smtpmail.port
        self.tls = smtpmail.tls

    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr(( \
            Header(name, 'utf-8').encode(), \
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    def sendmail(self, type, commentator, responder, articleid=0):
        try:
            webinfo = Websiteinfo.objects.get()
            if webinfo.websiteip[-1] != '/':
                webinfo.websiteip = webinfo.websiteip + '/'
        except Websiteinfo.DoesNotExist:
            return None

        #判断是文章评论还是留言
        if type == 0:
            try:
                article = Article.objects.get(id=int(articleid))
            except Article.DoesNotExist:
                return None
            anchor_point = [u'文章&lt;&lt;' +article.title+ '&gt;&gt;发表的评论:',u'评论', u'文章<<' + article.title +'>>']
            anchor_point_url = webinfo.websiteip + 'detail/' + str(article.id) + '.html#comment-' + str(responder.id)
        else:
            anchor_point = [u'留言板的留言:',u'留言', u'留言板']
            anchor_point_url = webinfo.websiteip + 'about#comment-' + str(responder.id)
        #给博主留言
        if commentator == None:
            msg = MIMEText('<html><body>' +
                                '<h2>您的网站<a target="_blank" href="' + webinfo.websiteip  +'">'+ webinfo.title + '</a>'+
                                '有新的' + anchor_point[1] + '啦!</h2>' +
                                '<p><b>' + responder.name + '</b>给您的<a target="_blank" href="'+ anchor_point_url +'">'+ anchor_point[0] +'</a></p>' +
                                '<p style="line-height:25px;padding:10px;background:#5c96be;border-radius:4px;color:#fff">' + responder.content + '</p>' +
                                '<p style="text-align:center">此邮件由系统自动发出，请勿回复.</p>' +
                                '</body></html>', 'html', 'utf-8')
        else:
            msg = MIMEText('<html><body>' +
                                '<h2>你在<a target="_blank" href="' + webinfo.websiteip  +'">'+ webinfo.title + '</a>' +
                                '上的' + anchor_point[1] + '有回复啦!</h2>' +
                                '<p>您好！<b>'+ commentator.name +'！</b>您曾在'+ anchor_point[0] + '</p>' +
                                '<p style="line-height:25px;padding:10px;background:#edecf2;border-radius:4px">' + commentator.content + '</p>' +
                                '<p><b>' + responder.name + '</b>给您的<a target="_blank" href="'+ anchor_point_url +'">回复</a>:</p>' +
                                '<p style="line-height:25px;padding:10px;background:#5c96be;border-radius:4px;color:#fff">' + responder.content + '</p>' +
                                '<p style="text-align:center">此邮件由系统自动发出，请勿回复.</p>' +
                                '</body></html>', 'html', 'utf-8')
        msg['From'] = self._format_addr(unicode(webinfo.title + ' <'+ self.mail_username +'>'))
        to_addr = ''
        if commentator == None:
            msg['To'] = self._format_addr(unicode(webinfo.title + ' <'+ self.mail_username +'>'))
            msg['Subject'] = Header(unicode('您网站的' + anchor_point[2] + '收到了新的' + anchor_point[1]), 'utf-8').encode()
            to_addr = self.mail_username
        else:
            msg['To'] = self._format_addr(unicode(commentator.name + ' <'+ commentator.email +'>'))
            msg['Subject'] = Header(unicode('您在【'+ webinfo.title +'】的' + anchor_point[1] + '收到了回复'), 'utf-8').encode()
            to_addr = commentator.email
        smtp = smtplib.SMTP(self.host, self.port)
        smtp.set_debuglevel(1)
        if self.tls:
            smtp.ehlo()
            smtp.starttls()
        try:
            smtp.login(self.mail_username, self.mail_password)
        except:
            print 'LOGIN ERROR ****'
        smtp.sendmail(self.mail_username, [to_addr], msg.as_string())
        smtp.quit()
        return True