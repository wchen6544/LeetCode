
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


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        self.height = 0
            
        def loop(root):
            
            if not root:
                
                return 0
            
            else:
                
                l = loop(root.left)
                r = loop(root.right)

                self.height = 1 + max(l, r)

                return 1 + max(l, r)
        
            
        
        
        loop(root)
        return self.height


    '''
    
    - if root doesn't exist, return 0
    - loop through the left and right side of tree and set height to 1 + max(l, r)
    - return 1 + max(l, r)
    - Make sure you have a if else seperating the looping part and if root doesn't exist

    '''
            
            

    def minDepth(self, root: Optional[TreeNode]) -> int:


        if not root: return 0

        self.res = float('inf')

        def loop(root, num):

            if not root:
                return

            if not root.left and not root.right:


                self.res = min(self.res, num)




            loop(root.left, num + 1)
            loop(root.right, num + 1)

        loop(root, 1)
        return self.res


    '''

    - if not initial root, return 0
    - needs 2 var in loop, one for the root and one to keep track of how many nodes were looped through
    - set result to infinity
    - if found leaf (no right or left root), set result to the min of itself and num
    - when looping through, loop with the root.left/root.right and num + 1

    '''



    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        self.res = False
        
        def loop(root, total):
            
            if not root:
                return
            
            total += root.val
            
            if total == targetSum and not root.right and not root.left:
                
                self.res = True
                return
            
            
            loop(root.left, total)
            loop(root.right, total)
        
        loop(root, 0)
        return self.res



    '''
    
    - tranverse through the tree and when you loop have the root and a total var
    - check if total is equal to the target and if its a leaf (no root right and no root left)

    '''



    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        
        def loop(root, direction):
            
            if not root:
                return
            
            if not root.left and not root.right and direction:
                
                self.res += root.val
            
            
            loop(root.left, True)
            loop(root.right, False)
        
        loop(root, False)
        return self.res


    '''
    
    - tranverse through the tree and when you loop have the root and a direction var
    - set direction to True if left, False if right
    - only add if its a leaf (no root right and no root left) and direction is True

    '''


    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.l = []
        self.res = float('inf')
        
        def loop(root):
            
            if not root:
                return
            
            loop(root.left)
            
            self.l.append(root.val)
            
            loop(root.right)
        
        loop(root)
        
        for i in range(len(self.l) - 1):
            
            if self.l[i + 1] - self.l[i] < self.res:
                
                self.res = self.l[i + 1] - self.l[i]
        
        return self.res


    '''
    
    - tranverse through the tree (inorder) and append all values to a list
    - this list will be scrictly ascending order
    - after all the tranversing, go through the list and subtract the pairs 
    (index1 - index0, index2 - index1, etc) and find the min

    '''


    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        self.res = None
        
        def loop(root):
            
            if not root:
                return
            
            if root.val == val:
                
                self.res = root
                return
            
            if root.val > val:
                loop(root.left)
            else:
                loop(root.right)
        
        loop(root)
        return self.res


    '''
    
    - tranverse through the tree and check if root value is equal to (val)
    - if its too big, loop left
    - if its too small, loop right

    '''


    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def loop(s, e):
            
            if s > e: return
            
            m = (s + e) // 2
            
            node = TreeNode(nums[m])
            node.left = loop(s, m - 1)
            node.right = loop(m + 1, e)
            
            return node
        
        return loop(0, len(nums) - 1)
            

    '''

    - loop through the tree with a start and end var (index)
    - set the node to equal the middle of the start and end and
    set the node.left to re-loop and set the start and end to the
    start, and middle minus one. For node.right, do the same but change
    the start to middle plus one and end to end.
    - return node after all of the looping.

    '''

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        self.res = []
        
        def loop(root, arr):
            
            if not root: return
            
            arr.append(str(root.val))
            
            if not root.left and not root.right:
                
                self.res.append("->".join(arr))
                return
            
            loop(root.left, arr.copy())

            loop(root.right, arr.copy())
        
        loop(root, [])
        return self.res


    '''
    
    - tranverse through the tree and append to an array the root val if exist
    - if the node is a leaf, append the completed list to the result


    '''


    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def loop(r1, r2):
            
            if not r1:
                return r2
            if not r2:
                return r1
            
            r1.val += r2.val
            r1.left = loop(r1.left, r2.left)
            r1.right = loop(r1.right, r2.right)
            
            return r1
        
        return loop(root1, root2)


    '''
    
    - if first tree node doesn't exist, return second tree node
    - if second tree node doesn't exist, return first tree node
    - if both exist, add root2 node to root1 node
    - root1 left is equal to loop left
    - root1 right is equal to loop right

    '''


    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        
        def loop(root, arr):
            
            if not root:
                return
            
            arr.append(str(root.val))
            
            if not root.left and not root.right:
                
                self.res += int("".join(arr))
                
                
                
            loop(root.left, arr.copy())
            loop(root.right, arr.copy())
        
        loop(root, [])
        return self.res


    '''

    - loop through the tree and everytime you loop, make a copy of the arr
    - append the string version of the number then if leaf, join and turn to int

    '''



    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.res = []
        
        def loop(root, lvl):
            
            if not root:
                return
            
            
            if len(self.res) - 1 < lvl:
                self.res.append([root.val])
            else:
                self.res[lvl].append(root.val)                
            
            
            loop(root.left, lvl + 1)
            loop(root.right, lvl + 1)
            
        
        loop(root, 0)
        return self.res
            


    '''
    
    - preorder tranversal (root, left, right)
    - loop with the root and the lvl
    - everytime you loop, lvl + 1 which tells you the height of which
    the node is at

    '''


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.res = []
        
        def loop(root, arr):
            
            if not root:
                return
            
            arr.append(root.val)
            
            if not root.left and not root.right:
                
                if sum(arr) == targetSum:
                    
                    self.res.append(arr)
                
            loop(root.left, arr.copy())
            loop(root.right, arr.copy())
            
        loop(root, [])
        return self.res

    '''

    - loop throught the tree using preorder
    - use arr.copy() to make paths to each leaf
    - if sum of the arr is equal to targetSum add it to res


    '''