def factorSum(n):
    factors = [1]
    for i in range(2, n//2+1):
        if n % i == 0:
            factors.extend([i, n//i])

    uniqFactors = []
    for i in factors:
        if i not in uniqFactors:
            uniqFactors.append(i)
    return sum(uniqFactors)


tot = 0
for i in range(1, 10000):
    if i != factorSum(i) and i == factorSum(factorSum(i)):
        print(i)
        tot += i

print(tot)
