from django.contrib.auth.decorators import user_passes_test
from django.db.models import F
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,\
    DetailView

from adminapp.forms import AdminShopUserCreateForm, AdminShopUserUpdateForm, \
    AdminProductCategoryEditForm, AdminProductEditForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


class OnlyAdminMixin:
    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class OnlyStaffMixin:
    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PageTitleMixin:
    page_title = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


# @user_passes_test(lambda user: user.is_superuser)
# def my_admin_users(request):
#     user_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser',
#                                                 '-is_staff', 'username')
#     context = {
#         'page_title': 'admin/users',
#         'object_list': user_list,
#     }
#     return render(request, 'adminapp/users.html', context)


class ShopUserListView(OnlyAdminMixin, PageTitleMixin, ListView):
    model = ShopUser
    page_title = 'admin/users'


# @user_passes_test(lambda user: user.is_superuser)
# def user_create(request):
#     if request.method == 'POST':
#         user_form = AdminShopUserCreateForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('my_admin:users'))
#     else:
#         user_form = AdminShopUserCreateForm()
#
#     context = {
#         'page_title': 'users/create',
#         'form': user_form
#     }
#
#     return render(request, 'adminapp/update.html', context)


class UserCreateView(OnlyAdminMixin, PageTitleMixin, CreateView):
    model = ShopUser
    form_class = AdminShopUserCreateForm
    page_title = 'users/create'
    success_url = reverse_lazy('my_admin:users')


# @user_passes_test(lambda user: user.is_superuser)
# def user_update(request, pk):
#     user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         user_form = AdminShopUserUpdateForm(request.POST, request.FILES,
#         instance=user)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('my_admin:users'))
#     else:
#         user_form = AdminShopUserUpdateForm(instance=user)
#
#     context = {
#         'page_title': 'users/edit',
#         'form': user_form
#     }
#
#     return render(request, 'adminapp/update.html', context)


class UserUpdateView(OnlyAdminMixin, PageTitleMixin, UpdateView):
    model = ShopUser
    form_class = AdminShopUserUpdateForm
    success_url = reverse_lazy('adminapp:users')
    page_title = 'users/edit'


# @user_passes_test(lambda user: user.is_superuser)
# def user_delete(request, pk):
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         user.is_active = False
#         user.save()
#         return HttpResponseRedirect(reverse('my_admin:users'))
#
#     context = {
#         'page_title': 'users/delete',
#         'obj_to_delete': user,
#     }
#     return render(request, 'adminapp/delete.html', context)


class UserDeleteView(OnlyAdminMixin, PageTitleMixin, DeleteView):
    model = ShopUser
    success_url = reverse_lazy('my_admin:users')
    page_title = 'user/delete'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


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


# @user_passes_test(lambda user: user.is_staff)
# def categories(request):
#     categories_list = ProductCategory.objects.all().order_by('-is_active', 'pk')
#
#     content = {
#         'page_title': 'administration/categories',
#         'objects': categories_list
#     }
#
#     return render(request, 'adminapp/categories.html', content)


class CategoriesListView(OnlyStaffMixin, PageTitleMixin, ListView):
    model = ProductCategory
    page_title = 'administration/categories of product'


# @user_passes_test(lambda user: user.is_staff)
# def category_create(request):
#     if request.method == 'POST':
#         category_form = AdminProductCategoryEditForm(request.POST)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('my_admin:categories'))
#     else:
#         category_form = AdminProductCategoryEditForm()
#
#     context = {
#         'page_title': 'category/create',
#         'form': category_form
#     }
#
#     return render(request, 'adminapp/update.html', context)


class ProductCategoryCreateView(OnlyStaffMixin, PageTitleMixin, CreateView):
    model = ProductCategory
    success_url = reverse_lazy('my_admin:categories')
    form_class = AdminProductCategoryEditForm
    page_title = 'category/create'


# @user_passes_test(lambda user: user.is_staff)
# def category_update(request, pk):
#     category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         category_form = AdminProductCategoryEditForm(request.POST,
#         instance=category)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('my_admin:categories'))
#     else:
#         category_form = AdminProductCategoryEditForm(instance=category)
#
#     context = {
#         'page_title': 'category/edit',
#         'form': category_form
#     }
#
#     return render(request, 'adminapp/update.html', context)


class ProductCategoryUpdateView(OnlyStaffMixin, PageTitleMixin, UpdateView):
    model = ProductCategory
    form_class = AdminProductCategoryEditForm
    success_url = reverse_lazy('my_admin:categories')
    page_title = 'category/edit'

    def form_valid(self, form):
        if  'discount' in form.cleaned_data:  # cleaned_data -очищенные
            # данные, пришедшие после заполнения формы данными, то что
            # пришло POSTом, структура - словарь.
            discount = form.cleaned_data['discount']
            if discount:
                self.object.product_set.update(
                    price=F('price') * (1 - discount / 100))
        return super().form_valid(form)



# @user_passes_test(lambda user: user.is_staff)
# def category_delete(request, pk):
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         category.is_active = False
#         category.save()
#         return HttpResponseRedirect(reverse('my_admin:categories'))
#
#     context = {
#         'page_title': 'category/delete',
#         'obj_to_delete': category,
#     }
#     return render(request, 'adminapp/delete.html', context)


class ProductCategoryDeleteView(OnlyStaffMixin, PageTitleMixin, DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('my_admin:categories')
    page_title = 'category/delete'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda user: user.is_staff)
def category_products(request, pk):

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by(
        '-is_active', 'name')

    content = {
        'title': 'administration/product',
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/category_products_list.html', content)


@user_passes_test(lambda user: user.is_staff)
def product_create(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        product_form = AdminProductEditForm(request.POST, request.FILES, )
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(
                reverse('my_admin:category_products', kwargs={
                    'pk': category.pk}))
    else:
        product_form = AdminProductEditForm(initial={
            'category': category,
        })

    context = {
        'page_title': 'product/create',
        'form': product_form,
        'category': category,
        'pk': pk,
    }

    return render(request, 'adminapp/update.html', context)


@user_passes_test(lambda user: user.is_staff)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product_form = AdminProductEditForm(request.POST, request.FILES,
                                            instance=product)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(
                reverse('my_admin:category_products', kwargs={
                    'pk': product.category.pk}))
    else:
        product_form = AdminProductEditForm(instance=product)

    context = {
        'page_title': 'product/edit',
        'form': product_form,
        'category': product.category,
        'pk': product.category.pk
    }

    return render(request, 'adminapp/update.html', context)


# @user_passes_test(lambda user: user.is_staff)
# def product_read(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': product,
#         'page_title': 'product/detail'
#
#     }
#     return render(request, 'adminapp/product_read.html', context)


class ProductDetailView(OnlyStaffMixin, PageTitleMixin, DetailView):
    model = Product
    page_title = 'product/detail'


@user_passes_test(lambda user: user.is_staff)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    category_pk = product.category.pk
    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('my_admin:category_products',
                                            kwargs={'pk': category_pk}))

    context = {
        'page_title': 'product/delete',
        'obj_to_delete': product,
        'pk': category_pk,
    }
    return render(request, 'adminapp/delete.html', context)
