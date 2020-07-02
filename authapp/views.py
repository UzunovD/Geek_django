from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserUpdateForm, ShopUserPasswordChangeForm

# from authapp.models import ShopUser


def register(request):
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = ShopUserRegisterForm()
    context = {
        'title': 'Registration',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


def login(request):
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = ShopUserLoginForm()
    context = {
        'title': 'Sign in the system',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)

@login_required
def update(request):
    if request.method == 'POST':
        form = ShopUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            # костомизировал - подтверждение успешного изменения #
            context = {
                'title': 'Chenge personal data',
                'form': form,
                'confirmation':'Changed successfully'
            }
            return render(request, 'authapp/update.html', context)
    else:
        form = ShopUserUpdateForm(instance=request.user)
    context = {
        'title': 'Chenge personal data',
        'form': form,
    }
    return render(request, 'authapp/update.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))

def pass_change(request):
    if request.method == 'POST':
        form = ShopUserPasswordChangeForm(data=request.POST or None, user=request.user)
        if form.is_valid():
            form.save()
            auth.update_session_auth_hash(request, form.user)  # сохраняем текущую сессию
            context = {
                'title': 'Chenge password',
                'form': form,
                'confirmation': 'Changed successfully'
            }
            return render(request, 'authapp/pass_change.html', context)
    else:
        form = ShopUserPasswordChangeForm(request.GET)
        context = {
            'title': 'Change password',
            'form': form,
        }
        return render(request, 'authapp/pass_change.html', context)
