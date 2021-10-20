# Original written by Mark Sherriff (mss2x)
# Modified and bugs introduced by Luther Tychonievich (lat7h)

'''
computing id: ers7hp upm8pb
'''
marbles = 0
pick = 0


def pow2(n):
    """Computes are returns the largest power of two that is no larger than n"""

    ans = 1
    while ans <= n:
        ans = ans *2

    ans = ans//2 // 2

    return ans
print(pow2(7))
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
        if take < can_take:
            take = int(input("How many marbles to you want to take (1-" + str(can_take) + "): "))

            marbles -= take
            print('in while loop')
            turn = False
    else:
        take = 1
        target = pow2(marbles)
        take = marbles - target
        if target - 2  > 1:
            take = 1
        marbles -= take
        print("The computer takes", take, "marbles.")

    turn = True

if turn:
    print("The player wins!")
else:
    print("The computer wins!")
