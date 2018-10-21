from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Post,Profile,Neighbourhood,Business,Join,Comments
from django.contrib import messages
from . forms import ProfileForm,BusinessForm,PostForm,CreateHoodForm,CommentForm
from django.contrib.auth.models import User

# Create your views here.
def hood(request):
    hoods = Neighbourhood.objects.all()
    business = Business.objects.all()
    posts = Post.objects.all()

    return render(request,'hood.html',locals())