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
