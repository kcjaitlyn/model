from django.shortcuts import render
from .models import Article

# Create your views here.
def home(request):
    article = Article.objects
    return render(request,'home.html',{'article':article})