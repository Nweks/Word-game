import random

# guessing a random number the computer choose

secret_number = random.randint(1, 100)
attempts = 0

print('Welcome to the number guessing game \n')
print('I am thiking of a number between 1 and 100 ')


while True:
    try:
        guess = int(input('Guess a number between 1 and 100: '))
        attempts +=1

        if guess < secret_number:
            print('Too low, Try again!')

        elif guess > secret_number:
            print('Too high, try again!')

        else:
            print(f'Congratulations, You got it in {attempts} tries')
            break

    except ValueError:
        print('Please enter a valid number')    




