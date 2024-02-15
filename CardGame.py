#####################################################################
# author:      Danison Zhang    
# date:       2/12/24
# description: program 7
#####################################################################

import random
import os

# define the possible suits that the cards can have using a list.
POSSIBLESUITS = ["clubs", "diamonds", "hearts", "spades"]

class Card:
    
    def __init__(self, number: int, suit: str):
        self.number = number
        self.suit = suit
    
    @property
    def number(self) -> int:
        return self._number
    
    @number.setter
    def number(self, value) -> None:
        if 2 <= value <= 10 and isinstance(value, int):
            self._number = value
        else:
            self._number = 2
    
    @property
    def suit(self) -> str:
        return self._suit
    
    @suit.setter
    def suit(self, value) -> None:
        if value.lower() in POSSIBLESUITS:
            self._suit = value
        else:
            self._suit = "clubs"
            
    # operator overloading
    
    def __str__(self):
        return f"{self.number} of {self.suit}"
    
    def __eq__(self, other: "Card") -> bool:
        if self.number == other.number:
            return True
        return False
        
    def __gt__(self, other: "Card") -> bool:
        if self.number > other.number:
            return True
        return False
        
    def __lt__(self, other: "Card") -> bool:
        if self.number < other.number:
            return True
        return False

class Deck():
    
    def __init__(self):
        self.cards = self.populate()
                
    @property
    def cards(self) -> list:
        return self._cards
        
    @cards.setter
    def cards(self, value) -> None:
        self._cards = value
    
    def __str__(self):
        if len(self.cards) == 0:
            return "[--empty--]"
        else:
            result = "["
            for card in self.cards:
                result += f'{card}, '
            result +="]"
            return result
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        if len(self.cards) == 0:
            return None
        else:
            c = self.cards[0]
            del self.cards[0]
            return c
    
    def size(self) -> int:
        return len(self.cards)
        
    def populate(self):
        list = []
        for i in range(2, 11):
            for type in POSSIBLESUITS:
                image = f'{i}_of_{type}.png'
                list.append(PictureCard(i, type, image))
        return list
                
    def reset(self):
        self.cards = self.populate()

class PictureCard(Card):
    
    def __init__(self, number, suit, imagefile: str):
        super().__init__(number, suit)
        self.imagefile = imagefile
    
    @property
    def imagefile(self) -> str:
        return self._imagefile
    
    @imagefile.setter
    def imagefile(self, value):
        p = './images/'
        if os.path.isfile(f'{p}{value}'):
            self._imagefile = value
        else:
            self._imagefile = 'default.png'
    
    def __str__(self):
        return f'{self.imagefile}'

class Game:
    
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.shuffle()
    
    @property
    def deck(self) -> "Deck":
        return self._deck
    
    @deck.setter
    def deck(self, value) -> None:
        self._deck = value
        
