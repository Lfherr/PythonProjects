import random

"""Number guessing game.
Batch file to run from command line: 
@py.exe File Location"""



print("Welcome to the Number Guessing Game!")
print("Enter your name.")
player_name = input("My name is ")
print("You have 6 attempts.")
print("Now enter your guess.  Choose a number between 1 and 20")

rand_num = random.randint(1, 20)
#print(rand_num) #For test purposes

for i in range(6):
    player_guess = input("I guess the number: ")
    if int(player_guess) < 1 or int(player_guess) > 20:
        print("Your guess is out of the given range. Guess again")
    elif int(player_guess) > rand_num:
        print("That was too high.")
    elif int(player_guess) < rand_num:
        print("That was too low.")
    else:
        print("Congratulations, " + player_name + "! You guessed correctly")
        break #Player guessed the correct number
if int(player_guess) != rand_num:
    print("You ran out of attempts and did not guess the number. The correct number was " + str(rand_num) +
          ". Better luck next time!")

print("The game is now finished. Thank you for playing")
