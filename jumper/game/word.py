import random

class Word:

    def __init__(self):

        self.words = []
        self.word = None

    def word_bank(self):

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

        self.word = random.choice(self.words)