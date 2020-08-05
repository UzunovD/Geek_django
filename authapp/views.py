from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, \
    ShopUserUpdateForm, ShopUserPasswordChangeForm, ShopUserProfileUpdateForm
# from authapp.models import ShopUser
from authapp.models import ShopUser, ShopUserProfile


def register(request):
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
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
    activate_message = ''
    next = request.GET['next'] if 'next' in request.GET.keys() else ''
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST or None)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                if 'next' in request.POST.keys():
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('main:index'))
    else:
        if 'auth/register' in request.META.get('HTTP_REFERER', ''):
            activate_message = f'A confirmation email was sent to your e-mail \
            address. To log in, click the link in the email.'
        form = ShopUserLoginForm()
    context = {
        'title': 'Sign in the system',
        'form': form,
        'next': next,
        'activate_message': activate_message,
    }
    return render(request, 'authapp/login.html', context)


@login_required
def update(request):
    if request.method == 'POST':
        form = ShopUserUpdateForm(request.POST, request.FILES,
                                  instance=request.user)
        profile_form = ShopUserProfileUpdateForm(request.POST,
            instance=request.user.shopuserprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            # profile_form.save()
            # костомизировал - подтверждение успешного изменения #
            context = {
                'title': 'Chenge personal data',
                'form': form,
                'profile_form': profile_form,
                'confirmation': 'Changed successfully'
            }
            return render(request, 'authapp/update.html', context)
    else:
        form = ShopUserUpdateForm(instance=request.user)
        profile_form = ShopUserProfileUpdateForm(
            instance=request.user.shopuserprofile)
    context = {
        'title': 'Chenge personal data',
        'form': form,
        'profile_form': profile_form,
    }
    return render(request, 'authapp/update.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def pass_change(request):
    if request.method == 'POST':
        form = ShopUserPasswordChangeForm(data=request.POST or None,
                                          user=request.user)
        if form.is_valid():
            form.save()
            auth.update_session_auth_hash(request,
                                          form.user)  # сохраняем текущую сессию
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


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not \
                user.is_activation_key_expired():
            user.is_active = True
            user.activation_key = ''
            user.save()
            auth.login(request, user,
                       backend='django.contrib.auth.backends.ModelBackend')
        else:
            print(f'Error activation user {user.username}')
        return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'Error activation user: {e.args}')
        return HttpResponseRedirect(reverse('main:index'))

@receiver(post_save, sender=ShopUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ShopUserProfile.objects.create(user=instance)
    else:
        instance.shopuserprofile.save()
