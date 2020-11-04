from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib import messages

from bulls_cows.common.play_master import PlayMaster
from bulls_cows.models import ScoreCard, ScoreBoard, Player

# from bulls_cows.common import player_session

# Create your views here.


def play(request):

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        cookie_state = True
    else:
        cookie_state = False


    if request.session.get('player_token'):
        current_player = Player.objects.get_or_create(player_id=request.session['player_token'])
    else:
        
        current_player = Player.objects.create()
        request.session['player_token'] = getattr(current_player,'player_id')

    print(current_player)

    if request.method == 'GET':

        context = {
            # "id": getattr(current_player,'player_name'),
            "cookie_state": cookie_state,
        }


        #stage test cookie
        request.session.set_test_cookie()


        return render(request, 'play.html', context) 

    else:

        context = {
            "id": current_player['player_name'],
            "cookie_state": cookie_state
        }
        
        
        #stage test cookie
        request.session.set_test_cookie()

        return render(request, 'play.html', context)

    #get or create user from session id

    # player, created = Player.objects.get_or_create(player_id = request.session.session_key)

    # try:

    #     user_number = request.POST['user-number']
    #     Score_card.user_num = user_number
    #     bulls_cows_count = PlayMaster.bull_cow_return(Score_card.secret_num, Score_card.user_num)
    #     print(f"User num = {Score_card.user_num} \nSecret num = {Score_card.secret_num}")

    #     Score_card.bulls = bulls_cows_count[0]
    #     Score_card.cows = bulls_cows_count[1]
    #     print(Score_card.bulls, Score_card.cows)
    #     Score_card.save()
    #     sc_2=ScoreCard()

    # except KeyError:
    #     pass