from random import seed, randint 
def main():

        
    def create_secret_number(size):
        """create random number with size"""
        seed()
        secret_number = randint((int('1'*size)), int('9' * size))
        return secret_number


    def bull_cow_return(sec_num, given_num):
        """return (cows, bulls) count"""
        my, your = str(sec_num), str(given_num)
        
        bulls = 0
        for i in range(len(your)):
            if your[i] == my[i]:
                bulls += 1

        cows = len([x for x in your if x in my])
        
        return cows, bulls


    def play(tries = 7, size = 4):
        secret_num = create_secret_number(size)
        print(secret_num)

        for i in range(tries):
            won = False
            player_input = input(f'Try 1 of {tries + 1 - i}\n')[0:size]

            x = bull_cow_return(secret_num, player_input)
            if x[1] == size:
                won = True
                result = f'YOU WON!\n{player_input} is the secrest number {secret_num}.\n'
                print(result)
                break
            else:
                result = f'Cows: {x[0]}, Bulls: {x[1]}'
                print(result)

        if not won:
            play_again = input('Sorry, you ran out of tries! Would you like to play again?\n')
            if play_again in ['yes', 'y', 'Y', 'YES', 'Yes']:
                play()
            else:
                return print('OK, Thank you for playing.')

    play()

if __name__ == '__main__':
    main()