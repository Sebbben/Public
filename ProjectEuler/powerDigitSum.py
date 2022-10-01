def main(num, power):
    fullNum = pow(num, power)
    sum = 0
    for i in str(fullNum):
        sum += int(i)
    return sum


print(main(2, 1000))
