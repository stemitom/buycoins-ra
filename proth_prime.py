
def is_prime(num):
    if num == 2: return True
    if num < 2 or num % 2 == 0: return False
    
    sqr = int(num**0.5) + 1

    for div in range(3, sqr, 2):
        if num % div == 0:
            return False
    return True

def isPowerOfTwo(num):
    return (num and (num & (num - 1)) == False)

def proth_number(num):
    num -= 1
    k = 1

    while (k < (num//k)):
        if (num % k == 0):

            if(isPowerOfTwo(num//k)):
                return True
        k = k + 2 
    return False

def check_proth_prime(num):
    if proth_number(num):
        if is_prime(num):
            return True
        return False
    return False

print(check_proth_prime(13))