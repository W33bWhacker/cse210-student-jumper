import random

class Word:

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Word): an instance of a Word.
        """

        self.words = []
        self.word = None

    def word_bank(self):
        """Populates 'words' attribute with list of words that can be chosen 
        at random.
        
        Args:
            self (Word): an instance of a Word.
        """

        self.words = [
            "ghost",
            "witch",
            "knife",
            "sword",
            "brain",
            "death",
            "grave",
            "candy",
            "creep",
            "crawl",
            "scare",
            "scary",
            "blood",
            "mummy",
            "haunt",
            "spook",
            "ghoul",
            "wrath",
            "devil",
            "bones",
            "demon",
            "fangs",
            "claws",
            "curse",
            "eerie",
            "magic",
            "skull",
            "spell",
            "troll",
            "panic",
            "masks",
            "treat",
            "trick"
        ]
    
    def safe_word(self):
        """Randomly generates a word from the word list that the guessee can guess.
        
        Args:
            self (Word): an instance of a Word.
        """

        self.word = random.choice(self.words)