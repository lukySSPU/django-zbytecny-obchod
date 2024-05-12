from django.urls import path
from . import views

urlpatterns = [
    path('uselessShop/', views.uselessShop_menu, name='uselessShop'),
    path('uselessShop/itemInspection/<int:id>', views.uselessShop_itemInspection, name='itemInspection'),
]