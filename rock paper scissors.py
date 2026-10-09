from tkinter import *
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [('rock', 0), ('paper', 1) ('scissors', 3)]

def computer_wins():
    global computer_score, player_score
    computer_score += 1
    winner_label.config(text = "Computer Won!!!")
    computer_score_label.config(text = 'Computer Score : ' + str(computer_score))
    player_score_label.config(text = 'Player Score : ') + str(player_score))

def player_wins():
    global computer_score, player_score
    player_score += 1
    winner_label.config(text = "Player Won!!!")
    computer_score_label.config(text = 'Computer Score: ' + str(computer_score))
    player_score_label.config(text = 'Player Score: ' + str(player_score))

def tie():
    global computer_score, player_score
    winner_label.config(text = "Tie!!!")
    computer_score_label.config(text = 'Computer Score: ' + str(computer_score))
    player_score_label.config(text = 'Player Score: ' + str(player_score))

def player_choice(player_input):
    global player_score, computer_score
    print(player_input)

    computer_input = get_computer_choice()
    print(computer input)
    player_choice_label.config(text = 'Your selected : ' + player_input[0])
    computer_choice_label.config(text = 'Computer selected : ' + computer_input[0])

    if (player_input == computer_input):
        tie()

#   If player has chosen rock:
    if(player_input[1] == 0):
        if(computer_input[[1] == 1):
            computer_wins()

        elif (computer_input[1] == 2):
            player_wins()

#   If player has chosen paper:
    elif(player_input[1] == 1):
        if(computer_input[1] == 1):
            player_wins()
            
        elif (computer_input[1] == 2):
            computer_wins()

#   If player has chosen scissors:
    elif(player_input[1] == 2):
        if(computer_input[1] == 0):
            computer_wins()
            
        elif (computer_input[1] == 1):
            player_wins()


#Function to randomly select computer choice
def get_computer_choice():
    return random.choice(options)

game_window = Tk()
game_window.title("Rock, Paper, Scissors Game!")

app_font = font.Font(size = 12)

#Displaying Game Title
game_title = Label(text = "Rock, paper, scissors",font = font.Font(size = 20), fg = 'grey')
game_title.pack()

#Label to display, who wins each time
winner_label = Label(text = "Let's Start the Game...", fg = 'green', font = font.Font(size = 13), pady = 8)
winner_label.pack()

input_frame = Frame(game_window)
input_frame.pack()

#Displaying playr options
player_options = Label(input_frame, text = "Your options : ", font = app_font, fg = 'green')















            

            

        
        



















