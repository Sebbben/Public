def mult3and5(r):
  tot = 0
  for i in range(3,r,3):
    tot+=i
  for i in range(5,r,5):
    if i % 3 != 0:
      tot+=i
  return tot

import time
start_time = time.time()
print(mult3and5(1000))
print("--- %s seconds ---" % (time.time() - start_time))