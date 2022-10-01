from math import sqrt
from itertools import count, islice

def isPrime(n):
  return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))


def isCircularPrime(num):
  num = str(num)
  for i in range(len(num)):
    if not isPrime(int(num)):
      return False
    num = num[-1]+num[:-1]
  return True

def main(r):
  cPrimes = 0
  for i in range(1,r,2):
    if not (str(i).count("2")>=1 or str(i).count("4")>=1 or str(i).count("6")>=1 or str(i).count("8")>=1):
      if isCircularPrime(i):
        cPrimes += 1
  return cPrimes+1



import time
start_time = time.time()
print(main(1000000))
print("--- %s seconds ---" % (time.time() - start_time))