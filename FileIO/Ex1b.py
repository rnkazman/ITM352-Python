# Add one line to a file of names.  Then print the file.

# Open the file for append and add one line.
nameFile = open("Names.txt", "a")
nameFile.write("\nPort, Dan")
nameFile.close()

# Now read and print the entire file
nameFile = open("Names.txt", "r")
print(nameFile.read())