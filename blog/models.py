# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User)
    title = models.CharField(max_length=500)
    content=models.TextField()
    img=models.ImageField(upload_to='blog_img/')
    is_piblished=models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user=models.ForeignKey(User)
    post=models.ForeignKey(Post, null=True)
    comment_text=models.CharField(max_length=500)
    date=models.DateTimeField(auto_now=True,auto_now_add=False)


    def __str__(self):
        return self.comment_text

