# coding=utf-8
from django.db import models
# Create your models here.

class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)
	
class GuestBook(models.Model):
	name = models.CharField('留言者名称', max_length=50)              #留言者名称
	email = models.CharField('留言者邮箱', max_length=80,default=None)
	message = models.TextField('留言内容', max_length=500)
	timemodify = models.DateTimeField(auto_now=True)    #修改时间
	timestamp = models.DateTimeField(auto_now_add=True)	#创建时间	

	def __unicode__(self):
		return self.__str__
	def __str__(self):
		return self.name

class Announcement(models.Model):
	content = models.CharField('网站公告', max_length=100)
	timemodify = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)  # 创建时间

	def __str__(self):
		return self.content

class ArticleCategory(models.Model):
	name = models.CharField('类型名称', max_length=50)
	timemodify = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)  # 创建时间

	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name

class Article(models.Model):
	category = models.ForeignKey(ArticleCategory,related_name='articale',verbose_name='文章类别')
	title = models.CharField('文章名称', max_length=100)
	content = models.TextField('文章内容', default=None)
	img  = models.CharField('文章可观性图片', max_length=100, default='null')
	pageviews = models.IntegerField('文章浏览量')
	isstick   = models.IntegerField('是否顶置',default=0) #0为普通, 1为置顶
	stickposition = models.IntegerField('置顶位置') #以十的余数,最多十个置顶
	timemodify = models.DateTimeField(auto_now=True)  # 修改时间
	timestamp = models.DateTimeField(auto_now_add=True)  # 创建时间

class ArticleRely(models.Model):
	artid = models.ForeignKey(Article,related_name='artrely',verbose_name='评论文章')
	commentid = models.ForeignKey('self',related_name='arirely', verbose_name='回复id')
	commentip = models.ForeignKey('self', related_name='comment', verbose_name='ip')
	name = models.CharField('评论者名称', max_length=50)  # 评论者名称
	email = models.CharField('评论者邮箱', max_length=80, default=None)
	content = models.TextField('评论内容', max_length=500)
	timemodify = models.DateTimeField(auto_now=True)  # 修改时间
	timestamp = models.DateTimeField(auto_now_add=True)  # 创建时间

class AccessBy(models.Model):
	ip = models.GenericIPAddressField('访问者ip')
	count = models.IntegerField('该IP访问次数')