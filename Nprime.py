import math

def indivisible(n, primes):
    for i in xrange(len(primes)):
        if n % primes[i] == 0:
            #print primes[i], n, "primes[i], num"
            return False
    return True

#print indivisible(8, [2])
#print indivisible(7, [2])

def sieve(primes):
    nums = []
    lower = primes[len(primes)-1]
    upper = lower*10
    #print lower, upper, primes,
    for i in xrange(lower, upper):
        if indivisible(i, primes):
            yield i


def nextPrime(primes):
    for i in sieve(primes):
        #if checkPrime(i):
            #return i
        if indivisible(i,primes):
            return i

#print nextPrime([2,3,5,7])


def returnNthPrime(n):
    primes = [2,3,5,7]
    while len(primes) < n:
        primes.append(nextPrime(primes))
    return primes[n-1]

def main(n):
    res = returnNthPrime(n)
    print(res)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
