from card import Card


class PokerGame:

    """
    The PokerGame class is designed to keep all of the data related to a game of poker. It can
    store a player's hand, the table's cards, and the deck of cards as a whole. This app is designed to calculate the odds from
    a single player's perspective, but will be allowed in the future to calculate given multiple hands.
    """

    def __str__(self):
        return_string = "Cards in your hand: \n"
        for card in self.hand:
            return_string += " - " + str(card) + "\n"
        return_string += "Cards on the table: \n"
        for card in self.table:
            return_string += " - " + str(card) + "\n"
        return_string += f"Number of players: {self.number_of_players}"
        return return_string

    def __init__(self,
                 hand: tuple[Card],
                 table: tuple[Card],
                 number_of_players: int):
        """
        This init constructor takes in two arguments, a 'hand' and a 'table.'
        The 'hand' object is assumed to be a tuple[Card] of length 2.
        The 'table' object is assumed to be a tuple[Card] of any length between 0 and 5 inclusive.
        """
        self.hand = hand
        self.table = table
        self.number_of_players = number_of_players

        self.deck = self.create_deck()

    def create_deck(self) -> tuple[Card]:
        """
        This method creates a default deck of 52 cards.
        This deck is unshuffled and the method simply returns a tuple[Card]
        """
        deck: list[Card] = []
        suits = ("Hearts", "Diamonds", "Spades", "Clubs")
        # The values above 10 are face cards and Ace
        values = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

        for suit in suits:
            for value in values:
                deck.append(Card(suit, value))
        return tuple(deck)

    def determine_hand(hand: tuple[Card], table: tuple[Card]) -> int:
        """
        This method is intended to test for hands and table cards that are already 2 and 5 cards respectively.
        These cards should already be created and put into tuples before the calling of this method. This method will return a 'rank'
        value between 1 and 10.
        The rankings are as follows, with higher cards being of better rank: \n
        1: High Card \n
        2: Pair \n
        3: Two Pair \n
        4: Three of a Kind \n
        5: Straight \n
        6: Flush \n
        7: Full House \n
        8: Four of a Kind \n
        9: Straight Flush \n
        10: Royal Flush \n
        """

        combined_hand = list(hand) + list(table)

        def has_flush():
            """
            This method determines in the combined_hand variable contains cards that are considered to
            be a Flush. This is done by counting the suits and determining if there are more than 5
            cards in any given suit.
            """
            suit_indices = {
                "Spades": 0,
                "Hearts": 1,
                "Diamonds": 2,
                "Clubs": 3
            }
            # Format: [Spades, Hearts, Diamonds, Clubs]
            suit_counts = [0, 0, 0, 0]
            for card in combined_hand:
                suit_counts[suit_indices[card.suit]] += 1
            print(suit_counts)
            for count in suit_counts:
                if count >= 5:
                    return True
            return False

        def has_straight():
            """
            This method determines if the combined_hand variable contains cards that can be considered
            a straight. It does this by determining all of the combinations of sets of values that result
            in a straight and testing for each of them, since there are only 10 of them.
            """
            values = set()
            for card in combined_hand:
                values.add(card.value)

            straight_lists = (
                {14, 2, 3, 4, 5},
                {2, 3, 4, 5, 6},
                {3, 4, 5, 6, 7},
                {4, 5, 6, 7, 8},
                {5, 6, 7, 8, 9},
                {6, 7, 8, 9, 10},
                {7, 8, 9, 10, 11},
                {8, 9, 10, 11, 12},
                {9, 10, 11, 12, 13},
                {10, 11, 12, 13, 14},
            )

            for straight in straight_lists:
                if len(values.intersection(straight)) == 5:
                    return True
            return False
