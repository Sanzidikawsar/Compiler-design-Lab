#read from file & split, then save in another file

file1 = open('in', 'r')  #open file
read = file1.read()      #reading file
file1.close()            #file closed

file2 = open('out', 'w')

for word in read.split() and read.split('s'):
    file2.write(word)
    file2.write("\n")
