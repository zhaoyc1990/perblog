# coding=utf-8
from django.db import models
import time
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
	tags = models.CharField('文章标签', max_length=120, null=True, blank=True)
	abstract = models.CharField('摘要', max_length=300,blank=True, null=True)
	content = models.TextField('文章内容', default=None)
	img  = models.ImageField('文章可观性图片', upload_to='static/article/Thumbnails/', default='static/article/Thumbnails/no-img.jpg')
	pageviews = models.IntegerField('文章浏览量', default=0)
	likes = models.PositiveIntegerField('点赞数', default=0)
	relycount = models.PositiveIntegerField('回复量', default=0) #临时字段不需要数据库操作
	isstick   = models.IntegerField('是否顶置',default=0) #0为普通, 1为置顶
	stickposition = models.IntegerField('置顶位置',default=0) #以十的余数,最多十个置顶
	timemodify = models.DateTimeField(auto_now=True)  # 修改时间
	timestamp = models.DateTimeField(auto_now_add=True)  # 创建时间
	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title

class AccessBy(models.Model):
	ip = models.GenericIPAddressField('访问者ip')
	count = models.IntegerField('该IP访问次数')

#文章评论及评论回复
class ArticleRely(models.Model):
	artid = models.ForeignKey(Article,related_name='artrely',verbose_name='评论文章')
	commentid = models.ForeignKey('self',related_name='arirely', verbose_name='回复id',blank=True, null=True)
	commentip = models.ForeignKey(AccessBy, related_name='artrely', verbose_name='回复ip', blank=True, null=True)
	name = models.CharField('评论者名称', max_length=50)  # 评论者名称
	email = models.CharField('评论者邮箱', max_length=80, default=None)
	content = models.TextField('评论内容', max_length=500)
	timemodify = models.DateTimeField(auto_now=True)  # 修改时间
	timestamp = models.DateTimeField(auto_now_add=True)  # 创建时间

	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name

#时光线
class TimeLine(models.Model):
	year = models.PositiveIntegerField('年',null=True, blank=True)
	month = models.PositiveIntegerField('月',null=True, blank=True)
	content = models.CharField('内容',max_length=200)
	timestamp = models.DateTimeField(auto_now_add=True)  # 创建时间

	def __unicode__(self):
		return self.content
	def __str__(self):
		return self.content
	def save(self, *args, **kwargs):
		print '创建时间:', self.timestamp
		print '年:',time.strftime('%Y', time.localtime(time.time()))
		print '月:',time.strftime('%m', time.localtime(time.time()))
		self.year = time.strftime('%Y', time.localtime(time.time()))
		self.month = time.strftime('%m', time.localtime(time.time()))
		super(TimeLine, self).save(*args, **kwargs)