from math import sqrt
import math
import random

current_set = list(())
random.seed()
very_best_accuracy = 0
answerlist = list(())
def cross_validation(data, testing_set): #leave-one-out cross validation
    number_correctly_classfied = 0
    mylist = data[0].split()
    featureLength = len(mylist)
    dataLength = len(data)
    #featureSet = current_set.copy()
    #featureSet.append(feature_to_add)
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
        nearest_neighbor_label = 100
        for k in range(0, dataLength):

            if k is not i:
                #print('Ask if ' + str(i+1) + ' is nearest neighbour with ' + str(k+1))
                summation = 0
                mylist2 = data[k].split()
                for j in testing_set:
                    #object_to_classify = float(mylist[j])
                    #object_to_classify_for_k = float(mylist2[j])
                    #print('j: ' + str(j))
                    #lets say curr set is [2,4,5] and feature to add is 6 this would go thru if j = to 1,3,6,7...
                    object_to_classify = float(mylist[j])
                    object_to_classify_for_k = float(mylist2[j])      
                    summation += ((object_to_classify - object_to_classify_for_k)**2)
                
                distance = math.sqrt(summation)
                #print('distance: ' + str(distance) + " vs nearest neighbor distance: " + str(nearest_neighbor_distance))
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    mylist2 = data[nearest_neighbor_location].split()
                    nearest_neighbor_label = int(float(mylist2[0]))
        #print('Object ' + str(i+1) + ' is class '+ str(label_object_to_classify))
        #print('Its nearest neighbor is ' + str(nearest_neighbor_location+1) + ' which is in class ' + str(nearest_neighbor_label))
        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classfied += 1
    #print(str(number_correctly_classfied) + ' / ' + str(dataLength))
    return number_correctly_classfied / dataLength


def feature_search_forward(data): # forward selection
    global very_best_accuracy
    global answerlist
    mylist = data[0].split()
    print('Beginning search.')
    for i in range(1, len(mylist)):
        feature_to_add_at_this_level = list(())
        best_so_far_accuracy = 0
        for k in range(1, len(mylist)):
            if k not in current_set:
                testingSet = current_set.copy()
                testingSet.append(k)
                print('    Using features(s)', end=' ')
                print(testingSet, end= ' ')
                temp_accuracy = cross_validation(data, testingSet)
                print('accuracy is  ' + str("{:.1f}".format(temp_accuracy*100)) + '%')
                if temp_accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = temp_accuracy
                    feature_to_add_at_this_level.append(k)
        current_set.insert(i, feature_to_add_at_this_level[-1])
        if best_so_far_accuracy > very_best_accuracy:
            very_best_accuracy = best_so_far_accuracy
            answerlist = current_set.copy()
        print('Feature set', end=' ')
        print(current_set, end=' ')
        print('was best, accuracy is ' + str("{:.1f}".format(best_so_far_accuracy*100)) + '%')

def feature_search_backwards(data, initial_set): #backwards elimination 
    global very_best_accuracy
    global answerlist
    mylist = data[0].split()
    placeHolderSet = list(())
    current_set = initial_set
    print('Beginning search.')
    for i in range(1, len(mylist)):
        feature_to_add_at_this_level = list(())
        best_so_far_accuracy = 0
        for k in range(1, len(mylist)):
            if k not in placeHolderSet:
                testingSet = current_set.copy()
                testingSet.remove(k)
                print('    Using features(s)', end=' ')
                print(testingSet, end= ' ')
                temp_accuracy = cross_validation(data, testingSet)
                print('accuracy is  ' + str("{:.1f}".format(temp_accuracy*100)) + '%')
                if temp_accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = temp_accuracy
                    feature_to_add_at_this_level.append(k)
        placeHolderSet.insert(i, feature_to_add_at_this_level[-1])
        current_set.remove(feature_to_add_at_this_level[-1])
        if best_so_far_accuracy > very_best_accuracy:
            very_best_accuracy = best_so_far_accuracy
            answerlist = current_set.copy()
        print('Feature set', end=' ')
        print(current_set, end=' ')
        print('was best, accuracy is ' + str("{:.1f}".format(best_so_far_accuracy*100)) + '%')

print('Welcome to Joseph\'s Feature Selection Algorithm')
#fileName = input('Type in the name of the file to test: ')
fileName = 'CS170_Small_Data__88.txt'
file = open(fileName)
data = file.readlines() #list of strings that hold all of the data
print("Type the number of the algorithm you want to run.")
print('    1) Forward Selection')
print('    2) Backward Elimination')
search_Algo = input()
if(search_Algo == '1'):
    featurelist = data[0].split()
    print('This dataset has ' + str(len(featurelist)-1) + ' features (not including the class attribute), with ' + str(len(data)) + ' instances.')
    print('Running nearest neighbor with all ' + str(len(featurelist)-1) + ' features, using "leaving-one-out" evaluation, I get an accuracy of:', end=' ')
    initial_set = list(())
    for a in range(1, len(featurelist)):
        initial_set.append(a)
    print(str("{:.1f}".format(cross_validation(data, initial_set)*100)) + '%')
    feature_search_forward(data)
elif(search_Algo == '2'):
    featurelist = data[0].split()
    print('This dataset has ' + str(len(featurelist)-1) + ' features (not including the class attribute), with ' + str(len(data)) + ' instances.')
    print('Running nearest neighbor with all ' + str(len(featurelist)-1) + ' features, using "leaving-one-out" evaluation, I get an accuracy of:', end=' ')
    initial_set = list(())
    for a in range(1, len(featurelist)):
        initial_set.append(a)
    print(str("{:.1f}".format(cross_validation(data, initial_set)*100)) + '%')
    feature_search_backwards(data, initial_set)
print()
print('Finished search!! The best feature subset is', end=' ')
print(answerlist, end=', ')
print('which has an accuracy of ' + str("{:.1f}".format(very_best_accuracy*100)) + '%')
file.close()
