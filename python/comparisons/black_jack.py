"""Here's your stupid docstring
    purpose: clutter the hell out of the program when the purpose is simple
"""

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.
    """

    number = [str(_) for _ in range(2, 11)]
    face = ["J", "Q", "K"]
    ace = ["A"]
    if card in number: return int(card)
    if card in face: return int(10)
    if card in ace: return int(1)
    raise ValueError("Not a valid card.")

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.
    """
    if value_of_card(card_one) > value_of_card(card_two):
        return str(card_one)
    if value_of_card(card_one) < value_of_card(card_two):
        return str(card_two)
    return (card_one, card_two)

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.
    """
    holding_ace = card_one == "A" or card_two == "A"
    combined_value = value_of_card(card_one) + value_of_card(card_two)
    if combined_value >= 11 or holding_ace: return int(1)
    return int(11)


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).
    """
    if (card_one == "A" and value_of_card(card_two) == 10) or (value_of_card(card_one) == 10 and card_two == "A"): return True
    return False

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    if value_of_card(card_one) == value_of_card(card_two): return True
    return False

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    combined_value = value_of_card(card_one) + value_of_card(card_two)
    double_down_value = list(range(9, 12))
    if combined_value in double_down_value: return True
    return False
