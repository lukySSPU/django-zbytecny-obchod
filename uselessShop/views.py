from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Item, Comment
from .forms import CommentForm

def uselessShop_menu(request):
    items = Item.objects.all()
    return render(request, 'uselessShop_menu.html', {'items': items})

def uselessShop_itemInspection(request, id):
    item = get_object_or_404(Item, id=id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, user=request.user)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.username = request.user.username
            comment.save()
            item.comment.add(comment)
    else:
        form = CommentForm(user=request.user if request.user.is_authenticated else None)

    context = {
        'item': item,
        'form': form,
    }
    return render(request, 'uselessShop_itemInspection.html', context)

def uselessShop_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('uselessShop_menu')
        else:
            return render(request, 'login/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login/login.html')

@login_required
def uselessShop_logout(request):
    logout(request)
    return render(request, 'login/logout.html')
