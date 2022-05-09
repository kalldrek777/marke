from django.contrib import messages
from django import template
from django.core.paginator import Paginator
from django.shortcuts import render
from weapons.models import Product
from weapons.forms import SearchForm
import sqlite3


def home(request):
    qs = Product.objects.all().order_by('-date')
    paginator = Paginator(qs, 8)  # Show 8 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = SearchForm()
    if request.method == 'POST':
        Search_page(request)
        page_obj, form = Search_page(request)
        return render(request,  'Search.html', {'page_obj': page_obj, 'form': form})

    dict = {'page_obj': page_obj, 'form': form}

    return render(request, 'home.html', dict)


def Search_page(request):
    form = SearchForm(request.POST)
    if form.is_valid():
        form_query = form.cleaned_data
        #   print(form_query['query'])
        query = form_query['query'].lower()
        a = []
        qs = Product.objects.all().order_by('-date')
        for i in qs:
            if query in i.name.lower():
                a.append(i)
                paginator = Paginator(a, 8)  # Show 8 contacts per page.

                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
            elif query not in i.name.lower():
                paginator = Paginator(a, 8)  # Show 8 contacts per page.

                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)

        return page_obj, form










