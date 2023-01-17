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

def feature_search_forward(data, featurelist):                  # forward selection
    global very_best_accuracy                                   #initilize global variables
    global answerlist
    print('Beginning search.')
    for i in range(1, len(featurelist)):                        #feature list only there for its length which is the features
        feature_to_add_at_this_level = list(())                 #initilize feature to add list to know the best feature to add/remove
        best_so_far_accuracy = 0                                #initilize best accuracy
        for k in range(1, len(featurelist)):                    #how we want to test what additional features to try
            if k not in current_set:                            #do not repeat features
                testingSet = current_set.copy()                 #copy the current set to a new set we can alter for testing
                testingSet.append(k)                            #add the feature we want to add to the testing set
                print('    Using features(s)', end=' ')
                print(testingSet, end= ' ')
                temp_accuracy = cross_validation(data, testingSet) #test the testing set with cross validation
                print('accuracy is  ' + str("{:.1f}".format(temp_accuracy*100)) + '%') # print the accuracy of using that set
                if temp_accuracy > best_so_far_accuracy:        #if the accuracy of this set is the best
                    best_so_far_accuracy = temp_accuracy        #update the best accuracy
                    feature_to_add_at_this_level.append(k)      #add it to be the latest feature to add
        current_set.insert(i, feature_to_add_at_this_level[-1]) #after all the testing, add/remove the feature that resulted in the best accuracy
        if best_so_far_accuracy > very_best_accuracy:           #if best accuracy in this set is the best overall
            very_best_accuracy = best_so_far_accuracy           #update respective global accuracy
            answerlist = current_set.copy()                     #update respective global set
        print('Feature set', end=' ')
        print(current_set, end=' ')
        print('was best, accuracy is ' + str("{:.1f}".format(best_so_far_accuracy*100)) + '%')

def feature_search_backwards(data, initial_set, featurelist):   #backwards elimination 
    global very_best_accuracy                                   #essentially the same thing as forward, but we remove instead of add
    global answerlist
    placeHolderSet = list(())                                   #have a placeholder list to track which features we've removed
    current_set = initial_set                                   #start with a full list of features
    print('Beginning search.')
    for i in range(1, len(featurelist)):
        feature_to_remove_at_this_level = list(())
        best_so_far_accuracy = 0
        for k in range(1, len(featurelist)):
            if k not in placeHolderSet:                         #check if we've removed this feature before already
                testingSet = current_set.copy()
                testingSet.remove(k)                            #remove the said feature from the testing set
                print('    Using features(s)', end=' ')
                print(testingSet, end= ' ')
                temp_accuracy = cross_validation(data, testingSet)
                print('accuracy is  ' + str("{:.1f}".format(temp_accuracy*100)) + '%')
                if temp_accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = temp_accuracy
                    feature_to_remove_at_this_level.append(k)
        placeHolderSet.insert(i, feature_to_remove_at_this_level[-1])  #insert the feature we removed that led to the best accuracy
        current_set.remove(feature_to_remove_at_this_level[-1])        #remove the feature that led to the best accuracy from the current set 
        if best_so_far_accuracy > very_best_accuracy:
            very_best_accuracy = best_so_far_accuracy
            answerlist = current_set.copy()
        print('Feature set', end=' ')
        print(current_set, end=' ')
        print('was best, accuracy is ' + str("{:.1f}".format(best_so_far_accuracy*100)) + '%') hjk
        hj

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
    print(str("{:.1f}".format(cross_validation(data, initial_set)*100)) + '%') #use all of features and get its accuracy
    feature_search_forward(data, featurelist)
elif(search_Algo == '2'):
    featurelist = data[0].split()
    print('This dataset has ' + str(len(featurelist)-1) + ' features (not including the class attribute), with ' + str(len(data)) + ' instances.')
    print('Running nearest neighbor with all ' + str(len(featurelist)-1) + ' features, using "leaving-one-out" evaluation, I get an accuracy of:', end=' ')
    initial_set = list(())
    for a in range(1, len(featurelist)):    #create an initial set since we start with a full set and then remove one at a time
        initial_set.append(a)
    print(str("{:.1f}".format(cross_validation(data, initial_set)*100)) + '%')
    feature_search_backwards(data, initial_set, featurelist)
print()
print('Finished search!! The best feature subset is', end=' ')
print(answerlist, end=', ')
print('which has an accuracy of ' + str("{:.1f}".format(very_best_accuracy*100)) + '%')
file.close()
