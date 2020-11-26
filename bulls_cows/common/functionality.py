def test_cooke(request):
    #reload test cookie
    request.session.set_test_cookie()
    
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        cookie_state = True
    else:
        cookie_state = False
    
    return cookie_state


# def get_current_player(request):
#     if request.session.get('player_token'):
#         current_player = Player.objects.get_or_create(player_id=request.session['player_token'])
#     else:
#         current_player = Player()
#         current_player.save()
#         request.session['player_token'] = str(current_player.player_id)

#     return current_player