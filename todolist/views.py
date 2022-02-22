from datetime import timedelta

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from todolist.models import Todo, User


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

            Todo.objects.create(title=title, description=description, deadline=deadline or None, difficulty=difficulty or None, creator=request.user)

            return redirect(reverse('index'), kwargs={'message': 'Created successful'})

        elif do == 'delete':
            id = request.POST.get('id')
            todo = Todo.objects.get(id=id)

            user = User.objects.get(id=request.user.id)
            user.xp = user.xp + todo.xp
            user.save()

            todo.delete()
            # 删除时+XP到User xp
            return redirect(reverse('index'), kwargs={'message': 'Deleted successful'})

        elif do == 'toggle_status':
            id = request.POST.get('id')
            todo = Todo.objects.get(id=id)
            todo.is_finished = not todo.is_finished

            todo.save()
            return redirect(reverse('index'))

def justify_time(todos):
    for todo in todos:
        todo.create_date = todo.create_date + timedelta(hours=6)
        todo.save()

def level_up(user, max_xp):
    user.level = user.level+1

    if user.xp >= max_xp:
        user.xp = user.xp - max_xp

    user.save()

def calculate_max_xp(level):
    max_xp = pow(level, 2) * 100
    return max_xp

