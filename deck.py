from card import Card


class Deck:

    def __init__(self) -> None:
        deck: list[Card] = []
        suits = ("Hearts", "Diamonds", "Spades", "Clubs")
        values = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

        for suit in suits:
            for value in values:
                deck.append(Card(suit, value))

        self.deck = deck
