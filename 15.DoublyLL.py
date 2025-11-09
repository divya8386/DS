# Program: Doubly Linked List for Employee Records

# Node class
class Node:
    def __init__(self, name, post):
        self.name = name
        self.post = post
        self.prev = None
        self.next = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # A. Insert node at start
    def insert_at_start(self, name, post):
        new_node = Node(name, post)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print(f"Employee {name} ({post}) inserted at start.")

    # B. Insert node at end
    def insert_at_end(self, name, post):
        new_node = Node(name, post)
        if self.head is None:
            self.head = new_node
            print(f"Employee {name} ({post}) inserted as the first node.")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        print(f"Employee {name} ({post}) inserted at end.")

    # C. Traverse forward
    def display_forward(self):
        if self.head is None:
            print("List is empty.")
            return
        print("\nEmployees (Forward Traversal):")
        temp = self.head
        while temp:
            print(f"Name: {temp.name}, Post: {temp.post}")
            temp = temp.next

    # D. Traverse backward
    def display_backward(self):
        if self.head is None:
            print("List is empty.")
            return
        print("\nEmployees (Backward Traversal):")
        temp = self.head
        while temp.next:  # Move to the last node
            temp = temp.next
        while temp:
            print(f"Name: {temp.name}, Post: {temp.post}")
            temp = temp.prev


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    dll = DoublyLinkedList()

    while True:
        print("\n=== Employee Record Management (Doubly Linked List) ===")
        print("A. Insert Employee at Start")
        print("B. Insert Employee at End")
        print("C. Display Employees (Forward)")
        print("D. Display Employees (Backward)")
        print("E. Exit")

        choice = input("Enter your choice (A/B/C/D/E): ").upper()

        if choice == 'A':
            name = input("Enter Employee Name: ")
            post = input("Enter Employee Post: ")
            dll.insert_at_start(name, post)

        elif choice == 'B':
            name = input("Enter Employee Name: ")
            post = input("Enter Employee Post: ")
            dll.insert_at_end(name, post)

        elif choice == 'C':
            dll.display_forward()

        elif choice == 'D':
            dll.display_backward()

        elif choice == 'E':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")
