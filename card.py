class Card:
    """
    This class will hold all card information:
    Instance Variables:
    name, atk, shield, heal, extra_move, draw_card, special
    """
    def __init__(self, name = "", atk = 0, shield = 0, heal = 0, extra_move = 0, draw_card = 0, special = False):
        self.name       = name
        self.atk        = atk
        self.shield     = shield
        self.heal       = heal
        self.extra_move = extra_move
        self.draw_card  = draw_card
        self.special    = special
    
    def attack(self, Opponent):
        if(Opponent.cur_hp < self.atk):
            Opponent.cur_hp = 0
            print(f"{Opponent.name}'s health has dropped to {Opponent.cur_hp}. {Opponent.name} is defeated.")
        else:
            Opponent.cur_hp -= self.atk
            print(f"{Opponent.name}'s health has dropped to {Opponent.cur_hp}")
        
    def cast_heal(self, Player):
        if Player.cur_hp + self.heal > Player.max_hp:
            Player.cur_hp = Player.max_hp
            print(f"{Player.name}'s hp is healed to max. {Player.name}'s hp is now {Player.cur_hp}.")
        else:
            Player.cur_hp += self.heal
            print(f"{Player.name}'s healed {self.heal} hp. {Player.name}'s hp is now {Player.cur_hp}.")
    
    def add_shield(self, Player):
        Player.shield.append(self)
    
    def gain_extra_move(self, Player):
        pass
    
    def draw_extra_cards(self, Player):
        for _ in range(self.draw_card):
            Player.draw_card()
    
    def cast_special(self, *args):
        pass
    
    def __rmul__(self, other):
        """ Implement this overload in the future. Return X copies of the Card Class"""
        pass
    
    def __str__(self):
        return f"{self.name}:\nATK: {str(self.atk)}\nShield: {str(self.shield)}\
            \nHeal: {str(self.heal)}\nExtra Move: {str(self.extra_move)}\n\
            Draw Card: {str(self.draw_card)}\nSpecial Move: {str(self.special)}"
    
    def __repr__(self):
        return f"Card({self.name},{str(self.atk)},{str(self.shield)},\
            {str(self.heal)},{str(self.extra_move)},{str(self.draw_card)},\
                {str(self.special)})"

# Card class END HERE
#