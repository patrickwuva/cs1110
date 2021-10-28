# Patrick Williamson:upm8pb David Peterson: ers7hp

def encrypt_chunk(chunk,key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    location = alphabet.find(chunk)

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

def decrypt(secret_text,key):
    key = 26-key
    plain_text = ''
    for i in range(0, len(secret_text)):
        chunk = secret_text[i]
        plain_text += encrypt_chunk(chunk, key)

print(encrypt('secret',9))
print(decrypt('bnlanc',26-9))




