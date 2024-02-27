
# Connections python game
# By Sam Hildebrandt
# Version 0.0.1

#Packages
import random

# Constants
catagories = [  # word list in catagories
    {"name": "Muiscal Instruments", "words": ["guitar", "piano", "violin", "drums"]},
    {"name": "Fruits",              "words": ["apple", "banana", "orange", "grape"]},
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

def get_player_input(game_board):
    
    guess_string = input("Please enter your guess by typing the 4 numbers seperated by commas associated to the words you think are connected (e.g '1,5,8,11') : ")
    
    while True:
        guess = guess_string.split(",")
        if len(guess) == 4:
            numeric_guess =[]
            for string in guess:
                cell = string_to_int(string)
                if cell > 0 and cell <= len(game_board) and game_board[cell-1]["done"] == False:
                    numeric_guess.append(cell)
                    
                else:
                    print(f"{cell} is not a valid word number")

            if len(numeric_guess) == 4:        
                return numeric_guess        
                    
        else:            
            print("Please ensure to enter 4 numbers seperated by commas respresenting your 4 chosen words")

        print("")
        guess_string = input("Please try again : ")
        




# Main prog starts here
welcome()
game_board = generate_new_game()
display_game_board(game_board)
get_player_input(game_board)

    