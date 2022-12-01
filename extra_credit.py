import random
#have a stick that has 2 cuts (these cuts need to be randomized to get a probability). we then gain 3 stick. We then check if these 3 sticks can make a triangle
random.seed()
simulationAmount = 1000000
goodTriangles=0
def tryTriangle(cutA, cutB):
    global goodTriangles
    if(cutA>cutB):
        cutA, cutB = cutB, cutA
    stick1 = cutA
    stick2 = cutB - cutA
    stick3 = 1 - cutB
    if(((stick1 + stick2) > stick3) and ((stick1 + stick3) > stick2) and ((stick2 + stick3) > stick1)):
        goodTriangles+= 1
for x in range(simulationAmount):
    tryTriangle(random.random(), random.random())
print(str(goodTriangles) + " valid triangles out of " + str(simulationAmount))
probabilty = goodTriangles/simulationAmount
print("probabilty of a successful triangle: " + str(format(probabilty, ".3f")) + " in other words about " + str(format(probabilty*100, ".1f"))+ "%")