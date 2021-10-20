# Original written by Mark Sherriff (mss2x)
# Modified and bugs introduced by Luther Tychonievich (lat7h)

'''
computing id: ers7hp upm8pb
'''
marbles = 0
pick = 0


def pow2(n):
    """Computes are returns the largest power of two that is no larger than n"""
    count = 0
    ans = 1
    while ans * 2 <= n:
        ans *= 2
        count += 1


    return count
print(pow2(5))
print("The Game of Nim\n")
while marbles <= 0:
    marbles = int(input("The number of marbles in the pile: "))
turn_choice = input("Who will start? (p or c): ")
turn = False
if turn_choice == 'p':
    turn = True

while marbles != 0:
    print("The pile has", marbles, "marbles in it.")
    while turn:
        can_take = marbles // 2
        take = 0
        while take <= can_take and turn == True:
            take = int(input("How many marbles to you want to take (1-" + str(can_take) + "): "))

            marbles -= take
            print('in while loop')
            turn = False
    else:
        take = 0
        target = pow2(marbles)
        take = marbles - (2**target -1)
        if marbles - (2**target-1) == 2**target -1:
            take = marbles - (target-1)
        else:
            take = 1
        marbles -= take
        print("The computer takes", take, "marbles.")

    turn = True

if turn:
    print("The player wins!")
else:
    print("The computer wins!")
