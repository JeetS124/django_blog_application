from django.http import Http404
from django import forms
from blog.models import Post, Comment


class BlogPostForm(forms.ModelForm):
    subtitle = forms.CharField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'post_image', 'content']


class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'post_image', 'content']

class CommentForm(forms.ModelForm):
    model = Comment
    fields = ['user', 'comment']