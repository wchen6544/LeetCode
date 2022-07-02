
from typing import Optional, List

COUNT = [10]

def print2DUtil(root, space) :
 
    if (root == None): return 
    
    space += COUNT[0]
 
    print2DUtil(root.right, space)

    
    print()
    
    for i in range(COUNT[0], space):
        print(end = " ")
    
    print(root.val)
    print2DUtil(root.left, space)
 

def print2D(root) :
    print2DUtil(root, 0)
    return



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            
        self.res = []    
        
        def loop(root):
            
            if not root: return
            
            loop(root.left)
            
            self.res.append(root.val)

            loop(root.right)
        
        loop(root)
        return self.res

    '''
    
    - first transverse left, 
    - second appends the root value to list
    - lastly transverse right 

    '''


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        self.res = []
        
        def loop(root):
            
            if not root: return
            
            self.res.append(root.val)
            loop(root.left)
            loop(root.right)
        
        loop(root)
        return self.res

    '''

    - first appends the root value to the list
    - second transverse left
    - lastly transverse right

    '''


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        self.res = []
        
        def loop(root):
            
            if not root: return
            
            loop(root.left)
            loop(root.right)
            self.res.append(root.val)
        
        loop(root)
        return self.res


    '''
    
    - first transverse left
    - second transverse right
    - lastly append the root value to the list


    '''


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


    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        self.newT = TreeNode()
        self.cur = self.newT
        
        
        def loop(root):
            
            if not root: return
        
            
            loop(root.left)
            
            self.cur.right = TreeNode(root.val)
            self.cur = self.cur.right
        
        
            loop(root.right)

        loop(root)
        
        return self.newT.right


        '''

        - first transverse left
        - second set current right Node to the root value, then set current Node to equal current's right Node.
        - lasly transverse right

        '''

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        self.res = []
        self.m = {}
        self.max = 0
        
        def loop(root):
            
            if not root: return
            
            loop(root.left)

            
            if root.val not in self.m: 
                self.m[root.val] = 0
            
            if root.val in self.m: 
                self.m[root.val] += 1
            
            
            loop(root.right)
        
        
        loop(root)

        for i in self.m:
            
            if self.m[i] == self.max:
                
                self.res.append(i)
                
                
            if self.m[i] > self.max:
                
                self.res.clear()
                self.res.append(i)
                self.max = self.m[i]
            

        
        return self.res


        '''

        - first transverse left
        - then set up hashmap and add occurances to the map
        - next transverse right

        - loop through the hashmap and check for max occurances (map.values)
        - return a list of values that appear the most number of times

        '''


a = TreeNode(4)
a.left = TreeNode(2)
a.left.left = TreeNode(1)
a.left.right = TreeNode(3)
a.right = TreeNode(7)
a.right.left = TreeNode(6)
a.right.right = TreeNode(9)

b = TreeNode(5)
b.left = TreeNode(3)
b.right = TreeNode(6)
b.left.left = TreeNode(2)
b.left.right = TreeNode(4)
b.left.left.left = TreeNode(1)
b.right.right = TreeNode(8)
b.right.right.left = TreeNode(7)
b.right.right.right = TreeNode(9)


s = Solution()
print(print2D(s.increasingBST(a)))
print(print2D(s.invertTree(a)))


