from django.urls import path ,include
from .views import *
urlpatterns = [    
    path('', board_lists, name='board_lists'),
]