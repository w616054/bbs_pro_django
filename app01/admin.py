#encoding: utf-8
from django.contrib import admin
from app01 import models


class BBS_admin(admin.ModelAdmin):
    #list_display = ('title', 'summary', 'author', 'signature', 'view_count','created_at',)
    list_display = ('title', 'summary', 'author', 'view_count','created_at',)
    list_filter = ('created_at',)
    search_fields = ('title', 'author__user__username',) # 注意anthor不能搜索因为是外键

    # 显示另外一张表的字段, 此处是BBS表查询BBS_user表的signature字段
    def signature(self, obj):
        return obj.author.signature
    signature.short_description = 'ha' # 改列 显示的名字

# Register your models here.
# 注册自己的表，不然web admin里面看不到
admin.site.register(models.BBS, BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)
