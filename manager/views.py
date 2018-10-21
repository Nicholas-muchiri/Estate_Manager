from django.shortcuts import render

# Create your views here.
def home(request):
    hoods = Neighbourhood.objects.all()
    business = Business.objects.all()
    posts = Post.objects.all()

    return render(request,'hood.html',locals())