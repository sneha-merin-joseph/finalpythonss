from django.shortcuts import render
from  . models import Place
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import Movie
from . models import Review

from .forms import MovieForm
from django.http import HttpResponse

# Create your views here.

def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})


##################################
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('film')
        else:
            messages.info(request,"invalid information")
            return redirect('login')
    return render (request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password = request.POST['password']
        cpassword =request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,last_name=last_name, email=email)
                user.save();
                return redirect('login')

        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('login')
    return render(request,"register.html")


def film(request):
    return render(request,"film.html")

def  logout(request):
    auth.logout(request)
    return redirect('/')


# def detail(request):
    # if request.method=="POST":
    #     name = request.POST.get('name', )
    #     desc = request.POST.get('desc', )
    #     img = request.FILES['img']
    #     actors = request.POST.get('actors', )
    #     release_date = request.POST.get('release_date', )
    #     movie = Movie(name=name, desc=desc, img=img, actors=actors, release_date=release_date)
    #     movie.save()
    #     return redirect('/')
    # return render(request, 'detail.html')


def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render (request,"detail.html",{'movie':movie})
def add_movie(request):
    if request.method=="POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        img = request.FILES['img']
        actors = request.POST.get('actors', )
        release_date = request.POST.get('release_date', )
        trailer_link=request.POST.get('trailer_link',)
        movie = Movie(name=name, desc=desc, img=img, actors=actors, release_date=release_date,trailer_link=trailer_link)
        movie.save()
        return redirect('home')
    return render(request, 'add.html')
def rev(request):
    if request.method=="POST":
        review= request.POST.get('review', )
        movie = Review(review=review)
        movie.save()
        return redirect('ho')
    return render(request, 'rev.html')
def ho(request):
    movie = Review.objects.all()
    context = {
        'movie_list': movie
        }
    return render(request, 'ho.html', context)
    #     return redirect('/')

def de(request,movie_id):
    movie=Review.objects.get(id=movie_id)
    return render (request,"de.html",{'movie':movie})
def home(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
        }
    return render(request, 'home.html', context)
    #     return redirect('/')
    # return render(request, 'add.html')

# def add_movi(request):
#     if request.method=="POST":
#         name=request.POST.get('name',)
#         desc=request.POST.get('desc',)
#         year=request.POST.get('year',)
#         img=request.FILES['img']
#         movie=Movie(name=name,desc=desc,year=year,img=img)
#         movie.save()
#         return redirect('home')
#
#     return render(request, 'add.html')

# def add_movi(request):
#     if request.method=="POST":
#         name = request.POST.get('name', )
#         desc = request.POST.get('desc', )
#         img = request.FILES['img']
#         actors = request.POST.get('actors', )
#         release_date = request.POST.get('release_date', )
#         movie = Movie(name=name, desc=desc, img=img, actors=actors, release_date=release_date)
#         movie.save()
#         return redirect('/')
#
#     return render(request, 'add.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('home')
    return render(request,'delete.html')
def details(request):
    if request.method=='POST':
        review=request.POST['review']
        return redirect('film')
    return render(request, "details.html")

def det(request):
    if request.method=='POST':
        review=request.POST['review']
        return redirect('film')
    return render(request, "det.html")

def deta(request):
    if request.method=='POST':
        review=request.POST['review']
        return redirect('film')
    return render(request, "deta.html")
def review(request):
    if request.method=='POST':
        review=request.POST['review']
        return redirect('film')
    return render(request, "review.html")

def cut(request,id):
    if request.method=='POST':
        movie=Review.objects.get(id=id)
        movie.delete()
        return redirect('ho')
    return render(request,'cut.html')
