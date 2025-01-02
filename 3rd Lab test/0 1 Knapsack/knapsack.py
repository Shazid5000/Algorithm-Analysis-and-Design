def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

def main():
    # Read input from file
    import fileinput
 
    filename = 'example.txt'
 
    for line in fileinput.input(files=filename):
        print(line, end='')
    
    # First line is the number of items
    num_items = int(lines[0].strip())
    
    values = []
    weights = []
    
    # Next num_items lines are the values and weights of each item
    for i in range(1, num_items + 1):
        value, weight = map(int, lines[i].strip().split())
        values.append(value)
        weights.append(weight)
    
    # Last line is the capacity of the knapsack
    capacity = int(lines[num_items + 1].strip())
    
    # Solve the knapsack problem
    max_value = knapsack(values, weights, capacity)
    
    # Output the result
    print(f"\nMaximum value in the knapsack: {max_value}")

if __name__ == "__main__":
    main()
    