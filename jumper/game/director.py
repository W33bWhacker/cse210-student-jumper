from game.Guesser import Guesser
from game.word import Word
from game.picture import Picture

class Director:

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
        self.list_guess = []
        self.list_safe = []
        self.letter = None

    def start_game(self):
        """ starts game so it plays
        args:
            self(director): an instance of Director.
            
        """ 
        self.word.word_bank()
        self.word.safe_word()

        while self.keep_playing:
            self.do_outputs()
            self.do_updates()

    def do_updates(self):
        """ determines if guess is correct or not, adjusts 
            lives accordingly and maintains prints of picture
        args: 
            self(director): an instance of director

        """ 
        counter = 0
        self.list_guess = ["_", "_", "_", "_", "_"]
        for x in self.word.word:
            self.list_safe.append(x)

        if self.letter not in self.list_safe: 
            self.lives =+ 1

        for i in self.list_safe:
            if self.letter != i:
                self.list_guess[counter]="_"
                counter += 1
            else:
                self.list_guess[counter] = i
                counter += 1
            return self.list_guess

    def do_outputs(self):
        """  prints guess marks gets the picture from picture
        args:
            self(director): an instance of director
        """ 
        print(self.list_guess[:5])
        self.picture.showPicture(self.lives)
        self.letter = self.guesser.make_guess()
        

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