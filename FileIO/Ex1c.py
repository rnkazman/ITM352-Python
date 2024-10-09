# Read a file of names.  Print them and print the number of names in the file. 

with open("Names.txt") as my_file:
    the_file = my_file.read() 
    print(the_file) 

print("Got the file\n")  
splitup = the_file.split("\n")
print(splitup)
print("Length=", len(splitup))

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