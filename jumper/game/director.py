from game import Guesser
from game import Word
from game import Picture 

def __init__(self):
    """ the class constructor.
    args: 
        self (director): an instance of Director.
    """
    self.picture = Picture()
    self.word = Word()
    self.keep_playing = True
    self.guesser = Guesser()
    self.lives = 0

def start_game(self):
    """ starts game so it plays
    args:
        self(director): an instance of Director.
        
    """ 
    while self.keep_playing:
        self.do_updates()
        self.do_outputs()


def do_updates(self):
    """ determines if guess is correct or not, adjusts 
        lives accordingly and maintains prints of picture
    args: 
        self(director): an instance of director

    """ 
    counter = 0
    list_safe = []
    self.list_guess = ["_", "_", "_", "_", "_"]
    for x in self.word.safe_word:
        list_safe.append(x)

    if self.guess.make_guess not in list_safe: 
        self.lives =+ 1

    for i in list_safe:
        if self.guesser.make_guess != i:
            list_guess[counter]="_"
            counter += 1
        else:
            list_guess[counter] = i
            counter += 1
        return self.list_guess

def do_outputs(self):
    """  prints guess marks gets the picture from picture
    args:
        self(director): an instance of director
    """ 
    print(self.list_guess[:5])
    self.picture.showpicture(lives)

def keep_playing(self):
    """ keeps the game going while lives != 4
        args:
            self(director) an instance of director
    """ 
    if self.lives == 4:
        self.keep_playing = False
        food = print("you lost loser")
        return food
    elif "_" not in self.list_guess:
        self.keep_playing = False
        food = print("you won buddy you lived")
        return food