from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home_page_view'),
    path('about_us/', views.about_us, name='about_us'),
    path('blog/', views.blog, name='blog'),
    path('black_friday/', views.black_friday, name='black_friday'),
    path('registration/', views.registration, name='registration')
]