from django.shortcuts import render

# Create your views here.
from .models import BlogPost

def blog_post_page(request, slug):
    queryset = BlogPost.objects.filter(slug=slug)
    obj = queryset.first()
    value = {"object": obj}
    return render(request, 'files/blog_post.html', value)