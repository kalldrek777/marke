from django.core.paginator import Paginator
from django.shortcuts import render
from weapons.models import Product
from weapons.forms import SearchForm
from Market.views import Search_page

__all__ = (
    'weapons',
    'knife',
)


def knife(request):
    qs = Product.objects.all().order_by('-date').filter(category='Ножи')
    paginator = Paginator(qs, 8)  # Show 8 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = SearchForm()
    if request.method == 'POST':
        Search_page(request)
        page_obj, form = Search_page(request)
        return render(request, 'Search.html', {'page_obj': page_obj, 'form': form})

    dict = {'page_obj': page_obj, 'form': form}

    return render(request, 'weapons/knifes.html', dict)


def weapons(request):
    qs = Product.objects.all().order_by('-date').filter(category='Оружие')
    paginator = Paginator(qs, 8)  # Show 8 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = SearchForm()
    if request.method == 'POST':
        Search_page(request)
        page_obj, form = Search_page(request)
        return render(request, 'Search.html', {'page_obj': page_obj, 'form': form})

    dict = {'page_obj': page_obj, 'form': form}

    return render(request, 'weapons/weapons.html', dict)


def wear(request):
    qs = Product.objects.all().order_by('-date').filter(category='Одежда')
    paginator = Paginator(qs, 8)  # Show 8 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = SearchForm()
    if request.method == 'POST':
        Search_page(request)
        page_obj, form = Search_page(request)
        return render(request, 'Search.html', {'page_obj': page_obj, 'form': form})

    dict = {'page_obj': page_obj, 'form': form}

    return render(request, 'weapons/wear.html', dict)


def stickers(request):
    qs = Product.objects.all().order_by('-date').filter(category='Наклейки')
    paginator = Paginator(qs, 8)  # Show 8 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = SearchForm()
    if request.method == 'POST':
        Search_page(request)
        page_obj, form = Search_page(request)
        return render(request, 'Search.html', {'page_obj': page_obj, 'form': form})

    dict = {'page_obj': page_obj, 'form': form}

    return render(request, 'weapons/stickers.html', dict)


def accessories(request):
    qs = Product.objects.all().order_by('-date').filter(category='Аксессуары')
    paginator = Paginator(qs, 8)  # Show 8 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = SearchForm()
    if request.method == 'POST':
        Search_page(request)
        page_obj, form = Search_page(request)
        return render(request, 'Search.html', {'page_obj': page_obj, 'form': form})

    dict = {'page_obj': page_obj, 'form': form}

    return render(request, 'weapons/accessories.html', dict)
