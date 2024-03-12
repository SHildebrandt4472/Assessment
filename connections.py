import sys

from termcolor import colored, cprint

# Connections python game
# By Sam Hildebrandt
# Version 0.0.1

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
    print("Welcome to Connections!")

# Gnenerate a new game by slecting 4 random catgories and adding their words to the game board list
def generate_new_game():
    
    if len(catagories) < 4:
        print("Thank you, you have played all our catagories that we offer currently, stay turned for more catagories in the future!")  # move to play again function ---->
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
                         "done": False}
            game_board.append(grid_cell)
        
    random.shuffle(game_board)  # shuffle game board list
    return game_board
        

def display_game_board(game_board):
      
      cell_number = 1
      for cell in game_board:
        print(cell_number, cell["word"])
        cell_number += 1

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
    
    guess_string = input("Please enter your guess by typing the 4 numbers seperated by commas associated to the words you think are connected (e.g '1,5,8,11') : ")
    
    while True:
        guess = guess_string.split(",")
        if len(guess) == 4:
            numeric_guess =[]
            for string in guess:
                string = string.strip()
                cell = string_to_int(string) - 1
                if cell >= 0 and cell < len(game_board) and game_board[cell]["done"] == False:
                    numeric_guess.append(cell)
                    
                else:
                    print(f"'{string}' is not a valid word number")
                    print("Please ensure to enter 4 numbers seperated by commas respresenting your 4 chosen words")

            if len(numeric_guess) == 4:        
                return numeric_guess        
                    
        else:            
            print("Please ensure to enter 4 numbers seperated by commas respresenting your 4 chosen words")

        print("")
        guess_string = input("Please try again : ")

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
            return False
    return True


# Main prog starts here
welcome()

print(centered_text("word", 20))

game_board = generate_new_game()
display_game_board(game_board)
guess = get_player_input(game_board)
correct = is_guess_correct(game_board, guess)
if correct == True:
    print("You Win!")
elif is_guess_close(game_board, guess):
    print("You are one off...")
else:
    print("You lose!, your bad!") 

    