# Program: Sorting Employee Salaries using Selection Sort and Bubble Sort

# Selection Sort Function
def selection_sort(salaries):
    n = len(salaries)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if salaries[j] < salaries[min_index]:
                min_index = j
        # Swap the found minimum with the first element
        salaries[i], salaries[min_index] = salaries[min_index], salaries[i]
    return salaries


# Bubble Sort Function
def bubble_sort(salaries):
    n = len(salaries)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if salaries[j] > salaries[j + 1]:
                # Swap if elements are in wrong order
                salaries[j], salaries[j + 1] = salaries[j + 1], salaries[j]
    return salaries


# Function to display top 5 highest salaries
def display_top_five(sorted_salaries):
    top_five = sorted_salaries[-5:]  # Last 5 elements (highest salaries)
    top_five.reverse()  # Reverse to show from highest to lowest
    print("Top Five Highest Salaries:")
    for salary in top_five:
        print(f"₹{salary:.2f}")


# Main Program
if __name__ == "__main__":
    # Example list of employee salaries
    salaries = [45000.50, 78000.75, 56000.00, 92000.25, 61000.10,
                48000.40, 100000.00, 89000.90, 72000.30, 53000.80]

    print("Original Salaries List:")
    print(salaries)

    # Selection Sort
    selection_sorted = selection_sort(salaries.copy())
    print("\nSalaries after Selection Sort (Ascending):")
    print(selection_sorted)
    display_top_five(selection_sorted)

    # Bubble Sort
    bubble_sorted = bubble_sort(salaries.copy())
    print("\nSalaries after Bubble Sort (Ascending):")
    print(bubble_sorted)
    display_top_five(bubble_sorted)
