from django.shortcuts import render, redirect
from.models import Post, Profile, Comments
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import ProfileForm, PostForm, CommentsForm


@login_required(login_url='/login')
def index(request):
    a = Post.objects.all()
    b = Profile.objects.all()
    return render (request, 'index.html', {'a':a, 'b':b})


def registration(request):

    if request.method == 'POST': 
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.info(request, 'E-mail already exists')
            return redirect('/registration')

        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken')
            return redirect('/registration')

        else:
            user=User.objects.create_user(email=email, username=username, password=password)
            user.save()
            return redirect('/')

    else:
        return render (request, 'registration.html')


def login(request):
   
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Sorry, your password was incorrect. Please double-check your password.")
            return redirect('/login')
        
    else:
        return render (request, 'login.html')  


@login_required(login_url='/login')
def logout (request):
        auth.logout(request)
        return redirect('/login')


@login_required(login_url='/login')
def profile(request): 

    if request.method == 'POST':
        
        form = ProfileForm(request.POST, request.FILES) 
        if form.is_valid():
            abc = form.save(commit=False)
            abc.user=request.user
            abc.save()
            return redirect('/profile')
    
    else:
        if Profile.objects.filter(user=request.user.id).exists():
            profile=Profile.objects.get(user=request.user.id)
            post=Post.objects.filter(user=profile.user.id)
            return render (request, 'profile.html', {'profile':profile, 'post':post})

        else:
            form = ProfileForm()
            return render (request, 'addprofile.html', {'form':form})


@login_required(login_url='/login')        
def profile2 (request, pid):
    p=Profile.objects.get(id=pid)
    a=Post.objects.filter(user=p.user)
    return render (request, 'profile2.html', { 'p':p , 'a':a} )


@login_required(login_url='/login')
def editprofile (request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user.id)
        profile2 = ProfileForm(request.POST, request.FILES, instance=profile) 
        if profile2.is_valid():
            profile2.save()
            return redirect('/profile')

    else:
        profile = Profile.objects.get(user=request.user.id)
        form = ProfileForm(instance=profile)
        return render(request, 'editprofile.html', {'form':form})


@login_required(login_url='/login')    
def addpost(request):
    
    if request.method == 'POST':

        form=PostForm(request.POST, request.FILES) 
        
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/profile')
        
    else:
        form=PostForm()
        return render (request, 'addpost.html', {'form':form})


@login_required(login_url='/login') 
def editpost (request, id):
    
    if request.method == 'POST': 
        a = Post.objects.get(id=id)
        form = PostForm(request.POST, request.FILES, instance=a)
        
        if form.is_valid():
            form.save()
            return redirect('/profile')
        
    else:
        a =Post.objects.get(id=id)
        form = PostForm(instance=a)
        return render(request, 'editpost.html', {'form':form})


@login_required(login_url='/login')   
def delete (request, id):
    
    a=Post.objects.get(id=id)
    a.delete()
    
    return redirect('/profile')


@login_required(login_url='/login')
def views(request, id):

    if request.method == "POST":
        form=CommentsForm(request.POST)
        post=Post.objects.get(id=id)
        if form.is_valid():
            abc=form.save(commit=False)
            abc.user=request.user
            abc.post=post
            abc.save()      
            return redirect (f'/views/{id}')
        
    else:
        a=Post.objects.get(id=id)
        cmt=Comments.objects.filter(post=a)
        form=CommentsForm()
        return render (request, 'views.html', {'a':a, "form":form, "cmt":cmt})


@login_required(login_url='/login')
def search(request):
        
    if request.method == 'POST': 
        searched = request.POST['searched']
        p = Profile.objects.filter(name__icontains=searched)
        return render (request, 'search.html', {'searched':searched, 'p':p,})

        
    else:  
        return render (request, 'search.html')
    
