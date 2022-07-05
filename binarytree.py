
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
    
    - first traverse left, 
    - second appends the root value to list
    - lastly traverse right 

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
    - second traverse left
    - lastly traverse right

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
    
    - first traverse left
    - second traverse right
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

        - first traverse left
        - second set current right Node to the root value, then set current Node to equal current's right Node.
        - lasly traverse right

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

        - first traverse left
        - then set up hashmap and add occurances to the map
        - next traverse right

        - loop through the hashmap and check for max occurances (map.values)
        - return a list of values that appear the most number of times

        '''

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.res = 0
        
        def loop(root):
            
            if not root: return
                
            if root.val >= low and root.val <= high: self.res += root.val
            
            loop(root.left)
            loop(root.right)
            
        loop(root)
        return self.res

        '''
        - check if root value fits the low and high values
        - tranverse left
        - tranverse right

        '''

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        self.res = None
        
        def loop(root):
            
            if not root: return
            
            if root.val == target.val: self.res = root
            
            loop(root.left)
            loop(root.right)
        
        loop(cloned)
        return self.res

        '''
        - check if cloned root value is equal to target value
        - tranverse left
        - tranverse right

        '''

    def checkTree(self, root: Optional[TreeNode]) -> bool:
        
        return root.left.val + root.right.val == root.val

        '''

        - check if left root plus right root is equal to parent root value

        '''


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.bal = True
        
        def loop(root):
            
            if not root:
                return -1
            
            else:
                
                l = loop(root.left)
                r = loop(root.right)

                print(l, r)
                if abs(l - r) > 1: self.bal = False
                
                return 1 + max(l, r)
        
        loop(root)
        return self.bal


        '''

        - tranverse through the tree and check if root.
        - if not a root then return -1
        - if root, continue the looping and return 1 + max(l, r)

                (1)
                /
              (2)
              /
            (3)

        - at (3), l and r should be -1 and -1
        - at (2), l should be 0 and r should be -1
        - at (1), l should be 1 and r should be -1 and abs(-1 - 1) is greater than 1


        '''



    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.same = True
        
        def loop(p, q):

            if not p and not q: return
            
            if (not p) or (not q) or p.val != q.val:
                
                self.same = False
                
                return
            
            loop(p.left, q.left)
            loop(p.right, q.right)
        
        loop(p, q)
        
        return self.same


        '''
        
        - tranverse through the trees and FIRST check if both not exist 
        - check if one exist and one doesn't
        - check if the values are equal

        '''


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        self.sym = True

        def loop(l, r):

            if not l and not r:

                return

            if (not l or not r) or l.val != r.val:

                self.sym = False

                return


            loop(l.left, r.right)
            loop(l.right, r.left)


        if root.left and root.right or not root.left and not root.right: 
            
            loop(root.left, root.right)
            return self.sym
        
        if root.left or root.right:

            return False
            


    '''

    - first check if the tree has either (both a left and right starting pair) or (none)
    and if these conditions are met loop through the loop with root.left and root.right
        Example:
            (3)       or       (3)
            / \
           (2)(5)

    - if the previous conditions are not met, return False if there is only a (root.left),
    but no (root.right), vise versa.

    - in the loop, check if (l and r both don't exist), 
    if this is the case, return and continue (still symmetric)

    
    - now check if one of the roots are missing (no left but right, or left but no right), and
    check if the root values are not equal. If either of these conditions are met, set the sym
    to FALSE and return

    '''







a = TreeNode(4)
a.left = TreeNode(2)
a.left.left = TreeNode(1)
a.left.right = TreeNode(3)
a.right = TreeNode(7)
a.right.left = TreeNode(6)
a.right.right = TreeNode(9)


p = TreeNode(1)
p.left = TreeNode(2)
p.left.left = TreeNode(3)
p.left.right = TreeNode(4)
p.right = TreeNode(2)
p.right.right = TreeNode(3)
p.right.left = TreeNode(4)

q = TreeNode(2)
q.left = TreeNode(3)


s = Solution()
#print(print2D(s.increasingBST(a)))
#print(print2D(s.invertTree(a)))
print(s.isSymmetric(q))

