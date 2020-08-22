from enum import IntEnum, unique


@unique
class Suit(IntEnum):
    DIAMONDS = 1,
    HEARTS = 2,
    CLUBS = 3,
    SPADES = 4


class Card:
    def __init__(self, suit: Suit, rank: int):
        if rank < 2 or rank > 14:
            print('Invalid rank')
            return
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        if self.rank == 11:
            r = 'J'
        elif self.rank == 12:
            r = 'Q'
        elif self.rank == 13:
            r = 'K'
        elif self.rank == 14:
            r = 'A'
        else:
            r = self.rank

        return str(r) + ' of ' + self.suit.name

    def __eq__(self, other) -> bool:
        return self.rank == other.rank and self.suit == other.suit
