from django.db import models

# Create your models here.
# 存储手机页面
class Phone(models.Model):
    # id = models.AutoField(primary_key=True)  # Django会自动创建,并设置为主键
    phone_id = models.CharField(max_length=20)
    phone_title = models.CharField(max_length=100)
    phone_url = models.CharField(max_length=50)

# 手机评论页面
class PhoneCPages(models.Model):
    # id 自动创建
    phone_id = models.CharField(max_length=20)
    comment_page_id = models.CharField(max_length=10)
    comment_page_url = models.CharField(max_length=50)

# 手机评论内容
class PhoneCDetails(models.Model):
    # id 自动创建
    phone_id = models.CharField(max_length=20)
    comment_page_id = models.IntegerField(default=0)
    comment_page_url = models.CharField(max_length=50)
    comment_num = models.CharField(max_length=10)
    comment_detail = models.CharField(max_length=1000)
    comment_sentiments = models.IntegerField(default=0)