"""
Author: Patrick Williamson
Computing id: upm8pb
Date: Wed October 6th
"""

#global variables
step_count = 0
current_value = 0
recent_operation = ""
operation_output = "0"
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
    global recent_operation
    global current_value
    global original_value

    #making sure to reset variables to their original values
    current_value = int(number)
    operation_output = str(number)
    recent_operation = ''
    step_count = 0

    #this is used for the get_expr function
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
    recent_operation = o
    recent_number = n

    #running through the different operatior options
    if o == "+":

        #doing the math with the inputed number and the original number
        current_value += n

        #appending the operation_output string to include the new operator and recent number and the proper ) syntax
        operation_output += str(recent_operation) + str(recent_number) + ")"

    elif o == '-':
        current_value -= n
        operation_output += str(recent_operation) + str(recent_number) + ")"

    elif o == '//':
        current_value //= n
        operation_output += str(recent_operation) + str(recent_number) + ")"

    elif o == '*':
        current_value *= n
        operation_output += str(recent_operation) + str(recent_number) + ")"

    else:
        return current_value


    return current_value


def repeat():
    global recent_number
    global recent_operation
    return step(recent_operation, recent_number)


def get_expr():
    """

    :return: returns the operation_output but with some more parenthesis
    """


    #check to see if there are any )'s to remove

    if operation_output.find(')') == -1:
        return operation_output
    else:

        '''this is the final get_expr output. first adding all the ('s at the beginning of the expression by counting 
        all the iterations of )'s in the string then multiplying that number times ( Then we have to squeeze a ) 
        in between the first number and the first operator. For this we find the first ) and subtract -2 to get right 
        behind the first number with is info we use some string slicing to split the string put a ) in and then use 
        string slicing again for everything after the newly added ) '''
        return ('('*operation_output.count(')'))+operation_output[:(operation_output.find(')')-2)]+")"\
               +operation_output[operation_output.find(')')-2:len(operation_output)-1]

