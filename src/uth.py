from deuces import Deck, Evaluator

class UTH:
    def __init__(self, players):
        self.num_players = len(players)
        self.players = players
        self.deck = Deck()
        self.evaluator = Evaluator()
        self.community_cards = []
        self.round = 0
        self.game_rounds = 0
        self.dealer = None

    def set_dealer(self, dealer):
        self.dealer = dealer

    def deal_cards(self):
        """Deals hole cards to each player and the dealer."""
        for player in self.players:
            player.set_hand([self.deck.draw(1), self.deck.draw(1)])
        self.dealer.set_hand([self.deck.draw(1), self.deck.draw(1)])

    def bet_round(self):
        """Players make decisions based on the round and community cards."""
        other_hands = [player.get_hand() for player in self.players if player != self.dealer]
        for player in self.players:
            if player.get_status() == "active":
                player.make_decision(self.round, self.community_cards, self.num_players, other_hands, self.game_rounds)

    def deal_community_cards(self, num_cards):
        """Deals community cards and adds them to the table."""
        self.community_cards.extend(self.deck.draw(num_cards))
    
    def evaluate_hands(self):
        """Evaluates and compares all player hands against the dealer."""
        dealer_rank = self.evaluator.evaluate(self.dealer.get_hand(), self.community_cards)
        dealer_rank_class = self.evaluator.get_rank_class(dealer_rank)
                
        for player in self.players:
            player_rank = self.evaluator.evaluate(player.get_hand(), self.community_cards)
            player_rank_class = self.evaluator.get_rank_class(player_rank)
            payout = self.calculate_payout(player_rank, player_rank_class, player.get_bet(), dealer_rank, dealer_rank_class)
            player.bankroll += payout

    def calculate_payout(self, player_rank, player_rank_class, bet, dealer_rank, dealer_rank_class):
        """Calculates the payout based on bets and ranks."""
        amount = 0
        amount += self._trips_payout(player_rank_class, bet.trips)
        amount += self._ante_payout(player_rank, bet.ante, dealer_rank)
        amount += self._blind_payout(player_rank, bet.blind, dealer_rank)
        amount += self._play_payout(player_rank, bet.play_bets, dealer_rank)
        return amount

    def _trips_payout(self, player_rank_class, trips_bet):
        """Calculates trips payout based on player rank."""
        amount = 0
        
        if trips_bet == 0:
            return amount
        
        payouts = {
            "Royal Flush": 50,
            "Straight Flush": 40,
            "Four of a Kind": 20,
            "Full House": 7,
            "Flush": 6,
            "Straight": 5,
            "Three of a Kind": 3
        }
        
        hand_class = self.evaluator.class_to_string(player_rank_class)
        amount += payouts.get(hand_class, 0) * trips_bet      
        return amount

    def _ante_payout(self, player_rank, ante_bet, dealer_rank):
        """Calculates ante payout based on player and dealer ranks."""
        # Add ante payout logic here
        return 0

    def _blind_payout(self, player_rank, blind_bet, dealer_rank):
        """Calculates blind payout based on player and dealer ranks."""
        return 0

    def _play_payout(self, player_rank, play_bet, dealer_rank):
        """Calculates play payout based on player and dealer ranks."""
        # Add play payout logic here
        return 0

    def reset_game(self):
        """Resets the deck, community cards, and player statuses for a new game."""
        self.deck = Deck()
        self.community_cards = []
        self.round = 0
        for player in self.players:
            player.reset()

    def play_round(self):
        """Manages the flow of a single round."""
        self.reset_game()
        self.deal_cards()
        self.bet_round()
        self.deal_community_cards(3)  # Flop
        self.bet_round()
        self.deal_community_cards(2)  # Turn and River
        self.bet_round()
        self.evaluate_hands()
        self.game_rounds += 1
