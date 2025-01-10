from dataclasses import dataclass

@dataclass
class Bet:
    ante: int = 0
    blind: int = 0
    trips: int = 0
    play: int = 0