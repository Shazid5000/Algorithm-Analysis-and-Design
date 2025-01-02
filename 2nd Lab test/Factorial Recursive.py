def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = n * factorial_recursive(n - 1)
        print(f"Recursion with n={n}: {result}")
        return result

# Get user input
num = int(input("Enter a number: "))

# Calculate factorial using recursive method
print(f"Factorial of {num} (recursive): {factorial_recursive(num)}")
