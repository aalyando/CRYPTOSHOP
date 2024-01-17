from django.shortcuts import render, redirect
from djangoStore.forms import AuthenticationForm, RegisterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.urls import reverse


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('authenticated_user')
            login(request, user)
            return HttpResponseRedirect('/product/products_list/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

        return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('products_list')
