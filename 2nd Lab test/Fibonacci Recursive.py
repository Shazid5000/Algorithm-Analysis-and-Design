def fibonacci_recursive(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibonacci_recursive(n - 1, computed) + fibonacci_recursive(n - 2, computed)
    return computed[n]

def print_fibonacci_recursive(num_terms):
    for i in range(num_terms):
        print(f"Term {i + 1}: {fibonacci_recursive(i)}")

# Get user input
num_terms = int(input("Enter the number of terms: "))

# Generate and display Fibonacci sequence using recursive method
print_fibonacci_recursive(num_terms)
