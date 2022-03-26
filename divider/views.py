from django.shortcuts import render, redirect, reverse
from utils.data import *

# Create your views here.

def divider(request):
    if request.method == 'GET':
        user = request.user
        current_money = user.money

        return render(request, 'divider.html', context={'money': current_money})

    if request.method == 'POST':
        user = request.user
        money = request.POST.get('money')
        user.money = money
        user.save()
    return redirect(reverse('divider'), kwargs={'message': 'Created successful'})
