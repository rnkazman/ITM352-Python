# Given dictionary
original_dict = {1.1: '$6.25', 0.8: '$5.25', 2.5: '$10.50', 2.6: '$8.05'}

# Create a new list of dictionaries, one list entry per dictionary item
# Name the first element in each dictionary "key" and the second element "value"
list_of_dicts = []

for k, v in original_dict.items():
    new_dict = {"key": k, "value": v}
    list_of_dicts.append(new_dict)

# Print the result
print("Original dictionary:")
print(original_dict)
print("\nNew list of dictionaries:")
print(list_of_dicts)

# Alternative one-liner using list comprehension
list_of_dicts_alt = [{"key": k, "value": v} for k, v in original_dict.items()]
print("\nAlternative using list comprehension:")
print(list_of_dicts_alt)
