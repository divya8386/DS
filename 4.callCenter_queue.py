# Program: Call Center Queue Simulation using Queue Data Structure

from collections import deque

class CallCenterQueue:
    def __init__(self):
        # Using deque for efficient queue operations (O(1) for enqueue/dequeue)
        self.queue = deque()

    def add_call(self, customer_id, call_time):
        """Add a call with customer ID and call time to the queue."""
        call = {"Customer ID": customer_id, "Call Time (min)": call_time}
        self.queue.append(call)
        print(f"Call from Customer {customer_id} added to the queue.")

    def answer_call(self):
        """Answer (remove) the first call from the queue."""
        if self.is_queue_empty():
            print("No calls to answer — the queue is empty.")
        else:
            call = self.queue.popleft()
            print(f"Answering call from Customer {call['Customer ID']} "
                  f"(Call Time: {call['Call Time (min)']} min).")

    def view_queue(self):
        """View all calls currently in the queue."""
        if self.is_queue_empty():
            print("The call queue is empty.")
        else:
            print("\nCurrent Call Queue:")
            for i, call in enumerate(self.queue, start=1):
                print(f"{i}. Customer ID: {call['Customer ID']} | "
                      f"Call Time: {call['Call Time (min)']} min")

    def is_queue_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0


# Main Program
if __name__ == "__main__":
    call_center = CallCenterQueue()

    while True:
        print("\n--- Call Center Menu ---")
        print("1. Add Call")
        print("2. Answer Call")
        print("3. View Queue")
        print("4. Check if Queue is Empty")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            customer_id = input("Enter Customer ID: ")
            call_time = int(input("Enter Call Duration (in minutes): "))
            call_center.add_call(customer_id, call_time)

        elif choice == "2":
            call_center.answer_call()

        elif choice == "3":
            call_center.view_queue()

        elif choice == "4":
            if call_center.is_queue_empty():
                print("Yes, the call queue is empty.")
            else:
                print("No, there are calls waiting in the queue.")

        elif choice == "5":
            print("Exiting Call Center System...")
            break

        else:
            print("Invalid choice. Please try again.")
