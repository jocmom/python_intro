
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
secret_number = 0
remaining_guesses = 7

# define helper functions
def init(range):
    global secret_number
    global num_range
    global remaining_guesses
    num_range = range
    
    secret_number = random.randrange(0, num_range)
    print "\nGuess a new number between [0, %d)" % (num_range)    

    remaining_guesses = int (round(math.log(num_range, 2)+0.5))
    print "Number of remaining guesses is %d" % (remaining_guesses)

    
# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    init(100)


def range1000():
    # button that changes range to range [0,1000) and restarts
    init(1000)   
    
def get_input(guess):
    # main game logic goes here	
    global remaining_guesses
  
    guess_number = float(guess)
    # invalid input
    if guess_number < 0 or guess_number >= num_range :
        print "Invalid input, your guess must be in the range [0, %d)" % (num_range)
        return
    print "\nGuess was %d" % (guess_number)
    
    remaining_guesses -= 1
    print "Number of remaining guesses is %d" % (remaining_guesses)
    
    # compare guessed number with secret number
    if guess_number == secret_number :
        print "BINGO!!!"
        init(num_range)   
        return
    # no guesses left 
    elif remaining_guesses == 0 :
        print "You ran out of guesses. Secret number was %d" % (secret_number)
        init(num_range)
        return      
    elif guess_number > secret_number :
        print "Lower!"
    elif guess_number < secret_number :
        print "Higher!"
    else :
        print "ERROR - Cannot compare numbers"

    
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)


# register event handlers for control elements
frame.add_button("Range: 0-100", range100, 200)
frame.add_button("Range: 0-1000", range1000, 200)
frame.add_input("Your guess:", get_input, 200)


# start frame
init(num_range)
frame.start()

# always remember to check your completed program against the grading rubric
