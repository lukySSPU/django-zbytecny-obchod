from django.shortcuts import loader
from django.http import HttpResponse
from .models import Item

def uselessShop_menu(request):
    items = Item.objects.all()
    template = loader.get_template('uselessShop_menu.html')
    context = {
        'items' : items,
    }
    return HttpResponse(template.render(context, request))

def uselessShop_itemInspection(request, id):
    item = Item.objects.get(id=id)
    template = loader.get_template('uselessShop_itemInspection.html')
    context = {
        'item' : item,
    }
    return HttpResponse(template.render(context, request))