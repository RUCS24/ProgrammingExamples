# Recursively finds the nth fibonacci number
def fib(n):
    # Base cases: 0th fibonacci number is 0, and 1st fibonacci number is 1
    if n == 0 or n == 1:
        return n
    # For other numbers, the nth fibonacci number is the sum of the 2 previous fibonacci numbers
    return fib(n - 1) + fib(n - 2)


# Output the fibonacci number at the position given by the user
print(fib(int(input("Enter the index of the fibonacci number to calculate: "))))
