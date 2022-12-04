import csv
from math import sqrt
import math
import random

current_set = list(())
random.seed()
print ("hello world")
very_best_accuracy = 0
best_so_far_index = 0
def cross_validation(data, current_set,feature_to_add): #leave-one-out cross validation
    number_correctly_classfied = 0
    mylist = data[0].split()
    featureLength = len(mylist)
    dataLength = len(data)
    #print(current_set)
    #print('feature to add: ' + str(feature_to_add))
    for i in range(0, dataLength):
        object_to_classify = -1
        mylist = data[i].split()
        label_object_to_classify = int(float(mylist[0]))
        #print('Looping over i, at the ' + str(i+1) + ' location')
        #print('The ' + str(i+1) + 'th object is in class ' + str(label_object_to_classify)) 
        nearest_neighbor_distance = float('inf')
        nearest_neighbor_location = float('inf')
        nearest_neighbor_label = 10
        for k in range(0, dataLength):
            if k is not i:
                #print('Ask if ' + str(i+1) + ' is nearest neighbour with ' + str(k+1))
                summation = 0
                for j in range (1, featureLength):
                    
                    object_to_classify = float(mylist[j])
                    mylist2 = data[k].split()
                    object_to_classify_for_k = float(mylist2[j])
                    #print('j: ' + str(j))
                    if j not in current_set:
                        if j is not feature_to_add:
                            object_to_classify = 0
                            object_to_classify_for_k = 0
                    
                    
                    summation = summation + ((object_to_classify - object_to_classify_for_k)**2)
                
                distance = math.sqrt(summation)
                #print('distance: ' + str(distance))
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    mylist2 = data[k].split()
                    nearest_neighbor_label = int(float(mylist2[0]))
        #print('Object ' + str(i+1) + ' is class '+ str(label_object_to_classify))
        #print('Its nearest neighbor is ' + str(nearest_neighbor_location+1) + ' which is in class ' + str(nearest_neighbor_label))
        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classfied += 1
    return number_correctly_classfied / dataLength


def feature_search(data):
    global very_best_accuracy
    global best_so_far_index
    mylist = data[0].split()
    for i in range(1, len(mylist)):
        print('On the ' + str(i) + 'th level of the search tree')
        feature_to_add_at_this_level = list(())
        best_so_far_accuracy = 0
        for k in range(1, len(mylist)):
            if k not in current_set:
                print('considering adding the ' + str(k) + ' feature')
                temp_accuracy = cross_validation(data, current_set, k)
                print('tempAccuracy: ' + str(temp_accuracy))
                if temp_accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = temp_accuracy
                    feature_to_add_at_this_level.append(k)
        #print('best so far accuracy: ' + str(best_so_far_accuracy))
        if best_so_far_accuracy > very_best_accuracy:
            very_best_accuracy = best_so_far_accuracy
            best_so_far_index = i
        current_set.insert(i, feature_to_add_at_this_level[-1])
        print('On level ' + str(i), 'i added feature ' + str(feature_to_add_at_this_level[-1]) + ' to current set. It had accuracy of ' + str(best_so_far_accuracy))



file = open('CS170_Small_Data__88.txt')
data = file.readlines() #list of strings that hold all of the data
feature_search(data)
print('The set of right features are: ')
answerlist = list(())
for p in range(best_so_far_index):
    answerlist.append(current_set[p])
print(answerlist)
print('with the best accuracy being: ' + str(very_best_accuracy))
file.close()
