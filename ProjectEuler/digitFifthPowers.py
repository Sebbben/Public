nums = []

for i in range(10,1000000):
  strnum = str(i)
  s = 0
  for j in strnum:
    s += int(j)**5
  if s == i:
    nums.append(i)

print(nums)
print(sum(nums))
