import random
from Collections import deque
from dungeon_cardgame.card import Card

class Lia():
    """This class holds all control for the Hero Lia's Deck"""
    
    __lias_deck = deque(
        [Card("Divine Inspiration",0,0,2,0,0,True),
         Card("Banishing Smite",0,0,0,1,0,True),
         Card("Divine Smite",3,0,1,0,0,False),
         Card("Fighting Words",2,0,1,0,0,False),
         Card("For The Most Justice",3,0,0,0,0,False),
         Card("For Even More Justice",2,0,0,0,0,False),
         Card("For Justice",1,0,0,1,0,False),
         Card("Finger-Wag of Judgment",0,0,0,2,0,False),
         Card("Divine Shield",0,3,0,0,0,False),
         Card("Fluffy",0,2,0,0,0,False),
         Card("Spinning Parry",0,1,0,0,1,False),
         Card("High Charisma",0,0,0,0,2,False),
         Card("Cure Wounds",0,0,1,0,2,False)]
    )
    
    def __init__(self):
        self.deck = self.__lias_deck
    
    def lias_special(self, Opponent):
        pass
    
    def shuffle(self):
        #tic = time.perf_counter()
        temp_list = list(self.deck)
        random.shuffle(temp_list)
        self.deck = deque(temp_list)
        #toc = time.perf_counter()
        #print(f"Shuffled the deck in {toc - tic:0.9f} seconds")
        
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
# Lia class ENDS HERE
#