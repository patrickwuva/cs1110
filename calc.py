"""
Author: Patrick Williamson
Computing id: upm8pb
Date: Wed October 6th
"""

current_value = 0
step_count = 0
recent_operation = ""
operation_output = "0"
add_operation = ''
recent_number = ''
original_value = current_value


def get_value():
    """

    :return: returnst the current value, which is the current output of the calculator
    """
    return current_value


def clear(number=0):
    """

    :param number: gets an optional int that replaces the current value
    :return: either the numebr inputed or by default 0
    """
    global operation_output
    global original_value
    global recent_operation
    global add_operation
    global current_value
    global step_count
    current_value = int(number)
    operation_output = str(number)
    recent_operation = ''
    add_operation = ''
    step_count = 0
    original_value = current_value

    return current_value


def step(o, n):
    """

    :param o: a str value + - // *
    :param n: the number that the current_value will be multiplied by
    :return: the answer, the new current value
    """
    global step_count
    global recent_operation
    global recent_number
    global current_value
    global original_value
    global operation_output
    global add_operation
    recent_operation = o
    recent_number = n

    if o == "+":
        current_value += n
        add_operation += str(recent_operation) + str(recent_number) + ")"
        step_count += 1

    elif o == '-':
        current_value -= n
        add_operation += str(recent_operation) + str(recent_number) + ")"
        step_count += 1

    elif o == '//':
        current_value //= n
        add_operation += str(recent_operation) + str(recent_number) + ")"
        step_count += 1

    elif o == '*':
        current_value *= n
        add_operation += str(recent_operation) + str(recent_number) + ")"
        step_count += 1

    else:
        return current_value

    operation_output = ('('*step_count) + str(original_value) + ')' + add_operation
    operation_output = operation_output[:len(operation_output)-1]

    return current_value


def repeat():
    global recent_number
    global recent_operation
    return step(recent_operation, recent_number)


def get_expr():
        return operation_output
