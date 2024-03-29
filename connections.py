import sys

from termcolor import colored, cprint

# Connections python game
# By Sam Hildebrandt
# Version 0.0.2   # First playable version

# Things to add
        # Add colours
        # add fancy graphics welcome screen
        # Change cell numbers to start at one
        # Split "please enter guess.." onto 2 lines
        # Add more categories (maybe move to separate)
        # Add a phew print out if 1 guess remaining

# Things to fix
        # Guessing same word twice
        # Dont count same guess


#Packages
import random

# Constants
catagories = [  # word list in catagories
    {"name": "Muiscal Instruments", "words": ["guitar", "piano", "violin", "drums"]},
    {"name": "Fruits",              "words": ["apple", "banana", "pear", "grape"]},
    {"name": "Animals",             "words": ["dog", "cat", "bird", "fish"]},
    {"name": "Colors",              "words": ["red", "blue", "green", "yellow"]},
    {"name": "Shapes",              "words": ["circle", "square", "triangle", "rectangle"]},
    {"name": "Vehicles",            "words": ["car", "truck", "bus", "train"]},
    {"name": "Sports",              "words": ["soccer", "basketball", "football", "baseball"]},
    {"name": "Countries",           "words": ["usa", "canada", "mexico", "brazil"]}
]


game_catagories = []

def welcome():
    print("\nWelcome to Connections!")

# Gnenerate a new game by slecting 4 random catgories and adding their words to the game board list
def generate_new_game():
    
    if len(catagories) < 4:
        print("\nThank you, you have played all the catagories that we currently have to offer.")
        print("Stay turned for more catagories in the future!")
        print("\nThanks for playing!")
        print()
        exit()

    random.shuffle(catagories)
    
    # Clear game board and catagories
    game_catagories = []
    game_board = []

    for i in range(4):
        catagory = catagories.pop(0)
        game_catagories.append(catagory)  # selects first 4 catgories from shuffled list and removes them from the origonal list of catgories
        
        for word in catagory["words"]:  # adds words to game board list with catagory guessed state
            grid_cell = {"catagory": catagory,
                         "word"    : word, 
                         "done"    : False}
            game_board.append(grid_cell)
        
    random.shuffle(game_board)  # shuffle game board list
    return game_board
        

def print_line(col_width):  # print row seperator line 
    for col in range(4):
        print("+"+"-"*col_width,end="")
    print("+")

def print_spacer(col_width,first_cell=0,game_board=None):  #print spacer between row, line and word
    
    for col in range(4):
        if first_cell > 0:  # if cell number is passed, print cell number in the col
            cell_number = first_cell + col
            spaces = col_width - 2
            if cell_number > 9:  # if number has 2 digit 
                spaces -= 1
            
            if game_board[cell_number-1]["done"] == True:
                print("|" + " "*col_width, end="")
            else:
                print(f"| {cell_number}" + " "*spaces, end="")  # print the col including cell number
        
        else:
            print("|" + " "*col_width, end="")

    print("|")

def display_game_board(game_board):

    print() 
    cell = 0
    col_width = 18
    for row in range(4):   # create the row
        print_line(col_width)   
        print_spacer(col_width,cell+1,game_board)
        for col in range(4):  # create individual col
            word = game_board[cell]["word"]
            print("|"+centered_text(word,col_width),end="")  # print without creating new line
            cell += 1
        print("|", end="")
        if game_board[cell-1]["done"] == True:  # if line has veeb guessed
            print(f"    {game_board[cell-1]["catagory"]["name"]}",end="")
        print()    
        print_spacer(col_width)
    print_line(col_width)

def string_to_int(string):
    try:
        return int(string)
    except ValueError:
        return 0   
    
def centered_text(word,width):
    spaces = (width-len(word)) // 2
    text = " "*spaces + word
    text += " " * (width - len(text))
    return text

def get_player_input(game_board):
    
    guess_string = input("\nPlease enter your guess by typing the 4 numbers seperated by commas associated to the words you think are connected (e.g '1,5,8,11') : ")
    

    while True:
        guess = guess_string.split(",")
        if len(guess) == 4:  # if guess correct length, 4 inputs
            numeric_guess =[]
            for string in guess:
                string = string.strip()
                cell = string_to_int(string) - 1
                if cell >= 0 and cell < len(game_board) and game_board[cell]["done"] == False: #  Validate guess
                    numeric_guess.append(cell)
                    
                else:
                    print(f"\n'{string}' is not a valid word number")
                    

            if len(numeric_guess) == 4:        
                return numeric_guess        
                   
        print("\nPlease ensure to enter 4 numbers seperated by commas respresenting your 4 chosen words")

        guess_string = input("\nPlease try again : ")

def is_guess_close(game_board,guess):
    guess_1_count = 0
    guess_2_count = 0
    for cell in guess:  
        if game_board[cell]["catagory"] == game_board[guess[0]]["catagory"]:  # count how many guesses match the first guess 
            guess_1_count += 1
        if game_board[cell]["catagory"] == game_board[guess[1]]["catagory"]:  # count how many guesses match the second guess 
            guess_2_count += 1
        
    if guess_1_count == 3 or guess_2_count == 3:
        return True  # At least three are from the same catagory
    else:
        return False
    

def is_guess_correct(game_board, guess):
    # check if the words are from the same catagory
    catagory = game_board[guess[0]]["catagory"]
    for cell in guess:
        if game_board[cell]["catagory"] != catagory:
            return None # words are not from the same catagory
    return catagory


def swap_cells(game_board,a,b):
    temp = game_board[a]
    game_board[a] = game_board[b]
    game_board[b] = temp

def update_board(game_board, catagory):
    for cell in game_board:
        if cell["catagory"] == catagory:
            cell["done"] = True

    for first_not_found in range(0,len(game_board)):
        if game_board[first_not_found]["done"] == False:   # Found the first word that not found
            for last_cell_found in range(len(game_board)-1,0,-1):
                if game_board[last_cell_found]["done"] == True:
                    if last_cell_found < first_not_found:
                        return
                    swap_cells(game_board,first_not_found,last_cell_found)
                    break

def pluralise(number,word,plural):
    if number != 1:
        return word + plural
    else:
        return word


def play_game(game_board):
    lives = 4
    correct_guesses = 0
    
    while lives > 0:
        display_game_board(game_board)
        print(f"\nYou have {lives} {pluralise(lives,"guess","es")} left.")

        guess = get_player_input(game_board)
        correct_catagory = is_guess_correct(game_board, guess)

        if correct_catagory != None: # guess is correct
            update_board(game_board, correct_catagory)
            print("\nCorrect guess!")
            correct_guesses += 1
            if correct_guesses > 3:
                print("\nCongratulations, you have won!!")
                return
            
        elif is_guess_close(game_board, guess):
            print("\nOne away, you got three out of the 4 words correct")
            lives -= 1

        else:
            print("\nSorry, Incorrect guess")
            lives -= 1
    
    print("\nOh no, looks like you've run out of guesses, GAME OVER")


# Main prog starts here
welcome()

while True:
    game_board = generate_new_game()
    play_game(game_board)
    play_again = input("\nWould you like to play again?? Y/N: ")
    if play_again.upper() != "Y":
        print("\nThanks for playing")
        print()
        exit()