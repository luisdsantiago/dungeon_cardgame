class Card:
    """
    This class will hold all card information:
    Instance Variables:
    name, atk, shield, heal, extra_move, draw_card, special
    """
    def __init__(self, name, atk, shield, heal, extra_move, draw_card, special):
        self.name       = name
        self.atk        = atk
        self.shield     = shield
        self.heal       = heal
        self.extra_move = extra_move
        self.draw_card  = draw_card
        self.special    = special
    
    def attack(self, Opponent):
        if Opponent.shield:
            if(Opponent.shield[0].shield <= self.atk):
                print(f"{Opponent.shield[0].name} has been destroyed!")
                Opponent.discard.append(Opponent.shield.popleft())
            else:
                Opponent.shield[0].shield -= self.atk
                print(f"{Opponent.shield[0].name} has {Opponent.shield[0].shield} shield power left.")
        else:
            if(Opponent.cur_hp < self.atk):
                Opponent.cur_hp = 0
                print(f"{Opponent.name}'s health has dropped to {Opponent.cur_hp}. {Opponent.name} is defeated.")
            else:
                Opponent.cur_hp -= self.atk
                print(f"{Opponent.name}'s health has dropped to {Opponent.cur_hp}")
        
    def cast_heal(self, Player):
        if Player.cur_hp + self.heal > Player.max_hp:
            Player.cur_hp = Player.max_hp
            print(f"{Player.name} hp is healed to max.\n{Player.name} hp is now {Player.cur_hp}.")
        else:
            Player.cur_hp += self.heal
            print(f"{Player.name} healed {self.heal} hp.\n{Player.name} hp is now {Player.cur_hp}.")
    
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
        #todo: Implement this overload in the future. Return X copies of the Card Class
        pass
    
    def __del__(self):
        #print(f"{self.name} is DELETED!")
        pass
    
    def __str__(self):
        return f"\n{self.name}:\nATK: {str(self.atk)}\nShield: {str(self.shield)}\nHeal: {str(self.heal)}\nExtra Move: {str(self.extra_move)}\
\nDraw Card: {str(self.draw_card)}\nSpecial Move: {str(self.special)}\n"
    
    def __repr__(self):
        return f"\nCard({self.name},{str(self.atk)},{str(self.shield)},{str(self.heal)},{str(self.extra_move)},{str(self.draw_card)},{str(self.special)})\n"

# Card class END HERE
#
