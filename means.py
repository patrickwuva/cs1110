'''
Author: Patrick Williamson
Date: October 27th 2021
Computing Id: upm8pb
'''


def mean_all(table):
    """
    :param table: given the table
    :return: we return the average of all the numbers in the table
    """

    total = 0
    for i in range(len(mean_by_col(table))):
        total += mean_by_col(table)[i]

    # for i in range(len(mean_by_col(table))):
    # total += mean_by_col(test)

    return total / len(mean_by_col(table))


def mean_by_row(table):
    """
    :param table: given the table
    :return: we want to return the mean of the numbers by the row
    """

    # set a list of the averages
    average_list = []

    # get the average by row
    for i in range(len(table)):
        total = 0

        # use a nested loop to grab each variable row by row
        for j in range(len(table[i])):
            total += table[i][j]

        # appending the average list to add the (total / the length of the row)
        average_list.append(total / len(table[i]))

    return average_list


def mean_by_col(table):
    average_list = []

    # get the average by column
    for i in range(len(table[0])):
        total = 0

        # using a nested loop to get the total column by column
        for j in range(len(table)):
            total += table[j][i]

        # appending the average list
        average_list.append(total / len(table))

    return average_list
