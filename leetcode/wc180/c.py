# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def popAll(self, root) -> list:
        if root == None:
            return []
        return self.popAll(root.left) + [root.val] + self.popAll(root.right)

    def createBalance(self, allValue) -> TreeNode:
        if len(allValue) == 0:
            return None
        l = len(allValue)
        r = TreeNode(allValue[l // 2])
        r.left = self.createBalance(allValue[:l // 2])
        r.right = self.createBalance(allValue[l // 2 + 1:])
        return r

    def balanceBST(self, root: TreeNode) -> TreeNode:
        allValue = self.popAll(root)
        return self.createBalance(allValue)
        

n4 = TreeNode(4)
n3 = TreeNode(3)
n2 = TreeNode(2)
n1 = TreeNode(1)
n3.right = n4
n2.right = n3
n1.right = n2
s = Solution()
b1 = s.balanceBST(n1)
print(b1.val, b1.left.val, b1.right.val, b1.left.right)