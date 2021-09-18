# post/urls.py
from django.urls import path
from .views import post_list, post_details, author_details, author_list, add_post, create_p, add_autor, create_a

app_name = 'posts'
urlpatterns = [
   path('', post_list,),
   path('<int:p>', post_details, name = 'details'),
   path('author_details/<int:a>', author_details, name = 'details_a'),
   path('author_list', author_list),
   path('add_post', add_post),
   path('add_autor', add_autor),
   path('create_p', create_p),
   path('create_a', create_a),
   ]
