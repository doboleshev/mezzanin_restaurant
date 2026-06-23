from django.shortcuts import render

from .menu_data import DESSERTS_SECTION, MENU_CATEGORIES


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def menu(request):
    return render(request, 'pages/menu.html', {
        'categories': MENU_CATEGORIES,
        'desserts': DESSERTS_SECTION,
    })
