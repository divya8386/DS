# Program: Queue Implementation using Linked List

# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Queue class using Linked List
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue - Add element to the rear
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:  # If queue is empty
            self.front = self.rear = new_node
            print(f"{data} enqueued to queue.")
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"{data} enqueued to queue.")

    # Dequeue - Remove element from the front
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow! Queue is empty.")
            return None
        removed = self.front.data
        self.front = self.front.next

        # If front becomes None, also reset rear
        if self.front is None:
            self.rear = None
        print(f"Dequeued element: {removed}")
        return removed

    # Display - Show all elements
    def display(self):
        if self.front is None:
            print("Queue is empty.")
            return
        print("Queue elements (Front → Rear): ", end="")
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    q = Queue()

    while True:
        print("\n=== Queue Operations Using Linked List ===")
        print("1. Enqueue (Add element)")
        print("2. Dequeue (Remove element)")
        print("3. Display Queue")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter element to enqueue: ")
            q.enqueue(data)

        elif choice == '2':
            q.dequeue()

        elif choice == '3':
            q.display()

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")
