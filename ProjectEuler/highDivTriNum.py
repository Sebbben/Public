from functools import reduce
primes = []


def highDivTriNum(targetDivisorNumber):
    f = []
    sum = 1
    counter = 1
    while True:
        f = factors(sum)
        if(len(f) >= targetDivisorNumber):
            return sum, len(f)

        counter += 1
        sum += counter


def factors(n):
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


print(highDivTriNum(500))
