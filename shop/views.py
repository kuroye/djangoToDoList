from django.shortcuts import render

# Create your views here.

def shop(request):

    if request.method == 'GET':

        return render(request, 'shop.html')
