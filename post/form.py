from django import forms
from post.models import Author, Posts

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nick', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'author_id']