# Program: Student Record Management System using Doubly Linked List

class Node:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.prev = None
        self.next = None


class StudentRecordSystem:
    def __init__(self):
        self.head = None

    # Add a new student record
    def add_student(self, roll_no, name, marks):
        new_node = Node(roll_no, name, marks)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        print(f"Student {name} (Roll No: {roll_no}) added successfully.")

    # Delete a student record by roll number
    def delete_student(self, roll_no):
        temp = self.head
        while temp:
            if temp.roll_no == roll_no:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                print(f"Student with Roll No {roll_no} deleted successfully.")
                return
            temp = temp.next
        print(f"No student found with Roll No {roll_no}.")

    # Update student record
    def update_student(self, roll_no, new_name=None, new_marks=None):
        temp = self.head
        while temp:
            if temp.roll_no == roll_no:
                if new_name:
                    temp.name = new_name
                if new_marks is not None:
                    temp.marks = new_marks
                print(f"Student (Roll No: {roll_no}) record updated successfully.")
                return
            temp = temp.next
        print(f"No student found with Roll No {roll_no}.")

    # Search student record by roll number
    def search_student(self, roll_no):
        temp = self.head
        while temp:
            if temp.roll_no == roll_no:
                print("\nStudent Found:")
                print(f"Roll No: {temp.roll_no} | Name: {temp.name} | Marks: {temp.marks}")
                return
            temp = temp.next
        print(f"No student found with Roll No {roll_no}.")

    # Sort student records by marks or roll number
    def sort_records(self, key="marks", ascending=True):
        if self.head is None or self.head.next is None:
            print("Not enough records to sort.")
            return

        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                if ascending:
                    condition = getattr(temp, key) > getattr(temp.next, key)
                else:
                    condition = getattr(temp, key) < getattr(temp.next, key)
                if condition:
                    # Swap data instead of nodes
                    temp.roll_no, temp.next.roll_no = temp.next.roll_no, temp.roll_no
                    temp.name, temp.next.name = temp.next.name, temp.name
                    temp.marks, temp.next.marks = temp.next.marks, temp.marks
                    swapped = True
                temp = temp.next
        order = "ascending" if ascending else "descending"
        print(f"Records sorted by {key} in {order} order successfully.")

    # Display all student records
    def display_records(self):
        if self.head is None:
            print("No student records available.")
            return
        print("\nStudent Records:")
        print(f"{'Roll No':<10}{'Name':<20}{'Marks':<10}")
        print("-" * 40)
        temp = self.head
        while temp:
            print(f"{temp.roll_no:<10}{temp.name:<20}{temp.marks:<10}")
            temp = temp.next


# Main Program
if __name__ == "__main__":
    system = StudentRecordSystem()

    while True:
        print("\n--- Student Record Management System ---")
        print("1. Add Student Record")
        print("2. Delete Student Record")
        print("3. Update Student Record")
        print("4. Search Student Record")
        print("5. Sort Records")
        print("6. Display All Records")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            roll = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            system.add_student(roll, name, marks)

        elif choice == "2":
            roll = int(input("Enter Roll No to Delete: "))
            system.delete_student(roll)

        elif choice == "3":
            roll = int(input("Enter Roll No to Update: "))
            new_name = input("Enter New Name (press Enter to skip): ")
            marks_input = input("Enter New Marks (press Enter to skip): ")
            new_marks = float(marks_input) if marks_input else None
            system.update_student(roll, new_name or None, new_marks)

        elif choice == "4":
            roll = int(input("Enter Roll No to Search: "))
            system.search_student(roll)

        elif choice == "5":
            key = input("Sort by 'marks' or 'roll_no': ").strip().lower()
            order = input("Ascending or Descending? (a/d): ").strip().lower()
            system.sort_records(key=key, ascending=(order == "a"))

        elif choice == "6":
            system.display_records()

        elif choice == "7":
            print("Exiting Student Record Management System...")
            break

        else:
            print("Invalid choice. Please try again.")
