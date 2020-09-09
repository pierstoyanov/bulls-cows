from django.shortcuts import render
from django.shortcuts import HttpResponse
from bulls_cows.models import PlayMaster
from bulls_cows.models import ScoreCard, ScoreBoard
# Create your views here.




def home(request):
    return render(request, 'bulls_cows/home.html')


Score_card = ScoreCard()

def play(request):


    try:
        user_number = request.POST['user-number']
        Score_card.user_num = user_number
        bulls_cows_count = PlayMaster.bull_cow_return(Score_card.secret_num, Score_card.user_num)
        print(f"User num = {Score_card.user_num} \nSecret num = {Score_card.secret_num}")

        Score_card.bulls = bulls_cows_count[0]
        Score_card.cows = bulls_cows_count[1]
        print(Score_card.bulls, Score_card.cows)
        Score_card.save()
        sc_2=ScoreCard()

    except KeyError:
        pass

    return render(request, 'bulls_cows/play.html', {"data": f"Bulls: {Score_card.bulls} | Cows: {Score_card.cows}"})

