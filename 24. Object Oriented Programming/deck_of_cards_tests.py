from deck_of_cards import Card
from deck_of_cards import Deck
import unittest

class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "A")

    def test_init(self):
        """Cards should have a suit and a value..."""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        """"repr should return a string of the form VALUE of SUIT"""
        self.assertEqual(repr(self.card), "A of Hearts")

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """deck should have a card attribute which is a list"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    def test_count(self):
        """count should return the count of cards"""
        self.assertEqual(len(self.deck.cards), 52)
        self.deck.cards.pop()
        self.assertEqual(len(self.deck.cards), 51)
    
    def test_deal_sufficient_cards(self):
        """deck should deal the number of cards specified"""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(len(self.deck.cards), 42)

    def test_deal_insufficient_cards(self):
        """deck shouldnt deal the number of cards """
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self):
        """deck should raise the value error """
        cards = self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_card(self):
        """it should deal the last card"""
        last_card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(last_card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        """it should deal the hand of cards"""
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)

    def test_shuffle_full_deck(self):
        """shuffle should return the deck if the deck is full"""
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

    def test_shuffle_not_full_deck(self):
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()   

if __name__ == "__main__":
    unittest.main()