import random

num_flip = int(input('How many times do you want to flip: '))

heads = 0
tails = 0


for i in range(num_flip):
    flip = random.choice(['Heads', 'Tails'])

    if flip == 'Heads':
        heads +=1

    else:
        tails +=1

print(f'Heads: {heads}')
print(f'Tails : {tails}')            

