# Program: Merge Sort Implementation in Python

def merge_sort(arr):
    # Base case: if the list has only one element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    i = j = 0

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements from left or right half
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    arr = list(map(int, input("Enter elements to sort (space-separated): ").split()))
    print("Original array:", arr)
    
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)
