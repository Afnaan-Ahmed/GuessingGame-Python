import random

#Generate a random number and store it in a variable.
secret_number = random.randint(1,10)

#Initially, set the guess counter to zero, we can add to it later!
guess_count = 0

#set a limit on how many guesses the user can make.
guess_limit = 3

print('Guess a number between 1 and 10.')

#Do this so the program terminates after the set amount of guesses.
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    #Ask for input and increment guess count by 1 so that our program doesn't loop infinately.
    guess_count += 1
    #Define the rules and conditions of the game.
    if guess == secret_number:
        print('Yay, you guessed right!, You Won!')
        break
        #Break it so it doesn't continue after the user wins the game.
    elif guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        print("Invalid input! Terminating the program.")
else:
    print('You hit the guess limit! You lose.')