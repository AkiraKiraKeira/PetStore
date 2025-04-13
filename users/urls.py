from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.home_page_view, name='home_page_view'),
    path('', views.dashboard, name='dashboard'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('log_in', views.log_in, name='log_in'),
    path('_logout', views._logout, name='_logout'),
    path("accounts", include("django.contrib.auth.urls")),
    # path("accounts/password_change/", views.password_change),
    # path("accounts/password_change/done/", views.password_change),
    # path("accounts/password_reset/", views.password_change),
    # path("accounts/password_reset/done/", views.password_change),
    # path("accounts/reset/<uidb64>/<token>/", views.password_change),
    # path("accounts/reset/done/", views.password_change),

]