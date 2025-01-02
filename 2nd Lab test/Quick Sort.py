def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        sorted_partition = quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
        print(f"Sorted partition: {sorted_partition}")
        return sorted_partition

# Get user input for the array
input_str = input("Enter space-separated integers for the array: ")
arr = list(map(int, input_str.split()))

# Display the unsorted array
print("Unsorted array:", arr)

# Apply Quick Sort and display each step
sorted_arr = quick_sort(arr)

# Display the sorted array
print("Sorted array:", sorted_arr)
