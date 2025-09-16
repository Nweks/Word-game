import random

print('Welcome to the Word guessing Game')
print('You have three attempts to guess the correct word \n')

words = ["apple", "grape", "chair", "table", "snake", 
         "bread", "plant", "house", "water", "light"]

print('\n' *1)
print(words)

playing = True
highscore = 0

while playing:
    score = 0
    while True:
        word = random.choice(words)
        attempts = 3

        for i in range(attempts):

            #the player guess
            player_guess = input(f'Attempts {i+1}:Pick a word from the list of words displayed above: ')
        

            if player_guess == word:
                score +=1 #the score increases
                print(f'You got it, your score is now: {score}')
                print('Moving to the next word...\n')
                break
            

            else:
                print('Wrong Guess')
                if i < attempts -1:
                    print('Try Again... \n')
        #fails all the attempts
        else:
            print(f'Out of attempts, the word was:{word}')
            print(f'Game over. Final score is:{score}')

        #updating high score
            if score > highscore:
                highscore = score
                print('New Highscore')
            print(f'Current highscore is:{highscore}')

        #play again
            play_again = input('Do you want to play again(yes/no): ').lower()

            if play_again != 'yes':
                print('Thanks for playing')
                playing = False
                

            else:
                print('\n  Staring a new Game \n')

            break    
               

            
                  