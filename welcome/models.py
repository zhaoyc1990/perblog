# coding=utf-8
from django.db import models
from django_thumbs.db.models import ImageWithThumbsField
import time, os, datetime, uuid
# Create your models here.

class PageView(models.Model):
	hostname = models.CharField(max_length=32)
	timestamp = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.__str__
	def __str__(self):
		return self.hostname
	class Meta:
		verbose_name_plural = verbose_name = '没用'

class GuestBook(models.Model):
	messagerely = models.ForeignKey('self', related_name='relymessage', verbose_name='回复id', blank=True, null=True)
	avatar = models.CharField('头像', max_length=200, default='/static/images/Logo_40.png')
	name = models.CharField('留言者名称', max_length=50)              #留言者名称
	email = models.CharField('留言者邮箱', max_length=80,default=None)
	message = models.TextField('留言内容', max_length=500)
	website = models.CharField('网站地址', max_length=200,blank=True, null=True)
	timemodify = models.DateTimeField(auto_now=True)    #修改时间
	timestamp = models.DateTimeField(auto_now_add=True)	#创建时间

	def __unicode__(self):
		return self.__str__
	def __str__(self):
		return self.name
	def replypeople(self):
		return self.relymessage.all()
	class Meta:
		verbose_name_plural = verbose_name = '网站留言'

class Announcement(models.Model):
	content = models.CharField('网站公告', max_length=100)
	timemodify = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)  # 创建时间

	def __str__(self):
		return self.content
	class Meta:
		verbose_name_plural = verbose_name = '网站公告'

class ArticleCategory(models.Model):
	name = models.CharField('类型名称', max_length=50)
	timemodify = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)  # 创建时间

	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = verbose_name = '文章类别'

#文章简介缩略图路径
def generate_filename(instance, filename):
	"""
	安全考虑，生成随机文件名
	:param instance:
	:param filename:
	:return:
	"""
	directory_name = datetime.datetime.now().strftime('static/article/Thumbnails/%Y/%m/%d')
	filename = uuid.uuid4().hex + os.path.splitext(filename)[-1]
	return os.path.join(directory_name, filename)

class Article(models.Model):
	category = models.ForeignKey(ArticleCategory,related_name='articale',verbose_name='文章类别')
	title = models.CharField('文章名称', max_length=100)
	tags = models.CharField('文章标签', max_length=120, null=True, blank=True)
	abstract = models.CharField('摘要', max_length=300,blank=True, null=True)
	content = models.TextField('文章内容', default=None)
	img  = ImageWithThumbsField('文章可观性图片', upload_to=generate_filename, default='static/article/Thumbnails/no-img.jpg', sizes=((138,53),))
	webimg = models.CharField('网络图片用于文章可观性图片', max_length=200, default='/static/article/Thumbnails/no-img.jpg')
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
	class Meta:
		verbose_name_plural = verbose_name = '文章'

class AccessBy(models.Model):
	ip = models.GenericIPAddressField('访问者ip')
	count = models.IntegerField('该IP访问次数')
	class Meta:
		verbose_name_plural = verbose_name = 'IP记录'

#文章评论及评论回复
class ArticleRely(models.Model):
	artid = models.ForeignKey(Article,related_name='artrely',verbose_name='评论文章', blank=True, null=True)
	commentid = models.ForeignKey('self',related_name='arirely', verbose_name='回复id',blank=True, null=True)
	commentip = models.ForeignKey(AccessBy, related_name='artrely', verbose_name='回复ip', blank=True, null=True)
	photo = models.CharField('随机头像',max_length=100, blank=True, null=True)
	name = models.CharField('评论者名称', max_length=50)  # 评论者名称
	email = models.CharField('评论者邮箱', max_length=80, blank=True, null=True)
	content = models.TextField('评论内容', max_length=500)
	timemodify = models.DateTimeField(auto_now=True)  # 修改时间
	timestamp = models.DateTimeField(auto_now_add=True)  # 创建时间

	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = verbose_name = '文章评论及评论回复'

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
	class Meta:
		verbose_name_plural = verbose_name = '时光线'

#博主信息
class Protagonist(models.Model):
	protagonist_sex = (
		(0,'女'),
		(1,'男'),
	)

	name = models.CharField('姓名',max_length=20)
	photo = ImageWithThumbsField('头像',upload_to=generate_filename, default='static/article/Thumbnails/no-img.jpg', sizes=((100,100),))
	webimg = models.CharField('网络图片头像', max_length=200, default='/static/article/Thumbnails/no-img.jpg')
	sex = models.IntegerField(choices=protagonist_sex, verbose_name='性别', null=True)
	career = models.CharField('职业', max_length=30)
	location = models.CharField('地理位置', max_length=100, help_text='省-市')
	githubnum = models.CharField('github.com帐号', max_length=100, blank=True, null=True)
	email = models.EmailField('邮箱地址', max_length=100, blank=True, null=True),
	qqnum = models.CharField('QQ帐号', max_length=20, blank=True, null=True)
	sinanum = models.CharField('新浪微博帐号', max_length=50, blank=True,null=True)
	twitter = models.CharField('twitter帐号', max_length=50, blank=True, null=True)
	selfinfo = models.TextField('个人介绍')
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = verbose_name = '博主信息'

#网站信息
class Websiteinfo(models.Model):
	title = models.CharField('网站名称', max_length=200)
	info = models.CharField('网站简介', max_length=200, blank=True, null=True)
	photo = ImageWithThumbsField('网站图标', upload_to=generate_filename, sizes=((40,40),) )
	casenum = models.CharField('备案号', max_length=50, help_text='没有，不写', blank=True, null=True)
	bottom = models.TextField('底部', default='Copyright©2017赵彦昌博客Design By LY')
	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title
	class Meta:
		verbose_name_plural = verbose_name = '网站信息'

class Links(models.Model):
	title = models.CharField('名字', max_length=50)
	link = models.CharField('超连接', max_length=100)
	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title
	class Meta:
		verbose_name_plural = verbose_name = '友情链接'