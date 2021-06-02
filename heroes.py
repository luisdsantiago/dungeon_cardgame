import random
from collections import deque
from dungeon_cardgame import Card

class Lia:
    """This class holds all control for the Hero Lia's Deck"""
    
    def __init__(self):
        self.deck = deque(
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

class Sutha:
    """This class holds all control for the Hero Sutha's Deck"""
    
    def __init__(self):
        self.deck = deque(
        [Card("Divine Inspiration2",0,0,2,0,0,True),
         Card("Banishing Smite2",0,0,0,1,0,True),
         Card("Divine Smite2",3,0,1,0,0,False),
         Card("Fighting Words2",2,0,1,0,0,False),
         Card("For The Most Justice2",3,0,0,0,0,False),
         Card("For Even More Justice2",2,0,0,0,0,False),
         Card("For Justice2",1,0,0,1,0,False),
         Card("Finger-Wag of Judgment2",0,0,0,2,0,False),
         Card("Divine Shield2",0,3,0,0,0,False),
         Card("Fluffy2",0,2,0,0,0,False),
         Card("Spinning Parry2",0,1,0,0,1,False),
         Card("High Charisma2",0,0,0,0,2,False),
         Card("Cure Wounds2",0,0,1,0,2,False)]
        )
    
    def suthas_special(self, Opponent):
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
    
# Sutha class ENDS HERE
#
