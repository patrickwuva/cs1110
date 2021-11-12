"""
Author: Patrick Williamson
Date: November 6th, 2020
Computing Id: Upm8pb
"""

states_winner = {}


def add_state(name, vote):
    """
    :param name: Name of the state
    :param vote: A dictionary of the Candidates and their vote count
    :return: returns a dictionary of the state name and the candidates and their votes
    """
    global states_winner
    states = {}
    states[name] = vote

    # make a list of votes and order it so we know which number is higher
    votes_list = list(vote.values())
    votes_list.sort()

    # make a list of names
    names_list = list(vote.keys())

    # We need to find the winner from each added state so we make a for loop that finds whcih
    for i in range(len(names_list)):
        # finding the name in the dictionary from the names_list and adding it to the winner dictionary
        if states[name][names_list[i]] == votes_list[-1]:
            states_winner[name] = names_list[i]

    return states


def winner(college):
    """
    :param college: given the college dictionary and the global state_winner
    :return: return the winner
    """
    global states_winner
    total = 0

    # if there are no votes that means no winner
    if states_winner == {}:
        return "No Winner"

    # I made a helper function to remove states that are not on the electoral college list
    remove_bad_states(college)

    # create the votes dict which is the names of the candidates who won
    votes = {}
    for values in states_winner:
        votes[states_winner.get(values)] = 0

    # create a list of the names so we can use it to find the winners
    names = list(states_winner.values())

    # for loop that appends the votes dict to update it with the votes
    i = 0
    for keys in states_winner:
        votes[names[i]] += college.get(keys)
        i += 1

    # getting a list of the keys in votes to make the for loop easy
    names = list(votes.keys())

    # lets get the total first using a for loop to find the total
    for i in range(len(names)):
        total += votes[names[i]]

    # now we check to see if one of the candidates got more votes than 50% of the total
    for keys in votes:
        if votes[keys] > total * .5:
            return keys

    # if there is not majority winner return no total
    return 'No Winner'


def remove_bad_states(college):
    """
    :param college: using the electoral college votes dict
    :return: update the state_winners dictionary with only states that are mentioned in the college dictionary
    """

    value = list(states_winner.keys())
    i = 0

    # a for loop that checks to see if there is a state winner that is not in the college dictionary
    for key in list(states_winner):
        if college.get(value[i]) is None:

            # removing that state from the winner states dictionary
            del states_winner[key]
        i += 1


def clear():
    """
    :return: clears the states_winner
    """
    global states_winner
    states_winner = {}
    return states_winner
