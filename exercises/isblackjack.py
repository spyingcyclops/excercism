def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """

    #     sum = 0
    #     if card_one == "A":
    #         sum += 11
    #     elif card_one in ["10", "J", "Q", "K"]:
    #         sum += 10
    #     elif card_two == "A":
    #         sum += 11
    #     elif card_two in ["10", "J", "Q", "K"]:
    #         sum += 10
    #     if sum == 21:
    #         return True

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


print(is_blackjack("10", "A"))
