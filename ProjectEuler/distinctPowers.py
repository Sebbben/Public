nums = []

for a in range(2,101):
  for b in range(2,101):
    prod = a**b
    if prod not in nums:
      nums.append(prod)

print(len(nums))