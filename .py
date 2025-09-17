import getpass
import random

def play():
    choices = ['rock', 'paper', 'scissors']

    #welcome message
    print('Welcome to the rock, paper, scissors game')
    print('Are you ready to play')
    print("Enter 'quit' to exit")

    score1 = 0
    score2 = 0

    
    #the main game play
    while True:
        user1 = getpass.getpass('pick one (rock, paper, scissors): ').lower()

        print('\n'*2)

        if user1 == 'quit':
            print('Thanks for playing')
            break

        if user1 not in choices:
            print('Invalid choice. Try again \n')
            continue

        user2 = getpass.getpass('Pick your choice user2 (rock,paper,scissors): ').lower()

        if user2 =='quit':
            print('User2 quits')
            print('Thanks for Playing')
            break

        if user2 not in choices:
            print('Invalid choice. Try again \n')

        if user1 == user2:
            print('It is a tie \n')
            
        #conditions that makes user1 wins
        elif (user1=='rock' and user2 =='scissors') or \
            (user1=='scissors' and user2=='paper') or \
            (user1=='paper' and user2=='rock') :
            print('Congratulation, User1 wins!')
            score1 +=1
            
        #conditions that makes user2 wins
        elif  (user2=='rock' and user1 =='scissors') or \
            (user2=='scissors' and user1=='paper') or \
            (user2=='paper' and user1=='rock') :
            print('Congratulation, User2 wins!')
            score2 +=1

        else:
            print('Invalid input, please typr rock paper or scissors')
        #shows the score after each round
        print(f' user1 score: {score1} | user2 score: {score2} \n')

    #final score after playing  
    print('Game over')
    print(f'Final Score --> user1: {score1}  | user2: {score2} ')

    if score1 > score2 :
        print('User1 is the winner')

    elif score2 > score1:
        print('User2 is the winner')

    else:
        print('It ends in a tie')

if __name__ == '__main__':
    play()

