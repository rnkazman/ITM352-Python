# Compare various GCD algorithms
import math

def gcd_obvious(a, b):
    num_iterations = 0
    for divisor in range(min(a, b), 0, -1):
        num_iterations += 1
        if a % divisor == 0 and b % divisor == 0:
            return divisor, num_iterations


def gcd_by_divisors(a, b):
    num_iterations = 0

    small, large = min(a, b), max(a, b)
    best = 1
    for d in range(1, math.isqrt(small) + 1):
        num_iterations += 1

        if small % d == 0:
            for cand in (d, small // d):        # check both halves of the pair
                num_iterations += 1
                if large % cand == 0:
                    best = max(best, cand)
    return best, num_iterations


def GCD_Euclid(a, b):
    num_iterations = 0
    while b != 0:
        a, b = b, a % b
        num_iterations += 1
    return a, num_iterations


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result1 = gcd_by_divisors(num1, num2)
result2 = gcd_obvious(num1, num2)
result3 = GCD_Euclid(num1, num2)
print(f"The clever GCD of {num1} and {num2} is: {result1[0]} (with {result1[1]} iterations)")
print(f"The obvious GCD of {num1} and {num2} is: {result2[0]} (with {result2[1]} iterations)")
print(f"The Euclidean GCD of {num1} and {num2} is: {result3[0]} (with {result3[1]} iterations)")