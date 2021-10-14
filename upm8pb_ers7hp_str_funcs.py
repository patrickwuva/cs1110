#David Peterson, ers7hp Patrick Williamson ump8pb

def ellipsis(word):
    '''

    :param word: string, this argument will be passed
    :return: the sliced string as a new variable x
    '''

    x = word[: 2] + '..' + word[len(word) - 2:]
    return x


def eighteen(word):
    length = len(word) - 2
    x = word[:1] + str(length) + word[len(word) - 1:]
    return x


print(eighteen('computer science'))


def allit(s, t):
    '''

    :param s: first string in the frucntion
    :param t: second string in the function
    :return: true or false depending on if they are vowels or concinents 
    '''
    x = s.lower()
    y = t.lower()


    if x[0] != y[0]:
        return False

    if x[0] == y[0] and x[0] == 'a' or x[0] == 'e' or x[0] == 'i' or x[0] == 'o' or x[0] == 'u' or x[0] == 'y':
        return False

    else:
        return True



def between(p,l):
    '''

    :param p: the string that we give to be parsed based on the location of the letter
    :param l: the letter we search for in the string
    :return: the
    '''
    firstL = p.find(l)

    x = p[firstL + 1:]
    secondL = x.find(l)
    if firstL == -1:
        return '""'

    elif secondL == -1:
        return '""'

    else:
        in_between =p[firstL+1:secondL+1]
        return in_between



def rbetween(p,l):
    '''

    :param p: the string that we give to be parsed based on the location of the letter
    :param l: the letter we search for in the string
    :return: the
    '''


    firstL = p.rfind(l)

    x = p[:firstL]

    print(x)
    secondL = x.rfind(l)
    if firstL == -1:
        return '""'

    elif secondL == -1:
        return '""'

    else:
        in_between =p[secondL+len(l):firstL]
        return in_between
rbetween('loan me a lovely loon to look at','lo')
