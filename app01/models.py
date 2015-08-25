#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# 
class BBS(models.Model):
    title = models.CharField(max_length=64)  # 标题 32个中文
    summary = models.CharField(max_length=256, blank=True,null=True)    # 概述
    content = models.TextField()    # 内容
    author = models.ForeignKey('BBS_user') # 连接BBS_user表
    view_count = models.IntegerField()  # 浏览数
    ranking = models.IntegerField()     # 排名
    created_at = models.DateTimeField() 
    updated_at = models.DateTimeField()

    def __unicode__(self):
        return self.title

# 评论表 使用django自带的
#class Comment(models.Model):


# 板块
class Category(models.Model):
    name = models.CharField(max_length=32, unique=True) # 字段唯一，但不是主键
    administrator = models.ForeignKey('BBS_user')

    def __unicode__(self):
            return self.name


# 用户
# 继承django自带的用户表，然后扩展
# 继承有2种方式：
# 1、参数里面直接继承
# 2、使用外键 (ForeignKey , OneToOneField , )
# 这里使用的外键
class BBS_user(models.Model):
    user = models.OneToOneField(User) # 继承 User
    signature = models.CharField(max_length=128, default='This guy is too lazy to leave anything here.') # 个人签名
    photo = models.ImageField(upload_to="upload_imgs/", default="upload_imgs/user-1.jpg") # 头像
    
    def __unicode__(self):
            return self.user.username

