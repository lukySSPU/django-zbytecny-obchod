from django.urls import path
from . import views

urlpatterns = [
    path('uselessShop/', views.uselessShop_menu, name='uselessShop'),
]