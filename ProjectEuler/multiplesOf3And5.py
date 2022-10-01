def sumMult3And5(r):
    tot = 0
    for i in range(r):
        if i % 3 == 0 or i % 5 == 0:
            tot += i
    return tot


import time
start_time = time.time()
print(sumMult3And5(1000))
print("--- %s seconds ---" % (time.time() - start_time))
