def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number.
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number

    returns: integer, the secret number
    '''
    guess = 0
    while True:
        sign = isMyNumber(guess)
        if sign == 0: break
        guess -= sign
    return guess

def isMyNumber(x):
    if (x < secret_number): return -1
    if (x == secret_number): return 0
    if (x > secret_number): return 1

# testing implementation of isMyNumber
secret_number = 15
assert isMyNumber(4) is -1
assert isMyNumber(15) is 0
assert isMyNumber(25) is 1
secret_number = -15
assert isMyNumber(4) is 1
assert isMyNumber(-15) is 0
assert isMyNumber(-25) is -1

# testing implementation of jumpAndBackpedal
secret_number = 15
assert jumpAndBackpedal(isMyNumber) == 15
secret_number = -17
assert jumpAndBackpedal(isMyNumber) == -17
secret_number = 0
assert jumpAndBackpedal(isMyNumber) == 0
secret_number = 9999
assert jumpAndBackpedal(isMyNumber) == 9999