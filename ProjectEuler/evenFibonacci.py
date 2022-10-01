def evenFibonacci(r):
    even = []
    last = 1
    i = 1
    while i < r:
        if i%2 == 0:
            even.append(i)
        tmp = i
        i += last
        last = tmp
    tot = 0
    for i in even:
        tot += i
    return tot
        
print(evenFibonacci(4000000))