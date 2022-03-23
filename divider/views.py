from django.shortcuts import render, redirect, reverse
from utils.data import *

# Create your views here.

def divider(request):
    if request.method == 'GET':
        user = request.user
        current_money = user.money

        return render(request, 'shop.html', context={'money': current_money})

    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        requirement = request.POST.get('requirement')
        grade = request.POST.get('grade')
        price = evaluate_price(grade)

    return redirect(reverse('shop'), kwargs={'message': 'Created successful'})
