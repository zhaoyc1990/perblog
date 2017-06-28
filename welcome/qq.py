# coding=utf-8
from models import Socialaccount, Socialuser
import urllib, urllib2, simplejson
import datetime, time

class Qq:
    scope = 'get_user_info'
    appid = None
    appkey = None
    redirect_url = None
    token_url = None
    code_url = None
    openid_url = None
    user_info_url = None
    def __init__(self, app=None):
        if app != None:
            self.appid = app.appid
            self.appkey = app.appkey
            self.code_url = app.code_url
            self.redirect_url = app.redirect_url
            self.token_url = app.token_url
        self.openid_url = 'https://graph.qq.com/oauth2.0/me'
        self.user_info_url = 'https://graph.qq.com/user/get_user_info'

    def get_code_url(self, crsf_token):
        auth_url = '%s?%s'%(self.code_url, urllib.urlencode({
                                        'response_type': 'code',
                                        'client_id': self.appid,
                                        'redirect_uri': self.redirect_url,
                                        'scope': self.scope,
                                        'state': crsf_token,
                                        }))
        return auth_url
    def get_code(self, request):
        return request.REQUEST.get('code')

    def get_token_url(self, code):
        token_url = '%s?%s' % (self.token_url, urllib.urlencode({
            'grant_type': 'authorization_code',
            'client_id': self.appid,
            'client_secret': self.appkey,
            'code': code,
            'redirect_uri': self.redirect_url,
        }))
        return token_url

    def get_token(self, code):
        token_url = self.get_token_url(code)
        print u'获取token_url:', token_url
        req = urllib2.Request(token_url)
        resp = urllib2.urlopen(req)
        content = resp.read()
        print 'content：', content
        access_token = urllib2.urlparse.parse_qs(content).get('access_token', [''])[0]
        refresh_token = urllib2.urlparse.parse_qs(content).get('refresh_token', [''])[0]
        expires_in = urllib2.urlparse.parse_qs(content).get('expires_in', [''])[0]
        print 'expires_in:', expires_in
        now_time = datetime.datetime.now()
        expires_date = now_time + datetime.timedelta(seconds=int(expires_in))
        expires_unix = int(time.mktime(expires_date.timetuple()))
        user = Socialuser()
        user.access_token = access_token
        user.refresh_token = refresh_token
        user.expires_in = expires_unix
        return user

    def get_openid_url(self, token):
        openid_url = '%s?%s' % (self.openid_url, urllib.urlencode({
            'access_token': token,
        }))
        return openid_url

    def get_openid(self, token):
        openid_url = self.get_openid_url(token)
        req = urllib2.Request(openid_url)
        resp = urllib2.urlopen(req)
        content = resp.read()
        content = content[content.find('(') + 1:content.rfind(')')]
        data = simplejson.loads(content)
        print 'get_openid:', data
        return data.get('openid')

    def get_user_info_url(self, token, openid):
        user_info_url = '%s?%s' % (self.user_info_url, urllib.urlencode({
            'access_token': token,
            'openid': openid,
            'oauth_consumer_key': self.appid
        }))
        return user_info_url
    def get_user_info(self, token, openid):
        user_info_url = self.get_user_info_url(token, openid)
        req = urllib2.Request(user_info_url)
        resp = urllib2.urlopen(req)
        content = resp.read()
        content = content[content.find('(') + 1:content.rfind(')')]
        data = simplejson.loads(content)
        print type(data)
        print data
        return data

    def get_refresh_token_url(self, refresh_token):
        refresh_token_url = '%s?%s' % (self.user_info_url, urllib.urlencode({
            'grant_type': 'refresh_token',
            'client_id': self.appid,
            'client_secret': self.appkey,
            'refresh_token': refresh_token
        }))
        return refresh_token_url
    #权限自动续期，获取Access Token
    def refresh_get_token(self, refresh_token, user):
        refresh_token_url = self.get_refresh_token_url(refresh_token)
        req = urllib2.Request(refresh_token_url)
        resp = urllib2.urlopen(req)
        content = resp.read()
        print 'content：', content
        access_token = urllib2.urlparse.parse_qs(content).get('access_token', [''])[0]
        refresh_token = urllib2.urlparse.parse_qs(content).get('refresh_token', [''])[0]
        expires_in = urllib2.urlparse.parse_qs(content).get('expires_in', [''])[0]
        print 'expires_in:', expires_in
        now_time = datetime.datetime.now()
        expires_date = now_time + datetime.timedelta(seconds=int(expires_in))
        expires_unix = int(time.mktime(expires_date.timetuple()))
        user.access_token = access_token
        user.refresh_token = refresh_token
        user.expires_in = expires_unix
        user.save()
        return user