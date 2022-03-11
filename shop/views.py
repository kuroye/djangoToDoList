from django.shortcuts import render, redirect, reverse
from utils.data import *
from .models import Item
# Create your views here.

def shop(request):

    if request.method == 'GET':

        user = request.user
        items = Item.objects.all()
        current_level = user.level
        max_xp = calculate_max_xp(current_level)

        return render(request, 'shop.html', context={'max_xp': max_xp,
                                                     'items': items})

    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        requirement = request.POST.get('requirement')
        grade = request.POST.get('grade')
        price = evaluate_price(grade)

        Item.objects.create(name=title, description=description, requirement=requirement,
                            grade=grade, price=price)

        return redirect(reverse('shop'), kwargs={'message': 'Created successful'})
