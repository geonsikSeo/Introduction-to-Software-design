import random

guessesTaken=0

print('Hello! what is your name?')
myName = raw_input()

number = random.randint(1, 20)
print('Well '+ myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.')
    guess = int(raw_input())

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
       break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, '+ myName+ '! you guessed my number in ' + guessesTaken)

if guess != number:
    number = str(number)
    print('Nope. the number I was thinking of was ' + number)
