with open("11-test.txt") as f:
    cont = [[int(x) for x in i]  for i in f.read().splitlines()]

flashes = 0

for _ in range(10):
    for i in range(len(cont)):
        for j in range(len(cont[i])):
            cont[i][j] += 1

    for i in cont:
        print(i)

    flash = True
    while flash:
        flash = False
        oldCont = []+cont
        for i in range(len(oldCont)):
            for j in range(len(oldCont[i])):
                if oldCont[i][j] == 10:
                    oldCont[i][j] += 1
                    flash = True
                    flashes += 1
                    for x in range(-1,2):
                        for y in range(-1,2):
                            if 0<=i+x<=len(cont)-1 and 0<=j+y<=len(cont[i])-1:
                                cont[i+x][j+y] += 1
    
            
    for i in range(len(cont)):
        for j in range(len(cont[i])):
            if cont[i][j] > 9:
                cont[i][j] = 0

    for i in cont:
        print(i)

    print(flashes)