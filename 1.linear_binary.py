# Program: Linear and Binary Search for Customer Account IDs

# Linear Search Function
def linear_search(account_list, target_id):
    for i in range(len(account_list)):
        if account_list[i] == target_id:
            return i  # Return index if found
    return -1  # Return -1 if not found

# Binary Search Function (list must be sorted)
def binary_search(account_list, target_id):
    low = 0
    high = len(account_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if account_list[mid] == target_id:
            return mid  # Found
        elif account_list[mid] < target_id:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Not found

# Main Program
if __name__ == "__main__":
    # Example list of customer account IDs
    customer_ids = [105, 204, 350, 410, 512, 630, 745, 890]

    print("Customer Account IDs:", customer_ids)

    # Input target ID from user
    target = int(input("Enter Customer Account ID to search: "))

    # Perform Linear Search
    linear_result = linear_search(customer_ids, target)
    if linear_result != -1:
        print(f"Linear Search: Account ID {target} found at position {linear_result}")
    else:
        print(f"Linear Search: Account ID {target} not found")

    # Perform Binary Search
    # Note: Binary search works only on sorted lists
    binary_result = binary_search(customer_ids, target)
    if binary_result != -1:
        print(f"Binary Search: Account ID {target} found at position {binary_result}")
    else:
        print(f"Binary Search: Account ID {target} not found")
