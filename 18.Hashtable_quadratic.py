# Program: Hash Table Implementation using Quadratic Probing

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.c1 = 1
        self.c2 = 3

    # Hash function using modulo division
    def hash_function(self, key):
        return key % self.size

    # Insert key using quadratic probing
    def insert(self, key):
        index = self.hash_function(key)
        i = 0

        # Quadratic probing formula: (h(k) + c1*i + c2*i^2) % size
        while self.table[(index + self.c1 * i + self.c2 * i * i) % self.size] is not None:
            i += 1
            if i >= self.size:
                print("Hash Table is full! Cannot insert:", key)
                return

        new_index = (index + self.c1 * i + self.c2 * i * i) % self.size
        self.table[new_index] = key
        print(f"Inserted key {key} at index {new_index}")

    # Display hash table
    def display(self):
        print("\nHash Table Contents:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    keys = [27, 72, 63, 42, 36, 18, 29, 101]
    hash_table = HashTable(10)

    print("Inserting keys using Quadratic Probing...\n")
    for key in keys:
        hash_table.insert(key)

    hash_table.display()
