# coding:utf-8
from django.contrib import admin

from .models import PageView, GuestBook, Announcement

# Register your models here.


class PageViewAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'timestamp']

admin.site.register(PageView, PageViewAdmin)
admin.site.register(GuestBook)
admin.site.register(Announcement)