from math import sqrt
import math

current_set = list(())
very_best_accuracy = 0
answerlist = list(()) #initialize place to keep the answerlist and best accuracy
def cross_validation(data, testing_set):                        #leave-one-out cross validation
    number_correctly_classfied = 0                              #keep track how many correct to get accuracy
    mylist = data[0].split()                                    #use this to get the featurelist, separates the lines of data into a list of strings
    dataLength = len(data)
    for i in range(0, dataLength):                              #this is the leave one out
        mylist = data[i].split()                                #feature list for the first object to compare to
        label_object_to_classify = int(float(mylist[0]))
        nearest_neighbor_distance, nearest_neighbor_location, nearest_neighbor_label = float('inf'), float('inf'), 100 #initial nearest neighbor information
        for k in range(0, dataLength):                          #loop to get the 2nd object to compare to
            if k is not i:                                      #make sure not to compare the same object to itself
                summation = 0
                mylist2 = data[k].split()                       #featurelist for the second object
                for j in testing_set:                           #testing set is the feature's we will, this is my way of putting 0s on the features we aren't checking
                    object_to_classify = float(mylist[j])                              #get the feature j from object 1
                    object_to_classify_for_k = float(mylist2[j])                       #get the feature j from object 2
                    summation += ((object_to_classify - object_to_classify_for_k)**2)  #get the summation 
                distance = math.sqrt(summation)                 #sqrt the summation to get the distance from object 1 and 2 based on the features in the testing set
                if distance < nearest_neighbor_distance:        #if the distance is less than current recorded nearest_neighbor data, make this the new nearest neighbor
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    mylist2 = data[nearest_neighbor_location].split()
                    nearest_neighbor_label = int(float(mylist2[0]))
        if label_object_to_classify == nearest_neighbor_label:  #if the label of object 1 is the same as the nearest neighbor then add 1 to correct classified
            number_correctly_classfied += 1
    return number_correctly_classfied / dataLength              #return the accuracy


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
fileName = input('Type in the name of the file to test: ')
#fileName = 'CS170_Small_Data__88.txt'
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
