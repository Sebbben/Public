def sumSqrDiff(r):
    tot = 0
    sqrTot = 0
    for i in range(r+1):
        tot += i
        sqrTot += i**2
    print(tot**2,sqrTot)
    return tot**2 - sqrTot
    
print(sumSqrDiff(100))