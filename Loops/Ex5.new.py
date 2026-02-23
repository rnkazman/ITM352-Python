# Define the tuples
celebrities_tuple = ("Taylor Swift", "Lionel Messi", "The Weeknd", "Keanu Reeves", "Angelina Jolie")
ages_tuple = (35, 37, 27, 60, 49)

# Initialize empty lists
celebrities_list = []
ages_list = []

# Iterate through the tuples and append values to the lists
for celebrity in celebrities_tuple:
    celebrities_list.append(celebrity)

for age in ages_tuple:
    ages_list.append(age)

# Create a dictionary to store the lists
data_dict = {
    "celebrities": celebrities_list,
    "ages": ages_list
}

# Print the dictionary
print(data_dict)