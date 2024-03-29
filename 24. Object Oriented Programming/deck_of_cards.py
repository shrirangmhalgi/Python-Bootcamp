from random import shuffle

class Card:    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    _suit = ("Hearts", "Diamonds", "Clubs", "Spades")
    _value = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        
    def __init__(self):
        self.cards = [Card(suit, value) for suit in self._suit for value in self._value]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def __iter__(self):
        return iter(self.cards)

    def _deal(self, number_of_cards):
        count = min((self.count(), number_of_cards))

        if not count:
            raise ValueError("Cannot remove cards from empty deck...")

        cards = self.cards[-count:]
        self.cards = self.cards[:-count]
        return cards
        
    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, number_of_cards):
        return self._deal(number_of_cards)

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full deck of cards can be shuffled")
        shuffle(self.cards)
        return self

