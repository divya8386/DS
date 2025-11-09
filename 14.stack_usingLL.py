14# Program: Stack Implementation using Linked List

# Node class to represent each element in the stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack class using linked list
class Stack:
    def __init__(self):
        self.top = None  # Initially, the stack is empty

    # 1. Push operation - Insert element at the top
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"{data} pushed onto stack.")

    # 2. Pop operation - Remove element from the top
    def pop(self):
        if self.top is None:
            print("Stack Underflow! Stack is empty.")
            return None
        popped = self.top.data
        self.top = self.top.next
        print(f"Popped element: {popped}")
        return popped

    # 3. Display operation - Print all elements
    def display(self):
        if self.top is None:
            print("Stack is empty.")
            return
        print("Stack elements (Top → Bottom): ", end="")
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    stack = Stack()

    while True:
        print("\n=== Stack Operations Using Linked List ===")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter element to push: ")
            stack.push(data)

        elif choice == '2':
            stack.pop()

        elif choice == '3':
            stack.display()

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")
