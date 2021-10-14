'''
computing ids: upm8pb ers7hp
'''

word = input("Enter a word or phrase: ")

word = "_".join(word)+"_"


while word.find('_') != -1:
    print('The word to guess: ' + word[1:len(word):2])
    letter = input('Guess a letter: ')

    word = word.replace(letter + '_', letter + letter)

