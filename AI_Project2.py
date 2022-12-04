import csv
from math import sqrt
import math
import random

current_set = list(())
random.seed()
print ("hello world")
def cross_validation(data, current_set,feature_to_add): #leave-one-out cross validation
    accuracy = random.random()
    return accuracy
#testing stub

def feature_search(data):
    mylist = data[0].split()
    for i in range(1, len(mylist)):
        print('On the ' + str(i) + 'th level of the search tree')
        feature_to_add_at_this_level = list(())
        best_so_far_accuracy = 0
        for k in range(1, len(mylist)):
            if k not in current_set:
                print('considering adding the ' + str(k) + ' feature')
                temp_accuracy = cross_validation(data, current_set, k)
                if temp_accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = temp_accuracy
                    feature_to_add_at_this_level.append(k)

        current_set.insert(i, feature_to_add_at_this_level[-1])
        print('On level ' + str(i), 'i added feature ' + str(feature_to_add_at_this_level[-1]) + ' to current set')



file = open('CS170_Small_Data__6.txt')
    #reader = csv.reader(file)
data = file.readlines() #list of strings that hold all of the data
mylist = data[0].split()
feature_search(data)
print(mylist)
print(len(mylist))
print(mylist[4])
floatTest = float(mylist[4])
print(floatTest)
file.close()

def accuracy():
    file = open('CS170_Test__Data.txt')
    number_correctly_classfied = 0
    data = file.readlines()
    mylist = data[0].split()
    featureLength = len(mylist)
    dataLength = len(data)
    for i in range(0, dataLength):
        object_to_classify = -1
        mylist = data[i].split()
        label_object_to_classify = int(float(mylist[0]))

        #print('Looping over i, at the ' + str(i+1) + ' location')
        #print('The ' + str(i+1) + 'th object is in class ' + str(label_object_to_classify)) 

        nearest_neighbor_distance = float('inf')
        nearest_neighbor_location = float('inf')
        for k in range(0, dataLength):
            if k is not i:
                #print('Ask if ' + str(i+1) + ' is nearest neighbour with ' + str(k+1))
                summation = 0
                for j in range (1, featureLength):
                    object_to_classify = float(mylist[j])
                    mylist2 = data[k].split()
                    object_to_classify_for_k = float(mylist2[j])
                    summation = summation + (object_to_classify - object_to_classify_for_k)
                
                distance = math.sqrt(summation**2)

                if distance < nearest_neighbor_distance:
                        nearest_neighbor_distance = distance
                        nearest_neighbor_location = k
                        nearest_neighbor_label = int(float(mylist2[0]))
        print('Object ' + str(i+1) + ' is class '+ str(label_object_to_classify))
        print('Its nearest neighbor is ' + str(nearest_neighbor_location+1) + ' which is in class ' + str(nearest_neighbor_label))
        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classfied += 1
    file.close()
    return number_correctly_classfied / dataLength

acc = accuracy()
print(str(acc))