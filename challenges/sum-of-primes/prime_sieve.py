# Prime Number Sieve
# http://inventwithpython.com/hacking (BSD Licensed)


"""
``` A prime number is an integer (that is, a whole number) 
    that is greater than 1 and has only two factors: 1 and itself. 
    Remember that the factors of a number are the numbers that 
    can be multiplied to equal the original number. 
    The numbers 3 and 7 are factors of 21. 
    The number 12 has factors 2 and 6, but also 3 and 4.```

source: 
https://inventwithpython.com/hacking/chapter23.html
"""

import math

def is_prime(num):
    """Divide test algorithm"""
    # Returns True if num is a prime number, otherwise False.
    # Note: Generally, isPrime() is slower than primeSieve().
    # all numbers less than 2 are not prime
    if num < 2:
        return False

    # see if num is divisible by any number up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def prime_sieve(sieveSize):
    """Sieve of Eratosthenes Algorithm"""

    # Returns a list of prime numbers calculated using
    # the Sieve of Eratosthenes algorithm.

    sieve = [True] * sieveSize
    sieve[0] = False # zero and one are not prime numbers
    sieve[1] = False

    # create the sieve
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i

    # compile the list of primes
    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)

    return primes