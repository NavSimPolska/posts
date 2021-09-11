from django.db import models


class Posts(models.Model):
    title   =  models.CharField(max_length = 256, blank=False)
    content =  models.TextField(blank=False)
    created =  models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now=True)

class author(models.Model):
    nick = models.CharField(max_length=50, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=254, blank=False)