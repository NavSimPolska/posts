from django.http import HttpResponse
from django.template import Context, loader
from post.models import Posts, Author
from django.shortcuts import render, redirect
from post.form import AddAutorsForm



def post_list(request):
   posty = Posts.objects.all()
   c = {"title": "Lista postów", "posty": posty}
   return render(request, "post/main.html", c)

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
   c = {"title": "Nowy post", "autorzy": autorzy, "blank": blank,}
   return render(request, "post/add_post.html", c)

def add_autor(request):
   autorzy = Author.objects.all()
   c = {"title": "Nowy autor", 'form': AddAutorsForm}
   return render(request, "post/add_autor.html", c)

def create_p(request):
   if request.method == "POST":
      dane = request.POST
      print(len(dane), dane)
      a = Author.objects.get(id=int(dane.get('author')))
      if dane.get('temat') != '' and dane.get('tresc') != '':
         Posts.objects.create(title=dane.get('temat'), content=dane.get('tresc'), author_id=a)
   return redirect('/')

def create_a(request):
   if request.method == "POST":
      dane = request.POST
      print(dane)
      if dane.get('temat') != '' and dane.get('tresc') != '':
         Author.objects.create(nick=dane.get('Nick'), email=dane.get('email'))
   return redirect('/author_list')

