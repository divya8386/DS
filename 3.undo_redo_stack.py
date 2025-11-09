# Program: Undo/Redo System using Stack Data Structure

# We’ll use two stacks:
# 1. undo_stack – stores document states for undo operations
# 2. redo_stack – stores undone states for redo operations

class TextEditor:
    def __init__(self):
        self.document = ""         # Current state of the document
        self.undo_stack = []       # Stack for undo operations
        self.redo_stack = []       # Stack for redo operations

    def make_change(self, new_text):
        """Make a new change and push current state to undo stack."""
        self.undo_stack.append(self.document)
        self.document = new_text
        self.redo_stack.clear()  # Clear redo history when new change is made
        print("Change made successfully.")

    def undo(self):
        """Undo the last change."""
        if not self.undo_stack:
            print("No actions to undo.")
            return
        # Move current state to redo stack
        self.redo_stack.append(self.document)
        # Restore last state from undo stack
        self.document = self.undo_stack.pop()
        print("Undo successful.")

    def redo(self):
        """Redo the last undone change."""
        if not self.redo_stack:
            print("No actions to redo.")
            return
        # Move current state to undo stack
        self.undo_stack.append(self.document)
        # Restore last undone change
        self.document = self.redo_stack.pop()
        print("Redo successful.")

    def display(self):
        """Display current state of the document."""
        print(f"Current Document State: \"{self.document}\"")


# Main Program
if __name__ == "__main__":
    editor = TextEditor()

    while True:
        print("\n--- Text Editor Menu ---")
        print("1. Make a Change")
        print("2. Undo Last Change")
        print("3. Redo Last Change")
        print("4. Display Document")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            new_text = input("Enter new document text: ")
            editor.make_change(new_text)
        elif choice == "2":
            editor.undo()
        elif choice == "3":
            editor.redo()
        elif choice == "4":
            editor.display()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")
