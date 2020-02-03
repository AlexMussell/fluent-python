import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    """ Initialise a standard deck of cards

        >>> deck = FrenchDeck()
        >>> for card in deck:  # doctest: +ELLIPSIS
        ...   print(card)
        Card(rank='2', suit='spades')
        Card(rank='3', suit='spades')
        Card(rank='4', suit='spades')
        ...
    """
    
    ranks = [str(r) for r in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                            for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    import doctest
    doctest.testmod()            # Doing this means you can run doctest files with python3 french_deck.py -v
