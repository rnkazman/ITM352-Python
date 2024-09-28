# Write Python code that uses the Python for-statement to create a list of 
# elements that are the odd numbers between 1 and 50.

odd_numbers = []
# 1.a
# for num in range(1,50):
#    if num % 2 != 0:
#        odd_numbers.append(num)
        
# 1.b
# for num in range(0,25):
#    odd_numbers.append(2*num + 1)
    
# 1.c
# for num in range(1,50,2):
    odd_numbers.append(num)

# 1.d
odd_numbers = [x for x in range(1, 51) if x % 2 != 0]


print(odd_numbers)