# Program: Implementation of Queue using Two Stacks

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # Main stack for enqueue
        self.stack2 = []  # Temporary stack for dequeue

    # Enqueue operation (add element to queue)
    def enqueue(self, item):
        self.stack1.append(item)
        print(f"{item} enqueued to queue")

    # Dequeue operation (remove element from front)
    def dequeue(self):
        if not self.stack1 and not self.stack2:
            print("Queue is empty! Cannot dequeue.")
            return None

        # Move elements to stack2 if stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    # Peek operation (view front element)
    def peek(self):
        if not self.stack1 and not self.stack2:
            print("Queue is empty!")
            return None

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    # Check if queue is empty
    def is_empty(self):
        return not self.stack1 and not self.stack2

    # Display the current elements in queue
    def display(self):
        # To display queue elements in order
        temp = self.stack2[::-1] + self.stack1
        print("Current Queue:", temp if temp else "Empty")


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    q = QueueUsingStacks()

    while True:
        print("\n=== Queue Using Two Stacks ===")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek (Front element)")
        print("4. Display Queue")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter element to enqueue: ")
            q.enqueue(item)

        elif choice == '2':
            removed = q.dequeue()
            if removed is not None:
                print(f"Dequeued element: {removed}")

        elif choice == '3':
            front = q.peek()
            if front is not None:
                print(f"Front element: {front}")

        elif choice == '4':
            q.display()

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")
