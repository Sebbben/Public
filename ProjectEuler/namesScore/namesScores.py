f = open("p022_names.txt")
text = f.read()
text = text.replace('"', "")
names = text.split(",")

names.sort()

tot = 0

for i in range(len(names)):
    wordVal = 0
    for j in names[i]:
        wordVal += ord(j)-64
    wordVal *= i+1
    tot += wordVal

print(tot)
