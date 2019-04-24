from django.shortcuts import render
from .models import Post

# Create your views here.

def main(request):
    qs = Post.objects.all()

    return render(request, 'blog/main.html',{
        'qs':qs
    })
