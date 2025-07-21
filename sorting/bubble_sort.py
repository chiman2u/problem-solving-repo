"""
Bubble Sort
-----------
Time Complexity:
- Average: O(n^2)
- Worst: O(n^2)
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False # Track if any swaps were made in the current pass
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements if the order is wrong 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swap is made then array is sorted
        if not swapped:
            break

    return arr


if __name__ == "__main__":
    example = [48, 32, 95, 2, 62, 14, 90]
    print("Original list:", example)
    sorted_list = bubble_sort(example)
    print("Sorted list:", sorted_list)