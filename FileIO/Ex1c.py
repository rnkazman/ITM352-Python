# Read a file of names.  Print them and print the number of names in the file. 

with open("Names.txt") as my_file:
    print(my_file.read())   

with open("Names.txt") as nameFile:
    count = 0
    for x in nameFile:
        count += 1
        print(x)

    print(f"\nThere are {count} names in the file")

with open("Names.txt") as nameFile:
    line = nameFile.readline()
    numNames = 0
    while line:
        numNames += 1
        print(line)
        line = nameFile.readline()
print(f"Got {numNames} lines")