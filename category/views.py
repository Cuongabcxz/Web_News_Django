from django.shortcuts import render, redirect
from .models import Category, Type
from .forms import CategoryForm


# Create your views here.

def category(request):
    category_list = Category.objects.all().filter()
    context = {
        'category_list': category_list,
    }
    return render(request, 'users/category/category.html', context)


def category_create(request):
    template = 'users/category/add_category.html'
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return render(request, 'users/category/category.html', {})
    else:
        category_form = CategoryForm()
    context = {
        'category_form': category_form,
    }
    return render(request, template, context=context)


def category_update(request, category_slug=None):
    category = Category.objects.get(slug=category_slug)
    category_form = CategoryForm(instance=category)

    if request.method == 'POST':
        category_form = CategoryForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            return render(request, 'users/category/category.html')

    context = {
        'category_form': category_form,
        'category': category,
    }
    return render(request, 'users/category/update_category.html', context)


def category_delete(request, category_slug=None):
    category = Category.objects.get(slug=category_slug)

    if request.method == 'POST':
        category.delete()
        return render(request, 'users/category/category.html')

    context = {
        'category': category,
    }
    return render(request, 'users/category/delete_category.html', context)