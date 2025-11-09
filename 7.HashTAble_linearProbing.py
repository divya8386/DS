# Program: Hash Table Implementation using Division Method and Linear Probing

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Initialize empty hash table
        self.DELETED = "<deleted>"  # Marker for deleted elements

    # Hash Function (Division Method)
    def hash_function(self, key):
        return key % self.size

    # Insert key using Linear Probing
    def insert(self, key):
        index = self.hash_function(key)
        original_index = index
        i = 0

        while self.table[index] is not None and self.table[index] != self.DELETED:
            if self.table[index] == key:
                print(f"Key {key} already exists at index {index}.")
                return
            i += 1
            index = (original_index + i) % self.size
            if i == self.size:
                print("Hash Table is full — cannot insert.")
                return

        self.table[index] = key
        print(f"Inserted key {key} at index {index}.")

    # Search for a key using Linear Probing
    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        i = 0

        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"Key {key} found at index {index}.")
                return index
            i += 1
            index = (original_index + i) % self.size
            if i == self.size:
                break
        print(f"Key {key} not found in the hash table.")
        return None

    # Delete a key using Linear Probing
    def delete(self, key):
        index = self.hash_function(key)
        original_index = index
        i = 0

        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = self.DELETED
                print(f"Key {key} deleted from index {index}.")
                return
            i += 1
            index = (original_index + i) % self.size
            if i == self.size:
                break
        print(f"Key {key} not found — cannot delete.")

    # Display the hash table
    def display(self):
        print("\nCurrent Hash Table:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")
        print()


# Main Program
if __name__ == "__main__":
    size = int(input("Enter the size of the hash table: "))
    hash_table = HashTable(size)

    while True:
        print("\n--- Hash Table Menu ---")
        print("1. Insert Key")
        print("2. Search Key")
        print("3. Delete Key")
        print("4. Display Table")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            key = int(input("Enter key (integer): "))
            hash_table.insert(key)

        elif choice == "2":
            key = int(input("Enter key to search: "))
            hash_table.search(key)

        elif choice == "3":
            key = int(input("Enter key to delete: "))
            hash_table.delete(key)

        elif choice == "4":
            hash_table.display()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")
