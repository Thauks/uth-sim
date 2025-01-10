from src.bet import Bet

class Player:
    def __init__(self, name, strategy, bankroll):
        self.name = name
        self.hand = []
        self.rank = None
        self.strategy = strategy
        self.bankroll = bankroll
        self.is_active = True

    def make_decision(self, phase, table):
        if self.strategy == 'Dealer':
            pass # Dealer strategy is ignored
        
        if self.strategy == 'Dumb':
            pass
        
        if self.strategy == 'Standard':
            pass
        
        if self.strategy == "AI":
            pass
