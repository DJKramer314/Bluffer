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
                 number_of_players: int = 2):
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

    def determine_hand(self) -> int:
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

        combined_hand = list(self.hand) + list(self.table)

        def has_flush() -> bool:
            """
            This method determines in the combined_hand variable contains cards that are considered to
            be a Flush. This is done by counting the suits and determining if there are more than 5
            cards in any given suit. It will then return True or False based on the determination.
            """
            suit_indices = {
                "Spades": 0,
                "Hearts": 1,
                "Diamonds": 2,
                "Clubs": 3
            }
            # Order: [Spades, Hearts, Diamonds, Clubs]
            suit_counts = [0, 0, 0, 0]
            for card in combined_hand:
                suit_counts[suit_indices[card.suit]] += 1
            for index in range(4):
                if suit_counts[index] >= 5:
                    return True

            # If no flushes are found
            return False

        def find_flush_suit() -> str:
            """
            This method determines which suit a flush has happened in. To do this, similarly to the has_flush() method, it counts the
            number of occurances of each suit, and returns the name of the suit that has more than 5 of it.

            For example, find_flush_suit of a combined_hand of (5s, 9s, 3s, As, Ks, 10s, 7s) would be "Spades"
            """
            suit_indices = {
                "Spades": 0,
                "Hearts": 1,
                "Diamonds": 2,
                "Clubs": 3
            }
            # Order: [Spades, Hearts, Diamonds, Clubs]
            suit_counts = [0, 0, 0, 0]
            for card in combined_hand:
                suit_counts[suit_indices[card.suit]] += 1
            for index in range(4):
                if suit_counts[index] >= 5:
                    suit_names = {
                        0: "Spades",
                        1: "Hearts",
                        2: "Diamonds",
                        3: "Clubs"
                    }
                    return suit_names[index]

            # If no flush is found within the cards
            return "No Flush"

        def has_straight(card_list=combined_hand) -> bool:
            """
            This method determines if the combined_hand variable contains cards that can be considered
            a straight. It does this by determining all of the combinations of sets of values that result
            in a straight and testing for each of them, since there are only 10 of them.

            This method takes an optional argument that allows you to test a certain set of cards for straight values.
            This functionality is only used in the has_straight_or_royal_flush() method as of now.
            """
            values = set()
            for card in card_list:
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

        def has_of_a_kind(number) -> int:
            """
            This method determines if the given cards have any _ of a kinds and if so, how many of them.
            It does this by counting the number of each card in a dictionary, similar to the flush method.
            Then, it determines which ones have exactly the number of cards specified by my input into the function.

            Example usage:
            number_of_four_of_a_kinds = has_of_a_kind(4)
            """

            number_of_solutions = 0

            card_counts = {
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0,
                8: 0,
                9: 0,
                10: 0,
                11: 0,
                12: 0,
                13: 0,
                14: 0,
            }

            for card in combined_hand:
                card_counts[card.value] += 1

            for value in card_counts:
                if card_counts[value] == number:
                    number_of_solutions += 1

            return number_of_solutions

        def has_straight_or_royal_flush() -> tuple[bool, bool]:
            """
            This method determines if the 'current_hand' variable in this class contains
            a straight flush or a royal flush. It does this by computing the cards that are involved in the flush, and then
            determining if those cards contain a straight. This method outputs a tuple of two boolean values. The first, being
            the outcome of Straight Flush and the second being the output of Royal Flush. For example, if the output is (True, True),
            This means that there is both a straight flush and a royal flush. Due to the nature of these hands, if there is a royal
            flush, there must also be a straight flush.

            Example: 
            combined_hand: 
            - 2 of Spades
            - 3 of Spades
            - 4 of Spades
            - 5 of Spades
            - 6 of Spades
            - 10 of Diamonds
            - A of Clubs

            Output:
            [True, False] -> Which means that the combined_hand has a straight flush but not a royal flush
            """
            suit = find_flush_suit()

            # This is fine being a list because it should never contain duplicate cards based on the input
            flush_cards: list[Card] = []

            for card in combined_hand:
                if card.suit == suit:
                    flush_cards.append(card)

            if has_straight(flush_cards):
                flush_card_values = set()
                for flush_card in flush_cards:
                    flush_card_values.add(flush_card.value)
                if len(flush_card_values.intersection({10, 11, 12, 13, 14})) == 5:
                    return (True, True)
                else:
                    return (True, False)
            else:
                return (False, False)

        # Begin main part of function

        if has_flush() and has_straight():
            outcome = has_straight_or_royal_flush()
            if outcome[0] and outcome[1]:
                return 10
            elif outcome[0]:
                return 9
            else:
                pass

        # Detect for four-of-a-kind
        if has_of_a_kind(4) == 1:
            return 8

        # Detect for full house
        if has_of_a_kind(3) >= 1 and has_of_a_kind(2) >= 1:
            return 7

        # Detect for flush
        if has_flush():
            return 6

        # Detect for straight
        if has_straight():
            return 5

        # Detect for three-of-a-kind
        if has_of_a_kind(3) == 1:
            return 4

        # Detect for two-pair
        if has_of_a_kind(2) == 2:
            return 3

        # Detect for one-pair
        if has_of_a_kind(2) == 1:
            return 2

        # Otherwise, high card
        return 1
