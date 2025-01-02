def knapsack(n, weight, profit, capacity):
    x = [0.0] * 20
    tp = 0.0
    u = capacity

    for i in range(n):
        x[i] = 0.0

    for i in range(n):
        if weight[i] > u:
            break
        else:
            x[i] = 1.0
            tp += profit[i]
            u -= weight[i]

    if i < n:
        x[i] = u / weight[i]
        tp += x[i] * profit[i]

    print("\nThe result vector is:")
    for i in range(n):
        print(f"{x[i]:.6f}\t", end="")
    print(f"\nMaximum profit is: {tp:.6f}")

def main():
    weight = [0.0] * 20
    profit = [0.0] * 20
    ratio = [0.0] * 20

    num = int(input("Enter the number of items: "))
    print("Enter the weights and profits of each item:")
    for i in range(num):
        weight[i], profit[i] = map(float, input().split())

    capacity = float(input("Enter the capacity of the knapsack: "))

    for i in range(num):
        ratio[i] = profit[i] / weight[i]

    for i in range(num):
        for j in range(i + 1, num):
            if ratio[i] < ratio[j]:
                ratio[i], ratio[j] = ratio[j], ratio[i]
                weight[i], weight[j] = weight[j], weight[i]
                profit[i], profit[j] = profit[j], profit[i]

    knapsack(num, weight, profit, capacity)

if __name__ == "__main__":
    main()
