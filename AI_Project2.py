import csv
import random

current_set = list(())
random.seed()
print ("hello world")
def accuracy_function(data, current_set,feature_to_add): #leave-one-out cross validation
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
                temp_accuracy = accuracy_function(data, current_set, k)
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
#print(accuracy_function())
    #for line in reader:
        #mylist = line.split()
        #print (mylist)
    #   print (line)

file.close()