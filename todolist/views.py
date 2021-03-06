from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from todolist.models import Todo, User
from utils.data import *

# Create your views here.
@login_required
def index(request):
    if request.method == 'GET':
        user = request.user
        todos = Todo.objects.filter(creator=user).order_by('deadline')

        current_level = user.level

        max_xp = calculate_max_xp(current_level)

        while user.xp >= max_xp:
            level_up(user, max_xp)
            user = request.user
            max_xp = calculate_max_xp(user.level)

        return render(request, 'index.html', context={'todos': todos,
                                                      'max_xp': max_xp})

    if request.method == 'POST':
        do = request.POST.get('do')

        if do == 'add':
            title = request.POST.get('title')
            description = request.POST.get('description')
            deadline = request.POST.get('deadline')
            # xp = request.POST.get('xp')
            difficulty = request.POST.get('difficulty')
            # 下一步： 更新xp为选择困难度   xp自动生成
            xp = evaluate_xp(difficulty)
            coin = evaluate_coin(difficulty)
            Todo.objects.create(title=title, description=description, deadline=deadline or None, xp=xp, coin=coin,
                                difficulty=difficulty or None, creator=request.user)

            return redirect(reverse('index'), kwargs={'message': 'Created successful'})

        elif do == 'exchange':
            id = request.POST.get('id')
            todo = Todo.objects.get(id=id)
            user = User.objects.get(id=request.user.id)

            if todo.is_finished:
                user.xp = user.xp + todo.xp
                user.coin = user.coin + todo.coin
                user.save()

            todo.delete()
            return redirect(reverse('index'), kwargs={'message': 'Deleted successful'})

        elif do == 'toggle_status':
            id = request.POST.get('id')
            todo = Todo.objects.get(id=id)
            todo.is_finished = not todo.is_finished

            todo.save()
            return redirect(reverse('index'))


