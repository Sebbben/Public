with open("8.txt") as f:
    cont = f.read().splitlines()

tot = 0

for line in cont:
    codeLen = len(line)

    line.replace("\"", "\\\"")
    line.replace("\\","\\\\")

    line = "\"" + line + "\""

    newLen = len(line)

    input(line)

    tot += newLen-codeLen

print(tot)