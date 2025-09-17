import csv

examplefile = open('frutas.csv')
examplereader = csv.reader(examplefile)
'''exampledata = list(examplereader)
print(exampledata)

print(exampledata[0][0])
print(exampledata[0][1])
print(exampledata[0][2])
print(exampledata[1][1])
print(exampledata[6][1])'''

for row in examplereader:
    print('row #' + str(examplereader.  line_num) + '' + str(row))