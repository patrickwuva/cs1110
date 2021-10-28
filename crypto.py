# Patrick Williamson:upm8pb David Peterson: ers7hp

def encrypt_chunk(chunk,key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    location = alphabet.find(chunk)

    if location + key >= 26:
        newstart= (location+key)%26
        cyphered_chunk=alphabet[newstart]


        return cyphered_chunk
    cyphered_chunk = alphabet[location+key]

    return alphabet.find(cyphered_chunk)


def decrypt(secret_text,key):
    plain_text = ''
    plain_text += encrypt(secret_text,26-key)

    return plain_text


def encrypt_chunk_vigenere(chunk,key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    location = alphabet.find(chunk)
    key = alphabet.find(key)
    if location + key >= 26:
        newstart= (location+key)%26
        cyphered_chunk=alphabet[newstart]


        return cyphered_chunk
    cyphered_chunk = alphabet[location+key]

    return cyphered_chunk

def encrypt(plain_text,key):
    secret_text = ''
    for i in range(0,len(plain_text)):
        chunk = plain_text[i]
        secret_text += encrypt_chunk(chunk,key)

    return secret_text

def encryptVigenere(plain_text,key):
    i = 0
    secret_text = ''

    while i <len(plain_text):
        chunk = plain_text[i]
        secret_text += encrypt_chunk_vigenere(chunk, key[0])
        i+=1
        chunk = plain_text[i]
        secret_text += encrypt_chunk_vigenere(chunk,key[1])
        i+=1
    return secret_text


def decryptVigenere(secret_text,key):
    plain_text = ''
    i = 0

    while i <len(secret_text):
        chunk = secret_text[i]
        plain_text += decrypt_chunk_vigenere(chunk, key[1])
        i+=1
        chunk = secret_text[i]
        plain_text += decrypt_chunk_vigenere(chunk,key[0])
        i+=1
    return plain_text

def decrypt_chunk_vigenere(chunk,key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    location = alphabet.find(chunk)
    key = alphabet.find(key) - 26
    if location + key >= 26:
        newstart= (location+key)%26
        cyphered_chunk=alphabet[newstart]


        return cyphered_chunk
    cyphered_chunk = alphabet[location+key]
    return cyphered_chunk
