def isPalindrome(num):
    return str(num) == str(num)[::-1]

sum = 0

for i in range(1_000_000):
    if isPalindrome(i) and isPalindrome(str(bin(i))[2:]):
        sum += i

print(sum)