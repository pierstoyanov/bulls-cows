from django.db import models
from random import seed, randint
from django import forms


class SecretNumber:
    @staticmethod
    def create_secret_number():
        """create random number"""
        secret_num = []
        seed()

        while len(secret_num) < 4:
            secret_digit = randint((int('0')), int('9'))
            if secret_digit not in secret_num:
                secret_num.append(str(secret_digit))
        return secret_num



class PlayGame:
    def __init__(self):
        self.won = False
        self.secret_num = SecretNumber.create_secret_number()


    def bull_cow_return(self, player_num):
        """return (cows, bulls) count"""
        cows = len([digit for digit in player_num if digit in self.secret_num])
        bulls = 0

        for i in range(len(player_num)):
            if player_num[i] == self.secret_num[i]:
                bulls += 1

        return bulls, cows


    def play_game(self, player_num):
     #TODO
        for i in range(tries):
            count = f'Try {i + 1} of {tries}'

            player_num = get_player_num()
            bulls, cows = bull_cow_return(secret_num, player_num)

            if bulls == 4:
                won = True
                result = f'YOU WON!\n{player_num} is the secrest number {secret_num}.\n'
                break
            else:
                print(f'Cows: {cows}, Bulls: {bulls}')

        print(result)
        return (won)

class UserInputNumber(forms.Form):
    digitpad = forms.DecimalField(label='digits')
    # digit_two = forms.DecimalField(label='d_two')
    # digit_three = forms.DecimalField(label='d_three')
    # digit_four = forms.DecimalField(label='d_four')