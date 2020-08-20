from card import Card, Suit
from deck import Deck

if __name__ == "__main__":
    deck = Deck.empty()

    # Add first card, ace of spades
    deck.add_after(None, Card(Suit.SPADES, 1))

    # Add J of Diamonds before the previous one
    # It becomes the head of the deck
    deck.add_before(deck.head.card, Card(Suit.DIAMONDS, 11))

    # Add 2 of Hearts after J of Diamonds
    deck.add_after(deck.head.card, Card(Suit.HEARTS, 2))

    # Add 4 of Clubs after 2 of Hearts
    deck.add_after(Card(Suit.HEARTS, 2), Card(Suit.CLUBS, 4))

    # Add 9 of Diamonds before 2 of Hearts
    deck.add_before(Card(Suit.HEARTS, 2), Card(Suit.DIAMONDS, 9))

    # Remove 4 of Clubs from the deck
    deck.delete(Card(Suit.CLUBS, 4))

    # Try to find 4 of Clubs
    four_of_clubs = deck.find(Card(Suit.CLUBS, 4))

    # Find J of Diamonds
    j_of_diamonds = deck.find(Card(Suit.DIAMONDS, 11))

    print(f'Found 4 of Clubs? {four_of_clubs}')
    print(f'Found J of Diamonds? {j_of_diamonds}')

    # Uncomment the two lines below to get a full deck
    # deck = deck.empty()
    # deck.fill()

    """ deck.add_after(None, Card(Suit.CLUBS, 4))
    print(f'Head: {deck.head}')

    deck.add_before(Card(Suit.CLUBS, 4), Card(Suit.DIAMONDS, 11))

    print(f'Head: {deck.head}')
    print(f'Tail: {deck.tail}') """

    deck.traverse_backwards()