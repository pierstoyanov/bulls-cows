from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib import messages

from bulls_cows.models import PlayMaster
from bulls_cows.models import ScoreCard, ScoreBoard, Player
# Create your views here.




def home(request):
    #todo - make better cookie message
    request.session.set_test_cookie()
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        messages.success(request, 'Cokes are turned ON')
    else:
        request.session.set_test_cookie()
        messages.error(request, 'Please enable cookie')

    return render(request, 'bulls_cows/home.html')


player = Player()
def play(request):
    #TODO Test if browser uses cookies


    #get or create user from session id

    player, created = Player.objects.get_or_create(player_id = request.session.session_key)

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

