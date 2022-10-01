with open("9.txt") as f:
    cont = [[int(i) for i in list(x)] for x in f.read().splitlines()]

totRiskLevel = 0

for y in range(0,len(cont)):
    for x in range(0,len(cont[y])):
        low = True
        for dx in [1,-1]:
            if 0<=x-dx<=len(cont[y])-1:
                if cont[y][x]>=cont[y][x-dx]:
                    low = False
                    break
        if not low:
            continue
        for dy in [1,-1]:
            if 0<=y-dy<=len(cont)-1:
                if cont[y][x]>=cont[y-dy][x]:
                    low = False
                    break
        if low:
            print(x,y,cont[y][x])
            totRiskLevel += 1+cont[y][x]

print(totRiskLevel)
                
        