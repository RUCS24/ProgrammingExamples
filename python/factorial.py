# Function to recursively find the factorial of a number
def factorial(n):
    # Base case: 0! = 1
    if n == 0:
        return 1
    # For other numbers: n! = n * (n - 1)!
    return n * factorial(n - 1)


# Print the factorial of the number the user enters
print(factorial(int(input("Enter a number to take the factorial of: "))))
