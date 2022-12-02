import csv

#list theList = ()
print ("hello world")
file = open('CS170_Small_Data__6.txt')
    #reader = csv.reader(file)
data = file.readlines() #list of strings that hold all of the data

mylist = data[1].split()
print(mylist)
print(mylist[4])
floatTest = float(mylist[4])
print(floatTest)
    #for line in reader:
        #mylist = line.split()
        #print (mylist)
    #   print (line)