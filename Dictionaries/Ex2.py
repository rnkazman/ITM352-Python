# Define a list of taxi trip durations in miles
trip_durations = [1.1, 0.8, 2.5, 2.6]

# Define a tuple of fares for the same number of trips
trip_fares = ("$6.25", "$5.25", "$10.50", "$8.05")

# Store both the list and tuple as values in a dictionary called trips
trips = {
    "miles": trip_durations,
    "fares": trip_fares
}

# Print out the dictionary to show what it looks like
print(trips)

# Now print the fourth item in the dictionary. 
print(f"The 4th trip was {trips['miles'][3]} miles and cost {trips['fares'][3]}")
