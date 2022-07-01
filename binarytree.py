from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: return
        
        tmp = root.left
        
        root.left = root.right
        root.right = tmp
        
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

        '''

        - Goes through every root in the tree and flips the left and right nodes
        - When you flip them, all the children nodes also get flipped.
        - Set temp for left, set left = right, set right to temp.

        '''

a = TreeNode(4)
a.left = TreeNode(2)
a.left.left = TreeNode(1)
a.left.right = TreeNode(3)
a.right = TreeNode(7)
a.right.left = TreeNode(6)
a.right.right = TreeNode(9)


s = Solution()

print(s.invertTree(a))
