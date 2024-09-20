# Exercise 3.7: Create a list of taxi trip durations and a tuple of fares.
# Store these in a dictionary and print it out.

tripDuration = [1.1, 0.8, 2.5, 2.6]
fares = ("$6.25", "$5.25", "$10.50", "$8.05")

tripDict = {"miles": tripDuration,
            "fares": fares}

print("tripDict:", tripDict)
print(tripDict["fares"][2],tripDict["miles"][2])

newDict = dict(zip(tripDuration, fares))
print(newDict)
print(newDict[1.1])