from django.db import models
from django import forms
from random import seed, randint


# Here is the business end of the Bull-Cow logic

class PlayMaster:
    def __init__(self):
        pass
        # self.secret_num = SecretNumber.create_secret_number()

    @staticmethod
    def create_secret_number():
        """create random 4 dig number in a list"""
        secret_num = []
        seed()

        while len(secret_num) < 4:
            secret_digit = randint((int('0')), int('9'))
            if secret_digit not in secret_num:
                secret_num.append(str(secret_digit))
        result = ''.join(str(x) for x in secret_num)
        return result

    @staticmethod
    def bull_cow_return(secret_num, player_num):
        """return (cows, bulls) count"""
        cows = len([digit for digit in player_num if digit in secret_num])
        bulls = 0
        for i in range(len(player_num)):
            if player_num[i] == secret_num[i]:
                bulls += 1

        return bulls, cows

    # TODO
    # def play(self, player_num):
    #     bulls, cows = self.bull_cow_return(self.secret_num, player_num)
    #     if bulls == 4:
    #         self.won = True
    #         result = f'YOU WON!\n{player_num} is the secret number {self.secret_num}.\n'
    #     else:
    #         result = f'Cows: {cows}, Bulls: {bulls}'
    #     return result


# Models for the DB.
#todo add null=True

class Player(models.Model):
    player_id = models.CharField(max_length=250)
    player_nickname = models.TextField(max_length=50, default='AwesomeUser')
    

class ScoreBoard(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    won = models.BooleanField(default=False)
    secret_num = models.PositiveIntegerField()

    def __str__(self):
        """A string representation of the model."""
        return f"id: {self.user_id} secret: {self.secret_num} won: {self.won}"


class ScoreCard(models.Model):
    score_board = models.ForeignKey(ScoreBoard, on_delete=models.CASCADE)

    user_num = models.CharField(max_length=4)
    bulls = models.CharField(max_length=1)
    cows = models.CharField(max_length=1)

    def __str__(self):
        """A string representation of the model."""
        return f"user: {self.user_num} bulls: {self.bulls} cows: {self.cows}"
