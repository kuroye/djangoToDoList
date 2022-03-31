from django.shortcuts import render, redirect, reverse
from utils.data import *

# Create your views here.

def divider(request):
    if request.method == 'GET':
        user = request.user
        current_money = user.money
        money_need = current_money*0.5
        money_invest = current_money*0.4
        money_want = current_money*0.1

        return render(request, 'divider.html', context={'money': current_money,
                                                        'need': money_need,
                                                        'invest': money_invest,
                                                        'want': money_want})

    if request.method == 'POST':
        user = request.user
        money = request.POST.get('money')
        income = request.POST.get('income')
        outcome = request.POST.get('outcome')
        user.money = money + income - outcome
        user.save()

    return redirect(reverse('divider'), kwargs={'message': 'Created successful'})
