from django.shortcuts import render, redirect, reverse
from utils.data import *
from .models import Item
from .forms import ItemForm


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
        # form = ItemForm(request.POST, request.FILES)
        #
        # if form.is_valid():
        title = request.POST.get('title')
        description = request.POST.get('description')
        requirement = request.POST.get('requirement')
        grade = request.POST.get('grade')
        # image = form.
        price = evaluate_price(grade)



        # last_image = Item.objects.last()
        #
        # last_image.path = last_image.image.url
        # last_image.save()

    Item.objects.create(name=title, description=description, requirement=requirement,
                        grade=grade, price=price)

    return redirect(reverse('shop'), kwargs={'message': 'Created successful'})
