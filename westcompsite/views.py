from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from .forms import PostForm


# Create your views here.

def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                auth.login(request, user)
                print("User is valid, active and authenticated")
                return redirect('post_new')
            else:
                print("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            print("The username and password were incorrect.")
    return render(request, 'westcompsite/page_login.html', {})


def post_list(request):
    return render(request, 'westcompsite/post_list.html', {})


def post_new(request):
    def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('post_new', pk=post.pk)
        return render(request, 'westcompsite/post_edit.html', {'form': form})
