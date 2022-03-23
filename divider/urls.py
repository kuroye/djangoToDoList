from django.urls import path
from .views import divider

urlpatterns = [
    path('', divider, name='divider')
]
