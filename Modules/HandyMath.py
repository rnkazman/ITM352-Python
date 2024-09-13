# A module with a bunch of handy math functions
import math

def average(num1, num2):
    return ((num1 + num2)/2)

def square(number):
    return (number*number)

def exponent(number, exp):
    return (number**exp)

def max(num1, num2):
    if num1 > num2:
        return(num1)
    else:
        return(num2)
    
def min(num1, num2):
   if num1 < num2:
        return(num1)
   else:
        return(num2)
   
def isPrime(number):
    # Return false if number is not an integer, or if it is 0 or 1
    if int(number) != number or number < 2:
        return(False)
    # Otherwise check up to the square root of the number
    for i in range(2, math.ceil(math.sqrt(number))):
        if(number % i) ==0:
            return(False)
    return(True)
