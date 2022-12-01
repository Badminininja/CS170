import random
random.seed()
numberOfNodes, totalsimulationAmount, totalgoodTriangles = 1000,0,0
nodelist = list(())
class node:
    def __init__(self, cutA):
        self.cut, self.childlist, self.validTriangles = cutA, list(()), 0
def tryTriangle(cutA, cutB):
    global goodTriangles
    if(cutA>cutB):
        cutA, cutB = cutB, cutA
    stick1, stick2, stick3 = cutA, cutB - cutA, 1 - cutB
    return 1 if(((stick1 + stick2) > stick3) and ((stick1 + stick3) > stick2) and ((stick2 + stick3) > stick1)) else 0
for i in range(numberOfNodes):
    nodelist.append(node(random.random()))
for x in range(numberOfNodes):
    for j in range(numberOfNodes):
        nodelist[x].childlist.append(node(random.random()))
        nodelist[x].validTriangles += tryTriangle(nodelist[x].cut, nodelist[x].childlist[j].cut)
for a in range(numberOfNodes):
    totalsimulationAmount+=numberOfNodes
    totalgoodTriangles+=nodelist[a].validTriangles
print(str(totalgoodTriangles) + " valid triangles out of " + str(totalsimulationAmount))
probabilty = totalgoodTriangles/totalsimulationAmount
print("probabilty of a successful triangle: " + str(format(probabilty, ".3f")) + " in other words about " + str(format(probabilty*100, ".1f"))+ "%")