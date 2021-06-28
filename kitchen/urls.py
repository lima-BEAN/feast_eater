"""feastfreedom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'kitchen'

urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    path('', views.home, name='home'),
    path('check', views.check, name='check'),
    re_path(r'kitchen/$', views.KitchenListView.as_view(), name='index'),
    #path('', KitchenListView.as_view(), name='index'),
    path('kitchen/create', views.KitchenCreateView, name='kitchen_create'),
    path('kitchen/<pk>', views.KitchenDetailView, name='kitchen_detail'),
    path('kitchen/<pk>/update', views.KitchenUpdateView.as_view(), name='kitchen_update'),
    path('kitchen/<pk>/delete', views.KitchenDeleteView.as_view(), name='kitchen_confirm_delete'),
    # path('kitchen/<pk>/food/create', views.FoodCreateView, name='food_create'),
    # path('food/<pk>', views.FoodDetailView.as_view(), name='food_detail'),
    # path('kitchen/<kpk>/food/<fpk>/delete', views.FoodDeleteView, name='food_confirm_delete'),
    # path('kitchen/<kpk>/food/<fpk>/update', views.FoodUpdateView, name='food_update'),

    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),

    path('accounts/profile/', views.profile, name='profile'),

    re_path(r'^register/$', views.register, name='register'),

]
