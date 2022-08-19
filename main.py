import random 
#import random will allow the computer to generate a secret number for us to guess

def guess(x):
    random_number = random.randint(1,x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}'))
        if guess < random_number:
            print('Sorry, guess again.Too Low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'YOU WIN! You have guessed the number {random_number} correctly')




#we have a secret number and we want the computer to guess the number
def computer_guess(x):
    low = 1
    high = x
    feedback = '' #this feedback variable allows for us to answer whether or not the guess is too high or too low
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high) # we pass low, high instead of 1,x because after every guess the range of possible answers will continue to change
        else:
            guess = low # could also be high because low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay the computer guessed our number, {guess}, correctly!')


guess(1000)

computer_guess(1000)