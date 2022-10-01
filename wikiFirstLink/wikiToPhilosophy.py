import requests
from bs4 import BeautifulSoup
import json

with open("endingTree.json") as f:
    data = f.read()
    if data:
        endingsTree = json.loads(data)
    else:
        endingsTree = {}

BASE = "https://en.wikipedia.org"

# STARTLINK = "https://en.wikipedia.org/wiki/Special:Random"
STARTLINK = input(">")

soup = BeautifulSoup(requests.get(STARTLINK).content, "html.parser")



bodyContent = soup.find("div", id="bodyContent").find("div", id="mw-content-text").find("div", class_="mw-parser-output").find_all("p",recursive=False)

for p in bodyContent:
    atags = p.find_all("a",href=True)

    for a in atags:
        href = a["href"]
        if href.startswith("/wiki/"):
            STARTLINK = BASE + href
            break
    else:
        continue

    break

# STARTLINK = input("Enter link\n>")
# STARTLINK = "https://en.wikipedia.org/wiki/Iraq"

MAX_DEPTH = 30

endings = [
    "Philosophy",
    "Science",
]


blacklist = [
    "coordinate_system",
    "_language",
    "Romanization",
    "File",
    "Ancient_Greek",
    "Chinese_characters",
    "Standard_Chinese",
    "Pinyin",
    "Help",
    "_translation",
    "-logy",
    "Enzyme_Commission_number",
    "Romanize",
    "British_English"
]

nextLink = STARTLINK
visitedLinks = []

depth = 0
loops = False

while depth < MAX_DEPTH:
    depth += 1
    isEnding = False

    shortNextLink = nextLink[nextLink.index("/wiki/")+len("/wiki/"):]
    visitedLinks.append(shortNextLink)
    
    if shortNextLink in endingsTree.keys():
        isEnding = True
        break


    for ending in endings:
        if nextLink.endswith(ending):
            isEnding = True
            break


    if isEnding:
        print("Finished, with the link:" + nextLink)
        break
    elif shortNextLink in visitedLinks[:-1]:
        print("Got stuck in loop, last link checked:", nextLink)
        loops = True
        break


    page = requests.get(nextLink, allow_redirects=True)
    

    soup = BeautifulSoup(page.content, "html.parser")
    bodyContent = soup.find("div", id="bodyContent").find("div", id="mw-content-text").find("div", class_="mw-parser-output").find_all("p",recursive=False)

    for p in bodyContent:
        atags = p.find_all("a",href=True)

        for a in atags:
            href = a["href"]
            if href.startswith("/wiki/"):
                containsBlacklistedText = False
                for b in blacklist:
                    if b in href:
                        containsBlacklistedText = True
                        break
                if not containsBlacklistedText:
                    nextLink = BASE + href
                    break
        else:
            continue

        break

    print(shortNextLink)

if loops:
    print("There is no path to science for this link :-(")
    exit()

print("\n\n\n")


for i in range(len(visitedLinks)-1):
    endingsTree[visitedLinks[i]] = visitedLinks[i+1]

print("Complete path:")
nxt = STARTLINK[STARTLINK.index("/wiki/")+len("/wiki/"):]
while nxt not in endings:
    print(nxt)
    nxt = endingsTree[nxt]

print(nxt)


with open("endingTree.json","w") as f:
    f.write(json.dumps(endingsTree))