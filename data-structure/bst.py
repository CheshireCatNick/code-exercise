class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def getStr(self, node):
        if node == None:
            return ''
        return self.getStr(node.left) + str(node.val) + self.getStr(node.right)
    def __str__(self):
        return self.getStr(self.root)

    def remove(self, val):
        pass
    
    def search(self, val):
        curr = self.root
        while curr != None:
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                return True
        return False

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
            return
        curr = self.root
        while True:
            if val < curr.val:
                if curr.left == None:
                    curr.left = Node(val)
                    return
                curr = curr.left
            elif val > curr.val:
                if curr.right == None:
                    curr.right = Node(val)
                curr = curr.right
            else:
                return

    def __init__(self):
        self.root = None
        pass

bst = BST()
print(bst)

bst.insert(4)
print(bst)

bst.insert(3)
print(bst)

print(bst.search(2))
print(bst.search(4))

bst.insert(2)
print(bst)

print(bst.search(2))

bst.insert(5)
print(bst)

print(bst.search(7))
bst.insert(7)
print(bst)

print(bst.search(7))
