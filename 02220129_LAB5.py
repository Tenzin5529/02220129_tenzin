def sequential_search(arr, target):
    comparisons = 0  # Initialize comparison counter
    for index, value in enumerate(arr):
        comparisons += 1  # Increment comparison count
        if value == target:
            return index, comparisons  # Return index and comparisons if found
    return -1, comparisons  # Return -1 and comparisons if not found

# Example usage
if __name__ == "__main__":
    arr = [23, 45, 12, 67, 89, 34, 56]
    target = 67
    index, comparisons = sequential_search(arr, target)
    
    print(f"List: {arr}")
    print(f"Searching for {target} using Sequential Search")
    if index != -1:
        print(f"Found at index {index}")
    else:
        print("Not found")
    print(f"Number of comparisons: {comparisons}")