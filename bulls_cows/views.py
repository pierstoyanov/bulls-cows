from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import UserInputNumber
from .game import *

def home(request):
    
    return render(request, 'bulls_cows/home.html')


def play(request):

    form = UserInputNumber()



    # user_digits = UserInputNumber
    
    # if request.method == 'POST':
    #     form = UserInputNumber(request.POST)
    #     print(form)


    # play_game()
    # count = []
    return render(request, 'bulls_cows/play.html', {'form':form})


# def play_this(request):
#     try:
#         game.main()
#         return render(request, 'bulls_cows/game.html')
#     except:
#         pass
