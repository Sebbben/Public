def main(rng):
    biggest = (0, 0)
    for i in range(1, rng):
        seq = []
        num = i
        while num != 1:
            seq.append(num)
            num = num/2 if num % 2 == 0 else num*3+1
        if(len(seq) > biggest[1]):
            biggest = (i, len(seq))
    return biggest


print(main(1000000))
