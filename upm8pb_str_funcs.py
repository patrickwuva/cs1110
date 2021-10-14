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
    '''x=s.lower()
    y=s.lower()'''

    if s[0] and t[0] != 'a' or 'e' or 'i' or 'o' or 'u' or 'y' and s[0] == t[0]:
        return True

    elif s[0] and t[0] == 'a' or 'e' or 'i' or 'o' or 'u' or 'y' and s[0] == t[0]:
        return False

    elif s[0] != t[0]:
        return False


print(allit('able', 'age'))
