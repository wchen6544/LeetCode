
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

    # Binary Tree Inorder Traversal
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

    # Binary Tree Preorder Traversal
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

    # Binary Tree Postorder Traversal
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

    # Invert Binary Tree
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

    # Increasing Order Search Tree
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
    
    # Find Mode in Binary Search Tree
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

    # Range Sum of BST
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


    # Find a Corresponding Node of a Binary Tree in a Clone of That Tree
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


    # Root Equals Sum of Children
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        
        return root.left.val + root.right.val == root.val

        '''

        - check if left root plus right root is equal to parent root value

        '''

    # Balanced Binary Tree
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


    # Same Tree
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

    # Symmetric Tree
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


    # Maximum Depth of Binary Tree
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
            
            
    # Minimum Depth of Binary Tree
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


    # Path Sum
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


    # Sum of Left Leaves
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


    # Minimum Absolute Difference in BST
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


    # Search in a Binary Search Tree
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


    # Convert Sorted Array to Binary Search Tree
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


    # Binary Tree Paths
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


    # Merge Two Binary Trees
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

    # Sum Root to Leaf Numbers
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


    # Binary Tree Level Order Traversal
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


    # Path Sum II
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

    # Construct Binary Tree from Inorder and Postorder Traversal
    def buildTreePost(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def loop(inorder, postorder):
            
            
            if len(inorder) == 0 or len(postorder) == 0:
                return

            if len(inorder) == 1:
                postorder.pop(-1)
                return TreeNode(inorder[0])


            root = TreeNode(postorder[-1])
            popped = postorder.pop(-1)

            rStuff = inorder[inorder.index(popped) + 1::]

            root.right = loop(rStuff, postorder)

            lStuff = inorder[0:inorder.index(popped)]
            root.left = loop(lStuff, postorder)

            return root
        
        return loop(inorder, postorder)
    
    '''
    
    - postorder[-1] = root
    - first tranverse right of the root
    - if length of inorder equals 1, pop the last index of postorder 
        and return the TreeNode of inorder[0]
    
    - when tranversing right, take everything after the postorder[-1] node    
    - when tranversing left, take everything before the postorder[-1] node
    
    '''



    # Construct Binary Tree from Preorder and Inorder Traversal
    def buildTreePre(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def loop(preorder, inorder):
            
            
            if len(preorder) == 0 or len(inorder) == 0:
                return
            
            if len(inorder) == 1:
                preorder.pop(0)
                return TreeNode(inorder[0])
            
            
            root = TreeNode(preorder[0])

            preorder.pop(0)
            root.left = (loop(preorder, inorder[0:inorder.index(root.val)]))
            root.right = (loop(preorder, inorder[inorder.index(root.val) + 1: len(inorder)]))
        
            return root
        
        return loop(preorder, inorder)


    '''

    - preorder[0] = root
    - tranverse left, take inorder from index of 0 to the preorder[0] root
    - tranverse right, take inorder from the preorder[0] root to the end
    - if length of inorder equals 1, pop preorder of 0 and return the TreeNode of inorder[0]

    '''

    # Subtree of Another Tree
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        self.res = False
        
        def loop(root):
            
            if not root:
                return
            
            loop(root.left)
            loop(root.right)
            
            
            if compare(root, subRoot):
                self.res = True
        
        def compare(root, subRoot):
            
            if not root and not subRoot:
                return True
            
            if not root or not subRoot or (root.val != subRoot.val):
                return False
            
            return compare(root.left, subRoot.left) and compare(root.right, subRoot.right)
                
            
                
        loop(root)
        return self.res
    
    
    '''
    - to split the tree into subtrees, loop left and loop right, then the root 
    will be a subtree
    - check each subtree
        - if both root and subRoot doesn't exist, True
        - if one exist and the other doesn't or their values are not equal, False
        - return compare(left) and compare(right)
        
    '''


    # Most Frequent Subtree Sum
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        self.m = {}
        self.biggest = 1
        self.res = []
        
        def loop(root):
            if not root:
                return 0
            
            l = loop(root.left)
            r = loop(root.right)
            
            self.m[l + r + root.val] = self.m.get(l + r + root.val, 0) + 1
            
            return root.val + l + r
            
        
        loop(root)
        
        for i in self.m:
            
            numberOfOccur = self.m[i]
            
            if numberOfOccur == self.biggest:
                self.res.append(i)
            if numberOfOccur > self.biggest:
                self.res = [i]
                self.biggest = numberOfOccur
        
        return self.res


    '''
    
    - use a hashmap and add the # of occurrences of sum of subtree
    - to get the sum of subtrees
        - set a l = loop(left)
        - set a r = loop(right)
        - the sum is equal to root.val + l + r
        return root.val + l + r to set the l and r values

    '''


    # Kth Smallest Element in a BST
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.smallest = 0
        self.k = k
        
        def loop(root):
            
            if not root:
                return
            
            loop(root.left)
            
            self.k -= 1
            
            if self.k == 0:
                self.smallest = root.val
            
            loop(root.right)
        
        loop(root)
        return self.smallest


    '''

    - binary tree, the left will always be the smallest, followed by the root,
    then the right


    '''

    # Unique Binary Search Trees
    def numTrees(self, n: int) -> int:
        
        nums = [1] * (n + 1)
        
        for i in range(2, n + 1):
            
            total = 0
            
            for i2 in range(1, i + 1):
                
                l = i2 - 1
                r = i - i2
                
                total += nums[l] * nums[r]
            
            nums[i] = total
        
        return nums[n]


    '''
    
    Example

    - If n = 3, make a list with [1] * (n + 1), so list = [1,1,1,1]
    - first for loop goes from 2 to n + 1, so 2, 3 (if n = 3)
    - set a total = 0
    - second for loop goes from 1 to i + 1
    - left is second for loop index minus 1
    - right is first for loop index minus second for loop index
    - total += the left times right

    n = 3

    1           1           1
     
    = 1 * 2    = 1 * 1     = 2 * 1
    = 2        = 1         = 2

    total = 2 + 1 + 2
    = 5

    '''

    # Binary Tree Tilt
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.tilt = 0
        
        def loop(root):
            if not root:
                return 0
            
            
            l = loop(root.left)
            r = loop(root.right)
            
            self.tilt += abs(l - r)
            
            return root.val + l + r
        
        loop(root)
        return self.tilt
    
    
    '''
    
    - loop left and loop right
    - add the abs of left minus right to tilt
    - return root.val + left + right
    
    
    '''


    # Binary Tree Zigzag Level Order Traversal
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            
        if not root:
            return []
        
        res = []
        queue = [root]
        direction = 1
        while len(queue) > 0:
            
            level = []
            qLength = len(queue)

            for i in range(qLength):
                
            
                level.append(queue[0].val)
                
                popped = queue.pop(0)
                
                if popped.left: 
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
                        

            if level:
                if direction % 2 == 0:
                    
                    for i in range(len(level) // 2):
                        
                        temp = level[len(level) - 1 - i]
                        level[len(level) - 1 - i] = level[i]
                        level[i] = temp
                
                res.append(level)

            direction += 1
        
        return res


    '''
    - same as level order search but now on every other level, we
    flip the list so that its backwars. Ex: [1,2,3] becomes [3,2,1]

    '''


    # Binary Tree Right Side View
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
            
        if not root:
            return
        
        queue = [root]
        res = []
        
        while len(queue) > 0:
            
            qLength = len(queue)

            for i in range(qLength):
                
                if i == 0:
                    res.append(queue[0].val)
            
                popped = queue.pop(0)
                
                if popped.right:

                    queue.append(popped.right)

                if popped.left:

                    queue.append(popped.left)

        return res

    '''
    
    - same as level search, but when i == 0, append the queue[0] value to res
    because that is the rightmost value.

    Example:

        [3]
        / \
      [2] [4]
      /
    [1]
        
    - check right first and append to queue if found, then left
    - it will only append the first value to (res) so that will
    - either be the right most of the left one if the right one
    - doesn't exist

    '''


    # Add One Row to Tree
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def loop(root, level):
            
            if not root:
                return
            
            if level + 1 == depth:
                
                l = root.left
                
                root.left = TreeNode(val)
                
                root.left.left = l
                
                r = root.right
                root.right = TreeNode(val)
                root.right.right = r
                
                return
            
            if level + 1 < depth:
                
                loop(root.left, level + 1)
                loop(root.right, level + 1)
        
        if depth == 1:
            
            r = TreeNode(val)
            r.left = root
            return r
        
        else:
            loop(root, 1)
            return root

    '''

    - get the level of the node, (level + 1) every time you loop
    - if level + 1 is equal to the depth, that means that the 
    left and right of the current node should be equal to val
    - set variables (l) and (r) to equal the original left and right
    of the node and make the new left and right equal to TreeNode(val).
    - then set the left and right of those new nodes to equal the original
    left and right trees.

    '''


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max = float('-inf')
        
        def loop(root):
            
            if not root:
                return
            
            loop(root.left)
            loop(root.right)
            
            self.max = max(self.max, root.val)
            
            if root.left or root.right:
                
                getMax(root)
        
            
        
        def getMax(root):
            
            curMax = root.val
            total = root.val
            
            if root.left:
                
                curMax = max(curMax, root.left.val + root.val)
                total += root.left.val
            
            if root.right:
                
                curMax = max(curMax, root.right.val + root.val)
                total += root.right.val
            
            root.val = curMax
            largest = max(curMax, total)
            self.max = max(self.max, largest)
        
        loop(root)
        return self.max
        
        
        '''
        
        Tree
        
          (1)
         /   \
        (2)  (3)
               \
               (-5)
        
        - loop through the tree (postorder tranversal)
        - if the node has a leaf, check to see for largest
            - node (3) has a leaf (-5), so we check the total (-5 + 3) = -2
            - set root.val to the biggest, either itself, left side + root.val, or
            right side + root.val
            - check if the subtree is the biggest (compare to self.max)
            
        
        '''


    def goodNodes(self, root: TreeNode) -> int:
        
        self.rootNode = root.val
        self.res = 0
        
        def loop(root, nodeVal):
            if not root:
                return
            
            if root.val >= nodeVal:
                
                self.res += 1
            
                
            loop(root.left, max(nodeVal, root.val))
            loop(root.right, max(nodeVal, root.val))
        
        loop(root, root.val)
        return self.res


    '''
    
    Tree

          (1)
         /   \
        (2)  (3)
               \
               (-5)
    
    - loop through tree (preorder tranversal)
    - if root value is greater than or equal to the biggest in path, self.res += 1
    - when looping compare the max of the current biggest and root value.

    Example Loop

    Tree

          (1)
          /
        (2)
        /
      (3)
      /
    (1)
    
    self.res = 1 (b/c (1) is always a good node)

    - (2) is greater than 1 so loop(left, 2), self.res = 2
    - (3) is greater than 2 so loop(left, 3), self.res = 3
    - (1) is less than 3 and theres nothing after so do nothing


    '''


    class Codec:

    def serialize(self, root):
        
        self.res = []
        
        def loop(root):
            if not root:
                self.res.append("n")
                return
            
            self.res.append(str(root.val))
            
            loop(root.left)
            loop(root.right)
        
        loop(root)
        
        return ",".join(self.res)
    
    '''
    
    - preorder tranversal
    - append to array, return with a join split with comma
    
    
    '''

    def deserialize(self, data):

        vals = data.split(",")
        self.i = 0
        
        
        def loop():

            if vals[self.i] == "n":
                self.i += 1
                return None 
            
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = loop()
            node.right = loop()
            
            return node
    
        return loop()
    
    '''
    - loop through the data [1,n,n,2]
    - have a self.i which will be your iterator
    - check if the val[i] = n, return None
    - set a node to be a TreeNode with the val[i]
    - set left to loop
    - set right to loop
    - iterate self.i by one every time you are looping
    - return node
    
    '''