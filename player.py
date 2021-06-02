from collections import deque

class Player:
    """This class will control their Hero classes"""
    
    def __init__(self, name, shield, hand, discard, cur_hp = 10, max_hp = 10):
        self.name    = name
        self.cur_hp  = cur_hp
        self.max_hp  = max_hp
        self.shield  = shield
        self.hand    = hand
        self.discard = discard
        
    def draw_card(self):
        self.hand.append(self.deck.deck.popleft())
    
    def play_card(self, Card, Opponent=None):
        """ In: Card being used,
                Opponent chosen
            Out: Dependant on Card stats
            Description:
        """
        card_index = self.get_card_index(self.hand, Card)
        
        if self.hand[card_index].special:
            self.hand[card_index].cast_special
        else:
            if self.hand[card_index].atk > 0:
                self.hand[card_index].attack(Opponent)
            if self.hand[card_index].shield > 0:
                self.hand[card_index].add_shield(self)
            if self.hand[card_index].heal > 0 and self.cur_hp < self.max_hp:
                self.hand[card_index].cast_heal(self)
            if self.hand[card_index].extra_move > 0:
                self.hand[card_index].gain_extra_move(self)
            if self.hand[card_index].draw_card > 0:
                self.hand[card_index].draw_extra_cards(self)
        
    def choose_hero(self, Deck):
        self.deck = Deck
    
    def show_deck(self):
        if self.deck:
            for card in self.deck:
                print(f"{card} in deck.")
        else:
            print(f"Deck is empty! Shuffling Discard pile for use now.")
    
    def show_hand(self):
        if self.hand:
            for card in self.hand:
                print(f"{card} in hand.")
        else:
            print(f"Hand is empty! Draw two cards.")
            
    def show_shields(self):
        if self.shield:
            for card in self.shield:
                print(f"{card} in shields.")
        else:
            print(f"No shields present.")
    
    def show_discard(self):
        if self.discard:
            for card in self.discard:
                print(f"{card} in discard pile.")
        else:
            print(f"Nothing in discard pile.")
            
    def get_card_index(self, Hand, Card):
        for card in Hand:
            if card.name == Card.name:
                return Hand.index(card)
            
    def __str__(self):
        pass
    
    def __repr__(self):
        pass

# Player class ENDS HERE
#
