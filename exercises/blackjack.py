"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


from re import L


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """
    if card in ["J", "Q", "K"]:
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """

    value_c1 = value_of_card(card_one)
    value_c2 = value_of_card(card_two)

    if value_c1 == value_c2:
        return (card_one, card_two)
    elif value_c1 > value_c2:
        return card_one
    elif value_c1 < value_c2:
        return card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 11 (if already in hand); numerical value otherwise.
    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    if "A" in [card_one, card_two]:
        return 1
    else:
        value_c1 = value_of_card(card_one)
        value_c2 = value_of_card(card_two)

        if value_c1 + value_c2 <= 10:
            return 11
        else:
            return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    sum = 0
    if card_one == "A":
        sum += 11
    if card_one in ["10", "J", "Q", "K"]:
        sum += 10
    if card_two == "A":
        sum += 11
    if card_two in ["10", "J", "Q", "K"]:
        sum += 10

    return sum == 21


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)
    return v1 == v2


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)
    return 8 < (v1 + v2) < 12
