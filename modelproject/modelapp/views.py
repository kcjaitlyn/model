from django.shortcuts import render
from .models import Article

# Create your views here.
def home(request):
    article = Article.objects
    return render(request,'home.html',{'article':article})

def home(request):
    blog = Blog.objects
    return render(request,'home.html',{'blog':blog})