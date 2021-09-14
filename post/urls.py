# post/urls.py
from django.urls import path
from .views import post_list, post_details, author_details, author_list, add_post

app_name = 'post'
urlpatterns = [
   path('', post_list),
   path('<int:p>', post_details),
   path('author_details/<int:a>', author_details),
   path('author_list', author_list),
   path('add_post', add_post),
   ]
