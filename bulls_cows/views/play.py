from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.views import View

from bulls_cows.common.play_master import PlayMaster
from bulls_cows.models import ScoreCard, ScoreBoard, Player
from bulls_cows.forms.profile import PlayerForm
from bulls_cows.forms.number_form import NumberForm

from bulls_cows.common.functionality import test_cooke


# from bulls_cows.common import player_session

# This view handles the user selection and play logic.
# There are two forms - player name and player number input.

class Play(View):

    def get(self, request):
        #check the cookies state
        cookie_state = test_cooke(request)

        #get the player token from cookies
        player_token = request.session.get('player_token')

        if player_token:
            #get or create player from DB
            current_player = Player.objects.get(player_id=player_token)
        else:
            # If no player token is present in cookies - create player and token
            current_player = Player.objects.create()
            request.session['player_token'] = str(current_player.player_id)

        form_player_name = PlayerForm(
            instance=current_player,
            initial={'player_name': current_player.player_name})

        form_number_input = NumberForm()

        context = {
            'id': current_player.player_name,
            'cookie_state': cookie_state,
            'form_player_name': form_player_name,
            'form_number_input': form_number_input
        }


        return render(request, 'play.html', context) 

    def post(self, request):

        # check the cookies state
        cookie_state = test_cooke(request)

        player_token = request.session.get('player_token')
        current_player = Player.objects.get(player_id=player_token)


        if 'player_name' in request.POST:      
            form = PlayerForm(request.POST, instance=current_player)
            if form.is_valid():
                form.save()
                

        elif 'digits_input' in request.POST:
            form = NumberForm(request.POST)
            if form.is_valid():
                request.session['player_number'] = request.POST.get('digits_input')
                return HttpResponseRedirect(request.path_info) 
