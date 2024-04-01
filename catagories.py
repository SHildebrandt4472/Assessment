#  Word catagories for Connections

easy_catagories = [ 
    {"name": "Muiscal Instruments", "words": ["guitar", "piano", "violin", "drums"]},
    {"name": "Fruits",              "words": ["apple", "peach", "pear", "raspberry"]},
    {"name": "Animals",             "words": ["dog", "cat", "mouse", "lion"]},
    {"name": "Colors",              "words": ["red", "blue", "green", "yellow"]},
    {"name": "Shapes",              "words": ["circle", "square", "triangle", "rectangle"]},
    {"name": "Vehicles",            "words": ["car", "truck", "bus", "train"]},
    {"name": "Sports",              "words": ["soccer", "basketball", "football", "baseball"]},
    {"name": "Countries",           "words": ["usa", "canada", "mexico", "brazil"]},
    {"name": "Planets",             "words": ["earth", "mars", "venus", "jupiter"]},
    {"name": "Elements",            "words": ["hydrogen", "oxygen", "carbon", "nitrogen"]},
]

medium_catagories = [
    {"name": "Red things",          "words": ["chilli", "strawberry", "ruby", "firetruck"]},
    {"name": "Blue things",         "words": ["bluebottle", "ocean", "blueberry", "jeans"]},
    {"name": "Green things",        "words": ["grass", "shrub", "frog", "lettuce"]},
    {"name": "Yellow things",       "words": ["sunflower", "banana", "honey", "daffodil"]},
    {"name": "Orange things",       "words": ["orange", "pumpkin", "carrot", "tiger"]},
    {"name": "Black things",        "words": ["night", "coal", "raven", "tuxedo"]},
    {"name": "White things",        "words": ["whiteboard", "dove", "swan", "milk"]},
    {"name": "Brown things",        "words": ["chocolate", "bear", "dirt", "wood"]},
    {"name": "Gray things",         "words": ["cloud", "elephant", "rock", "pigeon"]},
    {"name": "Ways to walk",        "words": ["run", "skip", "jump", "crawl"]},
    {"name": "Things that fly",     "words": ["bird", "plane", "kite", "rocket"]},
    {"name": "Things that swim",    "words": ["fish", "whale", "submarine", "duck"]},
    {"name": "Growing things",      "words": ["tree", "flower", "child", "hair"]},
    {"name": "Hot things         ", "words": ["fire", "sun", "oven", "coffee"]},
    {"name": "Cold things         ","words": ["beer", "freezer", "penguin", "greenland"]},
    {"name": "Wet things         ", "words": ["water", "rain", "swim", "sweat"]},
    {"name": "Dry things         ", "words": ["desert", "sand", "towel", "toast"]},
    {"name": "Things that are loud","words": ["siren", "thunder", "music", "shout"]},
]

hard_catagories = [
    {"name": "Body parts plus'Y'", "words": ["army", "colony", "livery", "shiny"]},
    {"name": "Things that shrink", "words": ["ice", "cotton", "wool", "leather"]},
    {"name": "Especially",         "words": ["mighty", "pretty", "really", "very"]},
    {"name": "Kinds of blue",      "words": ["baby", "royal", "sky", "true"]},
    {"name": "Kinds of green",     "words": ["ever", "forest", "jade", "lime"]},
    {"name": "Kinds of red",       "words": ["blood", "brick", "cherry", "rose"]},
    {"name": "Kinds of purple",    "words": ["grape", "lavender", "plum", "violet"]},
    {"name": "Kinds of white",     "words": ["ivory", "snow", "vanilla", "white"]},
]

catagories = easy_catagories + medium_catagories + hard_catagories

if __name__ == "__main__":  # Test for duplicates and max word length
    max_length = 0
    for cat in catagories:
        for word in cat["words"]:
            if len(word) > max_length:  # check for max word length
                max_length = len(word)
    print("Max word length is", max_length)
    if max_length > 16:  # if too big for gameboard
        print("Max word length is too long for game board")

    check_for_duplicates = []
    for cat in catagories:
        for word in cat["words"]:
            if word in check_for_duplicates:  # check for duplicates
                print("Duplicate word", word)
            check_for_duplicates.append(word)