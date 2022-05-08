class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
def insert(node, key):
    if node is None:
        return Node(key)

    if key <= node.key:
        node.left = insert(node.left, key)

    if key > node.key:
        node.right = insert(node.right, key)
    
    return node


def preorder(root):
    if root is not None:
        print(str(root.key), end=' ')
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key), end=' ')
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(str(root.key), end=' ')

def minValue(node):
    curr = node

    while(curr.left is not None):
        curr = curr.left
    return curr

def delete(root, key):
    if root is None:
        return root
    
    if key < root.key:
        root.left = delete(root.left, key)
    
    elif key > root.key:
        root.right = delete(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
    
        temp = minValue(root.right)

        root.key = temp.key

        root.right = delete(root.right, temp.key)

    return root

def delete2(root,key):
    if root is None:
        return root
    
    if key < root.key:
        root.left = delete(root.left, key)
        return root
    
    elif key > root.key:
        root.right = delete(root.right, key)
        return root

    if root.left is None and root.right is None:
        return None

    if root.left is None:
        temp = root.right
        root = None
        return temp
    elif root.right is None:
        temp = root.left
        root = None
        return temp
    
    succParent = root

    succ = root.right

    while succ.left is not None:
        succParent = succ
        succ = succ.left
    
    if succParent is not root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right

    root.key = succ.key

    return root



root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)
preorder(root)
print('\n')
inorder(root)
print('\n')
postorder(root)
print('\n')

delete2(root, 8)
inorder(root)