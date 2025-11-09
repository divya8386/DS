Algorithm: Insertion (key)

a) If tree empty → new node = root
b) Else compare key with root
c) If key < root → insert into left subtree
d) If key > root → insert into right subtree
e) Repeat recursively until inserted.

⸻

Search (key)

a) If tree empty → not found
b) If key == root → found
c) If key < root → search left
d) If key > root → search right

⸻

Deletion (key)

a) Locate node
b) If leaf → remove
c) If one child → replace with child
d) If two children → replace with inorder successor