def numberSpiralDiagonal(size):
  tot = 0
  biggestNum = size**2
  i = 1
  jumpAmt = 2
  counter = 0
  while i <= biggestNum:
    tot += i
    print(i, tot)
    i += jumpAmt
    counter += 1
    if counter == 4:
      jumpAmt += 2
      counter = 0
  return tot




print(numberSpiralDiagonal(1001))