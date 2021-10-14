"""
Date: October 13, 2021
Author: Patrick Williamson
Computing id: ump8pb
"""


def card_to_value(card):
    '''

    :param card: given the card as a str
    :return: we return the numeric value for the card
    '''

    # first check for the smallest case, the card being an ace
    if card == 'A':
        card = 1
        return card

    # Next check if its a face card or a 10
    elif card == "K" or card == "Q" or card == "J" or card == 'T':
        card = 10
        return card

    # all other (correct) cases are equal to 2-9
    else:
        card = int(card)
        return card


def hard_score(hand):
    '''

    :param hand: given the str hand we give each card in hand a numeric value
    :return: we return the hard score (when the first ace = 1) in the variable total
    '''

    # create total variable
    total = 0

    # un a for loop that gets the total of each card in hand
    for i in range(len(hand)):
        # use the call_to_value function and string parsing to update the total
        total += card_to_value(hand[i])

        # we also want our loop to end
        i += 1
    return total


def soft_score(hand):
    '''
    :param hand: given the str hand we give each card in hand a numeric value
    :return: we return the hard score (when the first ace = 11)
    '''

    total = 0
    # find the first ace
    ace = hand.find('A')

    # this is for all cases that does not have an ace which means we can use hard_score again
    if ace == -1:
        total = hard_score(hand)


    else:
        total = 0
        i = 0
        # similar to the soft score loop except we are waiting for when the first ace comes up in the hand
        # once the ace comes we can add 11 to the total instead of 1
        for i in range(len(hand)):
            if i == ace:
                total += 11
                i += 1
            else:
                total += card_to_value(hand[i])
                i += 1

    return total
