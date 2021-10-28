#i want to make a key based encryption program

import random
import string
key = ''
secret_text_list = []


def encrypt_chunk(chunk):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    location = alphabet.find(chunk)
    if location y >= 26:
        newstart= (location+private_key)%26
        cyphered_chunk=alphabet[newstart]

        return alphabet.find(cyphered_chunk)

    cyphered_chunk = alphabet[location+private_key]

    return alphabet.find(cyphered_chunk)

def encrypt(plain_text):
    global secret_text_list

    secret_text_list = []
    for i in range(0, len(plain_text)):
        chunk = plain_text[i]
        secret_text_list.append(str(encrypt_chunk(chunk, private_key)))

   # secret_text = ''.join(secret_text)
    secret_text = ''.join(secret_text_list)
    return secret_text


def decrypt(secret_text,list,):

    return secret_text

print(secret_text)

'''
alphabet = list("qbjwuclyirkdshegnmvpoaxztf")
random.shuffle(alphabet)

alphabet = ''.join(alphabet)
'''
