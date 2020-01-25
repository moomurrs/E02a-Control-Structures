#!/usr/bin/env python3
#import the libraries needed
import sys, random

# display a message is the python version is below 3.7
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# print to terminal
print('Greetings!')
# a list of color
colors = ['red','orange','yellow','green','blue','violet','purple']
# empty String
play_again = ''
# find CPU's largest number its registers are capable of holding
best_count = sys.maxsize            # the biggest number

# play as long as play_again isn't n or no
while (play_again != 'n' and play_again != 'no'):
    # randomly choose a String from the color list
    match_color = random.choice(colors)
    # reset count stat
    count = 0
    # reset user input variable
    color = ''
    # run loop continuously until user guesses the color
    while (color != match_color):
        # get user input to color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        # remove whitespaces and lowercase the input 
        color = color.lower().strip()
        # increment number of tries
        count += 1
        # if there's a match, print correct. If not, print stats.
        if (color == match_color):
            # print to terminal when the if condition is true
            print('Correct!')
        else:
            # print to terminal when the if condition is false
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    
    # print stats.
    print('\nYou guessed it in {} tries!'.format(count))

    # display if the current stats outrank the old ones.
    if (count < best_count):
        # print to terminal when condition is true
        print('This was your best guess so far!')
        # if the current stats are better than the old one, make current stats the best_count.
        best_count = count
    # print to terminal if the user want's to play again.
    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()

# final print to terminal before exiting.
print('Thanks for playing!')