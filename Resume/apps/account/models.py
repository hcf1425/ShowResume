from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone = models.CharField('phone number', max_length=11)
    avatar = models.CharField("user's avatar", max_length=255)
    wx_openid = models.CharField('openid of wechat user', max_length=64, blank=True)
    nickname = models.CharField('nickname', max_length=255, blank=True)

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name