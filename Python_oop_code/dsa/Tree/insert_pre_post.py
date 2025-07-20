class Root():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def insert(root, key):
    if root == None:
        return Root(key)
    else:
        if root.data == key:
            return
        elif key < root.data:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = Root(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 60)
inorder(root)
print()


preorder(root)
print()


postorder(root)
