from Collections import deque

class Player:
    """This class will control their Hero classes"""
    
    def __init__(self, name = "Computer", cur_hp = 10, max_hp = 10, shield = deque(), hand = deque(), discard = deque()):
        self.name    = name
        self.cur_hp  = cur_hp
        self.max_hp  = max_hp
        self.shield  = shield
        self.hand    = hand
        self.discard = discard
        
    def draw_card(self):
        self.hand.append(self.deck.deck.pop())
    
    def play_card(self, Card, Opponent):
        """ In: Card being used,
                Opponent chosen
            Out: Dependant on Card stats
            Description:
        """
        if Card.special:
            Card.cast_special
        else:
            if Card.atk > 0:
                Card.attack(Opponent)
            if Card.shield > 0:
                Card.add_shield(self)
            if Card.heal > 0 and self.cur_hp < self.max_hp:
                Card.cast_heal(self)
            if Card.extra_move > 0:
                Card.gain_extra_move(self)
            if Card.draw_card > 0:
                Card.draw_extra_cards(self)
        
    def choose_hero(self, Deck):
        self.deck = Deck
    
    def show_deck(self):
        if self.deck:
            for card in self.deck:
                print(card)
        else:
            print(f"Deck is empty! Shuffling Discard pile for use now.")
    
    def show_hand(self):
        if self.hand:
            for card in self.hand:
                print(card)
        else:
            print(f"Hand is empty! Draw two cards.")
            
    def show_shields(self):
        if self.shield:
            for card in self.shield:
                print(card)
        else:
            print(f"No shields present.")
    
    def show_discard(self):
        if self.discard:
            for card in self.discard:
                print(card)
        else:
            print(f"Nothing in discard pile.")
            
    def __str__(self):
        pass
    
    def __repr__(self):
        pass

# Player class ENDS HERE
#