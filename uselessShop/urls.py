from django.urls import path
from . import views

urlpatterns = [
    path('', views.uselessShop_menu, name='uselessShop_menu'),
    path('itemInspection/<int:id>/', views.uselessShop_itemInspection, name='uselessShop_itemInspection'),
    path('login/', views.uselessShop_login, name='login'),
    path('logout/', views.uselessShop_logout, name='logout'),
]
