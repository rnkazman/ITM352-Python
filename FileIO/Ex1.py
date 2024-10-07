# Read a file of names.  Print them and print the number of names in the file. 

nameFile = open("Names.txt")
count = 0
for x in nameFile:
    count += 1
    print(x)

print(f"\nThere are {count} names in the file")