from django.shortcuts import render

# Create your views here.

def shop(request):

    if request.method == 'GET':

        user = request.user
        current_level = user.level
        # max_xp = calculate_max_xp(current_level)
        max_xp = current_level

        return render(request, 'shop.html', context = {'max_xp': max_xp})
