import math

def indivisible(n, primes):
    for i in range(len(primes)):
        if n % primes[i] == 0:
            #print primes[i], n, "primes[i], num"
            return False
    return True

def sieve(primes):
    nums = []
    lower = primes[len(primes)-1]
    upper = lower*10
    #print lower, upper, primes,
    for i in range(lower, upper):
        if indivisible(i, primes):
            yield i


def nextPrime(primes):
    for i in sieve(primes):
        #if checkPrime(i):
            #return i
        if indivisible(i,primes):
            return i

#print(nextPrime([2,3,5,7]))

def returnNthPrime(n):
    primes = [2,3,5,7]
    while len(primes) < n:
        primes.append(nextPrime(primes))
    return primes[n-1]

print(returnNthPrime(100000))
