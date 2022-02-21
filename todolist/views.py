from datetime import timedelta

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from todolist.models import Todo, User


# Create your views here.
@login_required
def index(request):
    if request.method == 'GET':
        todos = Todo.objects.filter(creator=request.user).order_by('deadline')
        user = User.objects.filter(username=request.user)
        max_xp = user.get('level') * user.get('level') * 100
        # justify_time(todos)
        return render(request, 'index.html', context={'todos': todos,
                                                      'max_xp': max_xp})

    if request.method == 'POST':
        do = request.POST.get('do')

        if do == 'add':
            title = request.POST.get('title')
            description = request.POST.get('description')
            deadline = request.POST.get('deadline')

            Todo.objects.create(title=title, description=description, deadline=deadline or None, creator=request.user)

            return redirect(reverse('index'), kwargs={'message': 'Created successful'})

        elif do == 'delete':
            id = request.POST.get('id')
            todo = Todo.objects.get(id=id)
            todo.delete()
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
