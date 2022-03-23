from django.shortcuts import render, redirect, reverse
from utils.data import *

# Create your views here.

def shop(request):
    if request.method == 'GET':
        user = request.user
        current_money = user.money

        return render(request, 'shop.html', context={'money': current_money})

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
