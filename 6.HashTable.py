# Program: Hash Table Implementation using Division Method and Chaining

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Each index stores a list for chaining

    # Hash Function (Division Method)
    def hash_function(self, key):
        return key % self.size

    # Insert a key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if key already exists and update it
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated key {key} with new value '{value}'.")
                return
        # If key not found, append new pair
        self.table[index].append([key, value])
        print(f"Inserted key {key} with value '{value}' at index {index}.")

    # Search for a key
    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                print(f"Key {key} found at index {index} with value '{pair[1]}'.")
                return pair[1]
        print(f"Key {key} not found in the hash table.")
        return None

    # Delete a key-value pair
    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                print(f"Key {key} deleted successfully from index {index}.")
                return
        print(f"Key {key} not found — cannot delete.")

    # Display the hash table
    def display(self):
        print("\nHash Table State:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")


# Main Program
if __name__ == "__main__":
    hash_table = HashTable()

    while True:
        print("\n--- Hash Table Menu ---")
        print("1. Insert Key-Value Pair")
        print("2. Search by Key")
        print("3. Delete by Key")
        print("4. Display Hash Table")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            key = int(input("Enter Key (integer): "))
            value = input("Enter Value: ")
            hash_table.insert(key, value)

        elif choice == "2":
            key = int(input("Enter Key to Search: "))
            hash_table.search(key)

        elif choice == "3":
            key = int(input("Enter Key to Delete: "))
            hash_table.delete(key)

        elif choice == "4":
            hash_table.display()

        elif choice == "5":
            print("Exiting Hash Table Program...")
            break

        else:
            print("Invalid choice. Please try again.")
