from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    blog = Blog.objects.all()
    return render(request, "index.html", {'blog':blog})

def blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    print(slug)
    return render(request, "blog.html", {'blog':blog})