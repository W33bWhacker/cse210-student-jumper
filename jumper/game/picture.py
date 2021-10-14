class Picture():

    def __init__(self):
        self.picture = ["  ___", "/_____\\", "\\     /", "  \\ /", "   O", "  /|\\", "  / \\"]


    def showPicture(self, lives):
        """prints picture of player's current state
        args: lives(int), lives taken from player for incorrect guesses, determines how much of the parachute prints
        """
        if(lives < 4):
            while lives < len(self.picture):
                print(self.picture[lives])
                lives += 1
        else:
            print()

            print("  ________ ")
            print(" /        \\")
            print("|    RIP   |")
            print("|    ~~~   |")
            print("|          |")
            print("|          |")
            print("| @  @  @  |")
            print("---\\-|-/------")