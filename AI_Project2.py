import csv


print ("hello world")
with open('CS170_Small_Data__6.txt') as file:
    reader = csv.reader(file, delimiter = "\t")

    for line in reader:
        print(line[2])