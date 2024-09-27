# Iterate through the list sample_fares = [8.60, 5.75, 13.25, 21.21] and print a 
# message “This fare is high!” if the fare is greater than 12 dollars and “This 
# fare is low” otherwise.

sample_fares = [8.60, 5.75, 13.25, 21.21]

for x in sample_fares:
    if x > 12:
        print(f"This fare {x} is high!")
    else: 
        print(f"This fare {x} is low")
