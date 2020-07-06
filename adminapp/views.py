from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from adminapp.forms import AdminShopUserCreateForm, AdminShopUserUpdateForm, ProductCategoryEditForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda user: user.is_superuser)
def my_admin_users(request):
    user_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser',
                                                '-is_staff', 'username')
    context = {
        'page_title': 'admin/users',
        'object_list': user_list,
    }
    return render(request, 'adminapp/users.html', context)


@user_passes_test(lambda user: user.is_superuser)
def user_create(request):
    if request.method == 'POST':
        user_form = AdminShopUserCreateForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('my_admin:users'))
    else:
        user_form = AdminShopUserCreateForm()

    context = {
        'page_title': 'users/create',
        'form': user_form
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def user_update(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user_form = AdminShopUserUpdateForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('my_admin:users'))
    else:
        user_form = AdminShopUserUpdateForm(instance=user)

    context = {
        'page_title': 'users/edit',
        'form': user_form
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('my_admin:users'))

    context = {
        'page_title': 'users/delete',
        'user_to_delete': user,
    }
    return render(request, 'adminapp/user_delete.html', context)


# @user_passes_test(lambda user: user.is_superuser)
# def user_recover(request, pk):
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         user.is_active = True
#         user.save()
#         return HttpResponseRedirect(reverse('my_admin:users'))
#
#     context = {
#         'page_title': 'users/recover',
#         'user_to_recover': user,
#     }
#     return render(request, 'adminapp/user_recover.html', context)


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
        return JsonResponse({'result': result})


@user_passes_test(lambda user: user.is_staff == True)
def categories(request):
    title = 'administration/categories'

    categories_list = ProductCategory.objects.all().order_by('-is_active', 'pk')

    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda user: user.is_staff == True)
def category_create(request):
    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('my_admin:categories'))
    else:
        category_form = ProductCategoryEditForm()

    context = {
        'page_title': 'category/create',
        'form': category_form
    }

    return render(request, 'adminapp/category_update.html', context)


@user_passes_test(lambda user: user.is_staff == True)
def category_update(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('my_admin:categories'))
    else:
        category_form = ProductCategoryEditForm(instance=category)

    context = {
        'page_title': 'users/edit',
        'form': category_form
    }

    return render(request, 'adminapp/category_update.html', context)


@user_passes_test(lambda user: user.is_staff == True)
def category_delete(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('my_admin:categories'))

    context = {
        'page_title': 'category/delete',
        'category_to_delete': category,
    }
    return render(request, 'adminapp/category_delete.html', context)


@user_passes_test(lambda user: user.is_staff == True)
def products(request, pk):
    title = 'administration/product'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', content)
