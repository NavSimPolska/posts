from django.db import models

class Author(models.Model):
    nick = models.CharField(max_length=50, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=254, blank=False, unique = True, null=True)

    def __str__(self):
        return f"id:{self.id}, nick={self.nick}, email={self.email}"

class Posts(models.Model):
    title   =  models.CharField(max_length = 256, blank=True)
    content =  models.TextField(blank=True)
    created =  models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now=True)
#    author_id = models.IntegerField(null=False)
    author_id =models.ForeignKey(Author, on_delete=models.CASCADE )

    def __str__(self):
        return f"id:{self.id}, title={self.title}, content={self.content}, created={self.created}, author_id = {self.author_id}"
