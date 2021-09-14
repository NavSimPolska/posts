from django.http import HttpResponse
from django.template import Context, loader
from post.models import Posts, Author

def post_list(request):
   posty = Posts.objects.all()
   t = loader.get_template("post/main.html")
   c = {"title": "Lista postów", "posty": posty}
   return HttpResponse(t.render(c))

def post_details(request, p):
   post = Posts.objects.get(id = p)
   t = loader.get_template("post/main.html")
   c = {"title": "Szczegóły posta", "post": post}
   return HttpResponse(t.render(c))

def author_list(request):
   autorzy = Author.objects.all()
   t = loader.get_template("post/author_list.html")
   c = {"title": "Lista autorów", 'autorzy': autorzy}
   return HttpResponse(t.render(c))

def author_details(request, a):
   auth = Author.objects.get(id = a)
   t = loader.get_template("post/author_details.html")
   c = {"title": "O autorze", "auth": auth}
   return HttpResponse(t.render(c))

def add_post(request):
   blank = Posts.objects.first()
   autorzy = Author.objects.all()
   t = loader.get_template("post/add_post.html")
   c = {"title": "Nowy post", "autorzy": autorzy, "blank": blank}
   return HttpResponse(t.render(c))