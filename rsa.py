import crypto as cipher

e = 0
d = 0
public_key = 0


# function that finds common factors
def findCommonFactors(a, b):
    n = []
    for i in range(1, min(a, b) + 1):
        if a % i == b % i == 0:
            n.append(i)
    return n


# finding factors use
def findFactors(k):
    i = 0
    good_nums = []
    for i in range(1, k):
        n = findCommonFactors(k, i)
        i += 1
        if len(n) == 1:
            good_nums.append(i - 1)

    return good_nums


# function that makes the private pairs

def createKeys(p, q):
    global e
    global d
    global public_key
    # make the public key

    # make k for finding the private values
    k = (p - 1) * (q - 1)

    good_numbers = findFactors(k)

    check = 0

    i = 100
    j = 100
    while check != 1:
        check = (good_numbers[i] * good_numbers[j]) % k
        # print(good_numbers[i],good_numbers[j])
        if check == 1:
            e = good_numbers[i]
            d = good_numbers[j]
        j += 1
        if good_numbers[i] == good_numbers[j]:
            j += 1
        if j == len(good_numbers):
            i += 1
            j = 0


    public_key = p*q
    return e, d, public_key


def encryptMessage(private_key1, message, public_key):
    # encrypt
    secret_message = (message ** private_key1) % public_key

    return secret_message


def decryptMessage(secret_message, private_key2, public_key):

    # decrypt use secret message and second private key
    message = (secret_message ** private_key2) % public_key

    return message


plain_message = cipher.encrypt('hellohowareyou',3)

print('mesage encryped :'+plain_message)

