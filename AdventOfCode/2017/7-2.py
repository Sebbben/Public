with open("7.txt") as f:
    data = f.read().splitlines()


class Node:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

    def getChildren(self): return self.children
    def getName(self): return self.name
    def getWeight(self): return self.weight
    def getTotalWeight(self):
        if self.children == None:
            return self.weight
        tot = 0
        for child in self.children:
            tot += child.getTotalWeight()

