from src.uth import UTH
from src.player import Player

def main():
    
    dealer = Player("Dealer", "Dealer")
    
    players = [
        Player("Thauks", "Standard"),
    ]
    
    
    game = UTH(players)
    game.set_dealer(dealer)
    
    game.play_round()

if __name__ == "__main__":
    main()
