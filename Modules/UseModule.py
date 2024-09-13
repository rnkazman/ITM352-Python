# An example of using the HandyMath module.
# Also introducing formatted strings

import HandyMath as HM

first = input("Please enter your first number: ")
first = float(first)

second = input("Please enter your second number: ")
second = float(second)

average = HM.average(first,second)

print (HM.average.__name__)

print(f"The average of {first} and {second} is {average}")

print(f"The square of {first} is {HM.square(first)}")

print(f"{first} raised to the power of {second} is {HM.exponent(first,second)}")

print(f"The max of {first} and {second} is {HM.max(first, second)}")

print(f"The min of {first} and {second} is {HM.min(first, second)}")

print(f"It is {HM.isPrime(first)} that {first} is prime")
 