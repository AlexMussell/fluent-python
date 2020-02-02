import unittest
from part_one_prologue.chapter_one_python_data_model.french_deck import FrenchDeck, Card

class TestFrenchDeck(unittest.TestCase):
    
    def test_deck_len(self):
        deck = FrenchDeck()
        self.assertEqual(len(deck), 52)

    def test_deck_card(self):
        deck = FrenchDeck()
        self.assertEqual(deck[0], Card(rank='2', suit='spades'))
 
    def test_deck_card_minus(self):
        deck = FrenchDeck()
        self.assertEqual(deck[-1], Card(rank='A', suit='hearts'))

    def test_deck_slice(self):
        deck = FrenchDeck()
        self.assertEqual(deck[:3], [Card(rank='2', suit='spades'),
                                    Card(rank='3', suit='spades'),
                                    Card(rank='4', suit='spades')])

    def test_deck_get_aces(self):
        deck = FrenchDeck()
        self.assertEqual(deck[12::13], [Card(rank='A', suit='spades'),
                                        Card(rank='A', suit='diamonds'),
                                        Card(rank='A', suit='clubs'),
                                        Card(rank='A', suit='hearts')]) 

    def test_card_in_deck(self):
        deck = FrenchDeck()
        self.assertIn(Card(rank='Q', suit='hearts'), deck)

    def test_card_not_in_deck(self):
        deck = FrenchDeck()
        self.assertNotIn(Card(rank='Q', suit='whopper'), deck)


if __name__ == "__main__":
    unittest.main()