from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from adminapp.forms import AdminShopUserCreateForm, AdminShopUserUpdateForm
from authapp.models import ShopUser


@user_passes_test(lambda user: user.is_superuser)
def my_admin_home(request):
    user_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser',
                                                '-is_staff', 'username')
    context = {
        'page_title': 'admin/users',
        'object_list': user_list,
    }
    return render(request, 'adminapp/home.html', context)


@user_passes_test(lambda user: user.is_superuser)
def user_create(request):
    if request.method == 'POST':
        user_form = AdminShopUserCreateForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('my_admin:home'))
    else:
        user_form = AdminShopUserCreateForm()

    context = {
        'page_title': 'users/create',
        'form': user_form
    }

    return render(request, 'adminapp/update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def user_update(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user_form = AdminShopUserUpdateForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('my_admin:home'))
    else:
        user_form = AdminShopUserUpdateForm(instance=user)

    context = {
        'page_title': 'users/edit',
        'form': user_form
    }

    return render(request, 'adminapp/update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('my_admin:home'))

    context = {
        'page_title': 'users/delete',
        'user_to_delete': user,
    }
    return render(request, 'adminapp/delete.html', context)


# @user_passes_test(lambda user: user.is_superuser)
# def user_recover(request, pk):
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         user.is_active = True
#         user.save()
#         return HttpResponseRedirect(reverse('my_admin:home'))
#
#     context = {
#         'page_title': 'users/recover',
#         'user_to_recover': user,
#     }
#     return render(request, 'adminapp/recover.html', context)


@user_passes_test(lambda user: user.is_superuser)
def user_recover(request, pk):
    if request.is_ajax():
        user = get_object_or_404(ShopUser, pk=int(pk))
        if request.method == 'POST':
            user.is_active = True
            user.save()

        user_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser',
                                                    '-is_staff', 'username')
        context = {
            'page_title': 'admin/users',
            'object_list': user_list,
        }
        result = render_to_string('adminapp/includes/inc__users.html', context,
                                  request=request)
        print(result)
        return JsonResponse({'result': result})

