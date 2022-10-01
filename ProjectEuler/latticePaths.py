def main(size):
    size += 1
    ronald = []
    for i in range(size):
        ronald.append([n for n in range(size)])
    for i in range(len(ronald[0])):
        ronald[0][i] = 1
    for i in ronald:
        i[0] = 1
    for i in range(1, len(ronald)):
        for j in range(1, len(ronald[i])):
            ronald[i][j] = ronald[i-1][j]+ronald[i][j-1]

    return ronald[-1][-1]


print(main(21))
