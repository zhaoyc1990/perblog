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
    timestamp = models.DateTimeField(auto_now_add=True) #创建时间
