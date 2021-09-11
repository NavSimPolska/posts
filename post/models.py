from django.db import models

class Posts(models.Model):
    title   =  models.CharField(max_length = 256, blank=False)
    content =  models.TextField(blank=False)
    created =  models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now=True)
    author_id = models.IntegerField(null=False)

    def __str__(self):
        return f"id:{self.id}, title={self.title}, content={self.content}, created={self.created}"

    # def save(self):
    #     self.save()
    #     return


class Author(models.Model):
    nick = models.CharField(max_length=50, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=254, blank=False)

    def __str__(self):
        return f"id:{self.id}, nick={self.nick}, email={self.email}"