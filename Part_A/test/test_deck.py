import unittest
from deck import Deck
from card import Card, Suit


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def seed_two_cards(self):
        four_of_clubs = Card(Suit.CLUBS, 4)
        self.deck.add_after(None, four_of_clubs)
        j_of_diamonds = Card(Suit.DIAMONDS, 11)

        return self.deck.add_before(Card(Suit.CLUBS, 4), j_of_diamonds)

    def seed_three_cards(self):
        four_of_clubs = Card(Suit.CLUBS, 4)
        self.deck.add_after(None, four_of_clubs)
        j_of_diamonds = Card(Suit.DIAMONDS, 11)
        self.deck.add_before(Card(Suit.CLUBS, 4), j_of_diamonds)
        five_of_spades = Card(Suit.SPADES, 5)

        return self.deck.add_after(Card(Suit.CLUBS, 4), Card(Suit.SPADES, 5))

    def test_deck_is_initially_empty(self):
        self.assertTrue(self.deck.is_empty())

    def test_four_of_clubs_is_added(self):
        four_of_clubs = Card(Suit.CLUBS, 4)
        added = self.deck.add_after(None, four_of_clubs)

        self.assertTrue(added)
        self.assertIsNotNone(self.deck.head)
        self.assertEqual(self.deck.head.card, four_of_clubs)

    def test_j_of_diamonds_is_added_before_four_of_clubs(self):
        added = self.seed_two_cards()

        self.assertTrue(added)
        self.assertIsNotNone(self.deck.head)
        self.assertEqual(self.deck.head.card, Card(Suit.DIAMONDS, 11))
        self.assertIsNotNone(self.deck.head.next)
        self.assertIsNotNone(self.deck.tail)
        self.assertEqual(self.deck.tail.card, Card(Suit.CLUBS, 4))

    def test_five_of_spades_is_added_after_four_of_clubs(self):
        added = self.seed_three_cards()

        self.assertTrue(added)
        self.assertIsNotNone(self.deck.head)
        self.assertEqual(self.deck.head.card, Card(Suit.DIAMONDS, 11))
        self.assertIsNotNone(self.deck.tail)
        self.assertEqual(self.deck.tail.card, Card(Suit.SPADES, 5))

    def test_four_of_clubs_is_deleted(self):
        self.seed_three_cards()

        deleted = self.deck.delete(Card(Suit.CLUBS, 4))

        self.assertTrue(deleted)
        self.assertIsNotNone(self.deck.head)
        self.assertEqual(self.deck.head.card, Card(Suit.DIAMONDS, 11))
        self.assertIsNotNone(self.deck.tail)
        self.assertEqual(self.deck.tail.card, Card(Suit.SPADES, 5))
        self.assertEqual(self.deck.head.next.card, Card(Suit.SPADES, 5))

    def test_five_of_spades_is_found(self):
        self.seed_three_cards()

        found_five_of_spades = self.deck.find(Card(Suit.SPADES, 5))

        self.assertIsNotNone(found_five_of_spades)
        self.assertEqual(found_five_of_spades.card, Card(Suit.SPADES, 5))

    def test_traverse_backwards_returns_all_cards(self):
        self.seed_three_cards()

        all_cards = self.deck.traverse_backwards()

        self.assertEqual(len(all_cards), 3)
