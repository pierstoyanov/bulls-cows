# Here is the business end of the Bull-Cow logic
from random import seed, randint

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