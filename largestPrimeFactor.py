import math
def checkPrime(num):
    upper = math.sqrt(num)
    upper = int(upper)
    for i in range(2,upper+1):
        if num % i == 0:
            return False
    return True
def divideOut(num, prime):
    while num % prime == 0:
        num = num / prime
    return num
def primeDivisors(num):
    currentNum = num
    i = 2
    while i<=currentNum:
        if currentNum % i == 0:
            currentNum = divideOut(currentNum, i)
            gcd = i
        i += 1
    return gcd
print primeDivisors(600851475143)
