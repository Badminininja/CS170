import csv

#list theList = ()
print ("hello world")
file = open('CS170_Small_Data__6.txt')
    #reader = csv.reader(file)
line = file.readline()
print (type(line))
mylist = line.split()
print(mylist)
print(mylist[1])
    #for line in reader:
        #mylist = line.split()
        #print (mylist)
    #   print (line)