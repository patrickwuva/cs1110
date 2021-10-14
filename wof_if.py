
'''
computing ids: upm8pb ers7hp
'''
word = input("Enter a word or phrase: ")

word = "_".join(word)+"_"



def guessLetter():
    '''

    this function uses the word and replaces the letter with the underline
    to get out of the loop we just quit if we can't find any underscores
    '''
    global word
    print('The word to guess: ' + word[1:len(word):2])
    letter = input('Guess a letter: ')

    word = word.replace(letter + '_', letter + letter)

    if word.find('_') == -1:
        quit
    else:
        guessLetter()

guessLetter()

