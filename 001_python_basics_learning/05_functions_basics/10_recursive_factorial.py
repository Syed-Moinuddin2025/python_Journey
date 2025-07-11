# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Change this number to test different inputs
n = 6
result = factorial(n)

# Print using f-string
print(f"Factorial of {n} is: {result}")
