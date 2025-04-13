from django.shortcuts import render, get_object_or_404
# from django.http import render
# from django.template import loader Було
# template.loader import get_template

from django.shortcuts import render
def home_page_view(request):
    return render(request, 'base.html')


def about_us(request):
    return render(request, 'about.html')  # Рендерим шаблон для страницы "About Us"

# {% include "home.html" %}
def blog(request):
    return render(request, 'blog.html')

def black_friday(request):
    return render(request, 'black_friday.html')
# def users(request):
#     return render(request, 'users.html')
def registration(request):
    return render(request, 'dashboard.html')