import random 
n = random.randint(0,9)
guess_count = 0
guess_limit = 3
print('Guess a number between 0 to 9.')
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count +=1
    if guess == n:
        print('You win ')
        break
else:
    print('better luck next time.')
