# Exercise 3.2: Input first, MI, and last name and output the full name
# and some variations...

first = input("Enter your first name: ")
middleInitial = input("Enter your middle initial: ")
last = input("Enter your last name: ")

fullName = first + " " + middleInitial + " " + last
fullNameJoin = " ".join((first,middleInitial,last))
print("Your full name is:", fullName)
print("Your full name is:", fullNameJoin)

print("Your full name is: %s %s %s" % (first, middleInitial, last))
print("Your full name is: {0} {1} {2}".format(first, middleInitial, last) )
