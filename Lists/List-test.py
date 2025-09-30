# Start with an empty shopping list
shopping_list = []
# Add a few items using append()
shopping_list.append('apples')
shopping_list.append('milk')
shopping_list.append('bread')
# Add another item to the beginning using insert()
shopping_list.insert(0, 'eggs')
# Remove the last item using pop()
shopping_list.pop()
# Check if 'milk' is in the list
if 'milk' in shopping_list:
	print("Milk is in the shopping list.")
else:
	print("Milk is not in the shopping list.")

# Sort the list alphabetically
shopping_list.sort()

# Reverse the order of the sorted list
shopping_list.reverse()

# Print the final list
print("Final shopping list:", shopping_list)
