from django.shortcuts import render
from .models import blogpost
# Create your views here.

def index(request):
    mypost = blogpost.objects.all()
    return render(request,'Blog/index.html',{"mypost":mypost})

def Blogpost(request,id):
    post = blogpost.objects.filter(post_id=id)[0]
    return render(request,'Blog/Blogpost.html',{"post":post})