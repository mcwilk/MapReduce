import math
from functools import reduce

def is_prime(num):
    '''
    Function checks whether a given number is a prime number (if a remainder
    from any of iterations equals to 0 it means that number has a divider so
    it is not a prime number - function automatically returns 0 (False) as a
    result. Otherwise - it returns 1 (True)).
    '''
    i = 2
    s = math.sqrt(num)
    while i <= s:
        if num % i == 0:
            return 0
        else:    
            i += 1
    return 1

def mapReduce(n):
    '''
    Function generates list of following numbers (array). Next 'map' function
    executes 'is_prime' function on each number from the list and returns
    another list with values of 0 (when number is prime) and 1 (when it is not).
    The last step is a 'reduce' function which returns sum for the list returned
    by 'map' function - it is a number of primes (de facto number of 1 (Trues))
    in 'array' list.
    '''
    array = [z for z in range(2, n+1)]
    m = list(map(lambda x: is_prime(x), array))
    r = reduce(lambda a, b: a + b, m)
    return r

def main():
    n = int(input())
    print(mapReduce(n))

main()

