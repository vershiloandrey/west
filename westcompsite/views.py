from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from .models import Note


def post_list(request):
    return render(request, 'westcompsite/post_list.html', {})


def shop(request):
    products = Note.objects.all()
    return render(request, 'westcompsite/shop.html', {'products': products})


def notes(request):
    products = Note.objects.all()
    return render(request, 'westcompsite/notes.html', {'products': products})


def pcs(request):
    products = Note.objects.all()
    return render(request, 'westcompsite/pcs.html', {'products': products})


def access(request):
    products = Note.objects.all()
    return render(request, 'westcompsite/access.html', {'products': products})


def periphery(request):
    products = Note.objects.all()
    return render(request, 'westcompsite/periphery.html', {'products': products})


def complect(request):
    products = Note.objects.all()
    return render(request, 'westcompsite/complect.html', {'products': products})


def remont(request):
    products = Note.objects.all()
    return render(request, 'westcompsite/shop.html', {'products': products})

