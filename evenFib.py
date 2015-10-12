
seed1 = 1
seed2 = 1
fib = 0
sum = 0
while fib<4000000:
    fib = seed1 + seed2

    seed2 = seed1
    seed1 = fib
    if fib % 2 == 0:
        print fib
        sum = sum + fib
print sum
