# Program: Binary Search Tree Implementation in Python

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a node into the BST
    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_rec(root.left, key)
        elif key > root.key:
            root.right = self._insert_rec(root.right, key)
        return root

    # Search for a node in the BST
    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_rec(root.left, key)
        return self._search_rec(root.right, key)

    # Delete a node from the BST
    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, root, key):
        if root is None:
            return root

        # Find the node to delete
        if key < root.key:
            root.left = self._delete_rec(root.left, key)
        elif key > root.key:
            root.right = self._delete_rec(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get inorder successor (smallest in the right subtree)
            min_node = self._min_value_node(root.right)
            root.key = min_node.key
            root.right = self._delete_rec(root.right, min_node.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Display methods
    def inorder(self):
        print("Inorder Traversal:", end=" ")
        self._inorder_rec(self.root)
        print()

    def _inorder_rec(self, root):
        if root:
            self._inorder_rec(root.left)
            print(root.key, end=" ")
            self._inorder_rec(root.right)

    def preorder(self):
        print("Preorder Traversal:", end=" ")
        self._preorder_rec(self.root)
        print()

    def _preorder_rec(self, root):
        if root:
            print(root.key, end=" ")
            self._preorder_rec(root.left)
            self._preorder_rec(root.right)

    def postorder(self):
        print("Postorder Traversal:", end=" ")
        self._postorder_rec(self.root)
        print()

    def _postorder_rec(self, root):
        if root:
            self._postorder_rec(root.left)
            self._postorder_rec(root.right)
            print(root.key, end=" ")


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    bst = BinarySearchTree()

    while True:
        print("\n=== Binary Search Tree Operations ===")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display (Inorder, Preorder, Postorder)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            key = int(input("Enter key to insert: "))
            bst.insert(key)
            print(f"{key} inserted successfully.")

        elif choice == '2':
            key = int(input("Enter key to delete: "))
            bst.delete(key)
            print(f"{key} deleted (if it existed).")

        elif choice == '3':
            key = int(input("Enter key to search: "))
            result = bst.search(key)
            if result:
                print(f"Key {key} found in the BST.")
            else:
                print(f"Key {key} not found.")

        elif choice == '4':
            bst.inorder()
            bst.preorder()
            bst.postorder()

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")
