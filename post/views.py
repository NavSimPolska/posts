from django.http import HttpResponse
from django.template import Context, loader
from post.models import Posts, Author
from django.shortcuts import render, redirect
from post.form import AuthorForm, PostForm
from django.core.paginator import Paginator


def post_list(request):
   posty = Posts.objects.all()
   paginator = Paginator(posty, 5)
   page_number = request.GET.get('page')
   posty = paginator.get_page(page_number)
   c = {"title": "Lista postów", "posty": posty}
   return render(request, "post/main.html", c)

def post_details(request, p):
   post = Posts.objects.get(id = p)
   c = {"title": "Szczegóły posta", "post": post}
   return render(request, "post/main.html", c)

def author_list(request):
   autorzy = Author.objects.all()
   paginator = Paginator(autorzy, 5)
   page_number = request.GET.get('page')
   autorzy = paginator.get_page(page_number)
   c = {"title": "Lista autorów", 'autorzy': autorzy}
   return render(request, "post/author_list.html", c)

def author_details(request, a):
   auth = Author.objects.get(id = a)
   t = loader.get_template("post/author_details.html")
   c = {"title": "O autorze", "auth": auth}
   return HttpResponse(t.render(c))

def add_post(request):
   autorzy = Author.objects.all()
   c = {"title": "Nowy post", "autorzy": autorzy, 'form': PostForm}
   return render(request, "post/add_post.html", c)

def add_autor(request):
   autorzy = Author.objects.all()
   c = {"title": "Nowy autor", 'form': AuthorForm}
   return render(request, "post/add_autor.html", c)

def create_p(request):
   if request.method == "POST":
      dane = request.POST
      form = PostForm(dane)
      if form.is_valid():
         form.save()
   return redirect('/')

def create_a(request):
   if request.method == "POST":
      dane = request.POST
      form =AuthorForm(dane)
      if form.is_valid():
         form.save()
   return redirect('/author_list')

