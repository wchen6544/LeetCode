from typing import List
import time
import math

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","8"]]


class Solution:
    # Two Sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {} 
        for i in range(len(nums)):
            if target - nums[i] in m:
                return [m[target - nums[i]], i]
            m[nums[i]] = i
    '''
    uses hashmap and checks if the (target - number) in the map and if its not then it adds
    the current number into the hashmap
    
    Example:

    nums = [1,2]
    target = 3
    
    loop 1:
        3 - 1 = 2 which is not in the map
        m = {1: 0}

    loop 2:
        m = {1: 0}
        3 - 2 = 1 which is in the map so return [m[m[target - nums[i]]], i]
    '''

    # Palindrome Number
    def isPalindrome(self, x: int) -> bool:
        if x < 10 and x > 0: #Checks if the number is less than 10 but not negative which means its a 
            return True      #palindrome

        if x < 0: #If its negative then its not a palindrome
            return False

        '''
        num2 is x but a multiple of 10 so 123 is 100, 345 is 100
        (x // digit % 10) starts from the end of the number and goes up
        (x // num2 % 10) starts at the beginning of the number and goes down
        '''
        num2 = (10 ** len(str(x))) // 10
        num = x
        digit = 1
        while num != 0:
            num = num // 10
            if (x // digit % 10) != (x // num2 % 10):
                return False
            digit *= 10
            num2 /= 10
        return True

    # Roman to Integer
    def romanToInt(self, s: str) -> int:
        singles = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        doubles = { "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900 }
        count = 0
        total = 0
        while count != len(s):
            if count == len(s) - 1:
                total += singles[s[count]]
                count += 1
            elif s[count] + s[count + 1] in doubles:
                total += doubles[s[count] + s[count + 1]]
                count += 2
            else:
                total += singles[s[count]]
                count += 1
        return total


        '''
        - Uses 2 hashmaps one has the singles and ones has the doubles values
        - Uses a while loop to go through all the values, for loop not good here
        - Checks if value is not last character which prevents out of bonds error
        - Then checks for double pair then single pair and adds the count to total
        - Adds to count to progress the loop

        '''

    # Best Time to Buy and Sell Stock
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        smallest = prices[0]
        biggest = prices[1]

        # uses 2 pointer that are next to each other

        profit = 0
        for i in range(2, len(prices)):
            if biggest < smallest:
                smallest = biggest

                # smallest becomes biggest b/c that means that price is too high to buy

            else:
                if (biggest - smallest) > profit:
                    profit = biggest - smallest
            biggest = prices[i]

            # moves biggest b/c we need to check the rest of the days / values.

        if (biggest - smallest) > profit:
            profit = biggest - smallest

        # checks if new biggest is better day to sell then the day before.

        return profit

    # 3Sum
    def threeSum(self, nums):
        if len(nums) < 1:
            return []

        setsOfThree = []
        
        nums.sort()


        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            p1 = i + 1
            p2 = len(nums) - 1

            while p1 < p2:

                if nums[p1] + nums[p2] + nums[i] > 0:
                    p2 -= 1

                # of the pair is too small then you need to make the first pointer larger
                elif nums[p1] + nums[p2] + nums[i] < 0:
                    p1 += 1
                    
                else:
                    setsOfThree.append([nums[p1], nums[p2], nums[i]])
                    p1 += 1

                    # skips duplicates
                    while nums[p1] == nums[p1 - 1] and p1 < p2:
                        p1 += 1

        return setsOfThree    

        '''
        sortedList = [-4, -1, -1, 0, 1, 2]

        - when it gets to the first -1 (i = 1, p1 = 2, p2 = 5) it finds the first triple (-1 + -1 + 2 = 0), then

          it looks at (-1 + 0 + 2) b/c the while loop is still ongoing since p2(5) is still bigger than p1(3), it
        
          then sees (-1 + 0 + 1) which is another triple.
    
        - purpose of continue is to not do execute the while loop if there is a duplicate so you don't get repeat triples.

        '''
     

    # Two Sum II - Input Array Is Sorted
    def twoSum2(self, numbers, target):
        p1 = 0
        p2 = len(numbers) - 1
        
        # set up your two pointers, one in the beginning, one in the end

        for i in range(len(numbers)):

            # if the pair is too big then you need to make the second pointer smaller 
            if numbers[p1] + numbers[p2] > target:
                p2 -= 1

            # of the pair is too small then you need to make the first pointer larger

            elif numbers[p1] + numbers[p2] < target:
                p1 += 1
            else:
                return [p1 + 1, p2 + 1]

    # Zigzag Conversion
    def convert(self, s, numRows):
        if numRows < 2:
            return s

        returnString = ""
        setsOfList = [[] for _ in range(numRows)]
        count = 0
        count2 = 0
        decreasing = False

        while count2 != len(s):

            setsOfList[count].append(s[count2])

            if count < numRows - 1 and not decreasing:
                count += 1
            else:
                decreasing = True
                count -= 1
                if count == 0:
                    decreasing = False
            count2 += 1

        for i in setsOfList:
            returnString += ("".join(i))
        return returnString
        '''
    
        -   the basic pattern of this problem is that is you increase a count by 1 until it reaches 

            the (numRows - 1) b/c now its beginning that
          
            zigzag patten which you now decrease count by 1 so that it resembles the zigzag. 

        -   when count reaches 0 you need to add a (decreasing/increasing) boolean to tell the loop

            whether or not it has reached the top/bottom of 

            the zigzag


        '''

    # Container With Most Water
    def maxArea(self, height):

        l = 0
        r = len(height) - 1
        maxArea = 0
        while r > l:
            
            if min(height[l], height[r]) * (r - l) >= maxArea:
                maxArea = min(height[l], height[r]) * (r - l)

            if height[l] > height[r]: 
                r -= 1
            else: 
                l += 1
        return maxArea

        '''
        - simple two pointer problem where we have to move the smaller pointer in hopes of getting a greater maxArea of water

        '''

    # Valid Parentheses
    def isValid(self, s):
        stack = []
        closing = {")", "]", "}"}
        pairs = {"{}", "[]", "()"}

        for i in range(len(s)):
            if len(stack) == 0 and s[i] in closing:
                return False

            if len(stack) != 0 and s[i] in closing:

                if stack[-1] + s[i] in pairs:
                    stack.pop(-1)
                else:
                    return False


            if s[i] not in closing:
                stack.append(s[i])

        if len(stack) != 0:
            return False
        return True
        '''

        - simple stack problem where you have to check if the stack contains the corrosponding opening character example you have a "}" 

        and the only thing in your stack is a "{" then its good but if your stack is like this ["{", "["] but now you have a ")" then 

        your stack is invalid because "[)" is not valid

        '''

    # Valid Sudoku
    def isValidSudoku(self, board):

        setsOfThree = [[] for _ in range(9)]

        for row in range(len(board)):
            cols = []
            rows = []
            for col in range(len(board)):

                if board[col][row] in cols:
                    return False
                if board[col][row] != ".":
                    cols.append(board[col][row])
                if board[row][col] in rows:
                    return False

                if board[row][col] != ".":
                    rows.append(board[row][col])

                if board[row][col] in setsOfThree[(col // 3) + ((row // 3) * 3)] and board[row][col] != ".":
                    return False

                setsOfThree[(col // 3) + ((row // 3) * 3)].append(board[row][col])


        return True

        '''

        - simple math and list problem where you have to split up the problem into 3 smaller ones

        - first problem is to check if each row is valid

        - second problem is to check if each col is valid

        - last problem is to check if each set of three is valid

        - math behind the last problem is (col // 3) + ((row // 3) * 3) where you are appending to

        a certain list depending on the values of row and col. 

        '''



    # Combination Sum
    def combinationSum(self, candidates, target):
        res = []

        def dfs(i, cur, total, callType):
            if total == target:
                res.append(cur[:])
                return

            if total > target or i >= len(candidates):
                return


            cur.append(candidates[i])

            dfs(i, cur, total + candidates[i], 1)

            cur.pop()

            dfs(i + 1, cur, total, 2)


        dfs(0, [], 0, 0)

        return res


        '''
        - backtracking problem
        - tree structure

                   []
                  /  \
                [1]  [2]
                /  \
            [1,1] [1,2] 
            / \
      [1,1,1] [1,1,2]

        - reason there is two dfs calls in the function dfs is b/c it needs to check for other possibilities if a set of nums

          either done or impossible like [1,1,1] is done b/c 1+1+1 is 3 so it checks if [1,1,2] is possible which is not so it ends the node

        - when [1,1] checked all possibilities it pops a 1 so its [1] and it checks [1,2] b/c you are adding (1 + i) to force it to skip 1 and 

          go straight to 2. 

        - then when it checked all possibilities of [1], it pops the 1 so now its [] and it goes to [2] b/c of (1 + i).


        '''


    # Binary Watch
    def readBinaryWatch(self, turnedOn):

        if turnedOn > 8:
            return []

        times = [1,2,4,8,16,32,60,120,240,480]

        res = []
        formattedRes = []

        def dfs(i, cur, recLength, total):

            if recLength == turnedOn and total <= 719:

                if 4 in cur and 8 in cur and 16 in cur and 32 in cur:
                    return

                res.append(sum(cur))
                return

            if i >= len(times) or total > 719:
                return


            cur.append(times[i])

            dfs(i + 1, cur, recLength + 1, sum(cur))

            cur.pop()

            dfs(i + 1, cur, recLength, sum(cur))

        dfs(0, [], 0, 0)

        for i in res:
            
            if i%60 < 10:

                minutes = "0{0}".format(str(i%60))

            else:

                minutes = str(i%60)

            hours = i // 60



            formattedRes.append("{0}:{1}".format(str(hours), minutes))



        return formattedRes




    # Rotate Image
    def rotate(self, matrix):


        for row in range(len(matrix)):
            for col in range(row, len(matrix)):
                temp = matrix[row][col]

                matrix[row][col] = matrix[col][row]

                matrix[col][row] = temp

        '''
        - converts the rows into columns
        [1,2,3]      [1,4,7]
        [4,5,6]  ->  [2,5,8]
        [7,8,9]      [3,6,9]
        
        - if you don't have the row in `for col in range(row, len(matrix))` then

          you are going to be editing values in the matrix that you already set which is bad.
        '''

        for r in range(len(matrix)):
            for c in range(len(matrix) // 2):

                t = matrix[r][c]
                matrix[r][c] = matrix[r][len(matrix) - 1 - c]
                matrix[r][len(matrix) - 1 - c] = t

        '''
        - flips each row

        - the reason for the len(matrix) // 2 is because you don't need to flip the middle index and only 1 side since
          you are doing 2 changes per loop

        - [0,0] turns to [0,2]
          [0,1] turns to [1,2]
          [0,2] turns to [2,2]


        '''
    # Contains Duplicate
    def containsDuplicate(self, nums):
        m = set()

        for i in nums:
            if i not in m:
                m.add(i)
            else:
                return True

        return False

    '''
    - uses a set instead of a stack b/c a stack takes too long when you have list that are very large
    - sets use a key so its O(1) compared to O(n) for stack

    '''

    # Product of Array Except Self
    def productExceptSelf(self, nums):
        total = 1
        totalNo0 = 1



        for i in nums:
            total *= i
            if i != 0:
                totalNo0 *= i

        if nums.count(0) > 1:
            totalNo0 = 0



        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = totalNo0
            else:
                nums[i] = total // nums[i]

        return nums

    '''
    - logic based question

    - calculates the multiplication of the whole list
    [1,2,3,4] = 24
    - dividies by the number so 24 // 1 = 24
                                24 // 2 = 12
    - when there is 2 zeros then everything will be a 0

    - when there is only 1 zero then it calculates the muliplication without that zero
      and then whenever it loops and sees the zero it will use the calculation without
      that zero (totalNo0)


    '''
        

    # Permutations
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums.copy()]
        
        completed = []

        def dfs(array, empArray):
            '''
        
            - base case is [1] which we just return it

            '''
            if len(array) == 1:
                empArray.append(array[0])
                completed.append(empArray)
                return empArray

            else:

                if len(array) > 1: # reason you check if len(array) > 1 is b/c there are multiple paths the array can take
                                   # for example [1,2,3,4] and [1,2,4,3]
                    '''
                    - if you have array = [2,3,4], empArray = [1] then
                    
                    you have to create a whole new search for [1,3] and [1,4], [1,2] is handled

                    through the code outside the for loop on the bottom b/c 2 is the zero index of the array

                    '''
                    for i in range(1, len(array)):
                        # the reason we start at 1 is b/c we are checking combos after the inital one the intial is handled below the for loop
                        # ex [1,3,4,2] and [1,4,3,2] no need to do [1,2,3,4] b/c its handled at the end.
                        newArray = array.copy()
                        newEmp = empArray.copy()

                        d = newArray.pop(i)
                        newEmp.append(d)

                        dfs(newArray, newEmp)




                c = array.pop(0)
                empArray.append(c)

                dfs(array, empArray)


        for i in range(len(nums)):

            a = nums.copy()
            b = a.pop(i)

            emp = []
            emp.append(b)
            dfs(a, emp)


        return completed


    # Search in Rotated Sorted Array
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r + l) // 2

            if target == nums[mid]:

                return mid

            if nums[l] <= nums[mid]:

                if target > nums[mid] or target < nums[l]:

                    l = mid + 1

                else:

                    r = r - 1


            else:

                if target < nums[mid] or target > nums[r]:
                    r = r - 1

                else:

                    l = mid + 1

        return -1








    # Coin Change

    def coinChange(self, coins: List[int], amount: int) -> int:



        '''
        Explanation:

            This is a memorization question so you have to keep track of everything before during your for loops
            
            coins = [1,2,3]
            amount = 10

            To make a 1 you need 1 coin, to make a 2 you need 1 coin, to make a 3 you need 1 coin

            TO make a 4 you need to look through all of your COINS and you see that you can make a 4 with either a (2 and 2) or
            a (1 and 3). BOTH require 2 coins so its {4: 2}

            Make sure you add the (if i not in m) in your code b/c you are getting the smallest amount of coins so you need a 
            starting value as your "biggest".

            Finally you add a (if amount in m) to check if it is possible to make the amount given the coin list. If it is impossible
            then you return -1

        '''


        m = {}

        if amount == 0: return 0
        
        for i in range(1, amount + 1):

            total = 0

            for c in coins:

                if c == i:

                    m[i] = 1

                    break

                else:

                   if (i - c) in m:

                        if i not in m:

                            m[i] = m[i - c] + m[c]

                        if m[i - c] + m[c] < m[i]:
                            m[i] = m[i - c] + m[c]


        if amount in m:

            return m[amount]

        return -1

                

    # Count and Say
    def countAndSay(self, n: int) -> str:
        
        '''
        
        the "base case" is 1 which you just return 1

        Basically this is a "recursive" question where you are given a number and you are looping
        that many times

        Example: n = 3
        Output = 21

        Loop 1: 1
        Loop 2: 11 (there is 1 count of 1)
        Loop 3 : 21 (there is 2 counts of 1)


        You have to make a for loop that looks for how many times a number appears in a row

        Example: 1123

        the number 1 appears 2 times in a row (2 counts of 1) = 21
        the number 2 appears 1 time (1 count of 2) = 12
        the number 3 appears 1 time (1 count of 3) = 13

        return = 211213

        '''





        start = 1
        it = "1"

        if n == 1: return "1"

        for i in range(2, n + 1):

            string = ""
            saw = []
            num = it[0]
            count = 0
            for letter in range(len(it)):
                if it[letter] == num:
                    count += 1
                else:
                    string += str(count) + str(num)
                    count = 1
                    num = it[letter]


            if count != 0:

                string += str(count) + str(num)
            
            it = string

        return it


    # House Robber
    def rob(self, nums: List[int]) -> int:

        '''
    
        Example: [2,7,9,3,1]

        At the first number, the max rob value is 2
        At the second number, the max rob value is 7

        At the third number, the max rob value is 11
        Explanation:
            You can rob house 2 and 9
            You can rob house 7 only

        At the fourth number, the max rob is 11
            You can rob house 2 and 9
            You can rob house 7 and 3

        At the fifth number, the max rob is 12
            You can rob house 2, 9, and 1 
            You can rob house 7 and 3


        Code Explanation:

            Loop 1:

                tempValue = max(2 + 0, 0)
                          = 2
                rob1 = 0 (we set rob1 to 0 because on the next loop we 
                            cannot add it to the next number because it will cause it
                            to be adjacent | EX: 2 + 7)

                rob2 = 2 (we set rob2 to 2 is because on the next loop it will either be the max of
                            2 or 7)

        '''

        rob1, rob2 = 0, 0

        for i in nums:
            tempValue = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = tempValue

        return rob2


    # Decode Ways
    def numDecodings(self, s: str) -> int:

        '''

        Time Complex: O(n)
        Space Complex: O(n) 

        Loop starting from the back

        1   1    1   0   2


        1   1    0   0   1
        +   +    +
        1   0    1
        =   =    =
        2   1    1


        There is only 1 way to make a 2
        There is 0 ways to make a 02
        There is 1 way to make a 102 which is (10, 2)
        There is 1 way to make a 1102 which is (1, 10, 2)
        There is 2 ways to make a 11102 which is (1, 1, 10, 2) and (11, 10, 2)
        '''


        dp = { len(s): 1 }

        # Looping backwards (5,4,3,2,1,0)

        for i in range(len(s) - 1, -1, -1):

            if s[i] == "0":

                dp[i] = 0

            else:

                dp[i] = dp[i + 1]


            # checks if there is a number that comes after the current one
            # wouldn't check if (i == last number) because there is nothing
            # that comes after

            if (i + 1 < len(s)):

                # checks if s[i] is 0 b/c if s[i] is 0 then you can't have 01, 02, 03 ...

                if (s[i] != "0"):

                    # if s[i] not 0 and there is a number after s[i] then you add the two numbers
                    # to check if it is less than 27.

                    if int(s[i] + s[i + 1]) < 27:

                        # if the two numbers is less than 27 then you want to add dp[i + 2] to 
                        # dp[i]

                        dp[i] += dp[i + 2]

        return dp[0]


    # Unique Paths
    def uniquePaths(self, m: int, n: int) -> int:

        # m = rows
        # n = columns


        '''

        Loops through all of the spaces in the array and calculates how many moves it takes to reach

        Example

        3x7

        [ 

            [1, 1, 1,  1,  1,  1, 1] 
            [1, 2, 3,  4,  5,  6, 7] 
            [1, 3, 6, 10, 15, 21, 1] 
        ]

        To make a 7, you add the 1 above it and the 6 to the left of it
        To Make a 21, you add the 6 above it and the 15 to the left of it
    
        '''


        arr = [1] * n

        for row in range(1, m):
            for col in range(n):

                if row == 0:

                    arr.append(1)

                elif col == 0:

                    arr.append(1)


                else:

                    arr.append(arr[-1] + arr[len(arr) - n])


        return arr[-1]




    # Jump Game
    def canJump(self, nums: List[int]) -> bool:

        '''
        
        nums = [3,1,1,2,0,4]

        Explanation:

            You want to loop backwards starting from 4 going all the way back to 3. Our ending number is going to be the

            index of the last number which is 5. We check if the number at the current index of the for loop plus its index

            is greater or equal to the ending number

            Example:

                2 + 3 (index of 2) = 5 which is greater than 4.

            If the ending number is 0 then we can return True because it means that we are able to get from the last index

            to the first index.

        Steps:

            Loop 0
                ending = 5

            Loop 1
                i = 5
                4 + 5 >= 5
                ending = 5

            Loop 2
                i = 4
                0 + 4 >= 5 (nope)

            Loop 3
                i = 3
                3 + 2 >= 5
                ending = 3

            Loop 4
                i = 2
                1 + 2 >= 3
                ending = 2

            Loop 5
                i = 1
                1 + 1 >= 2
                ending = 1

            Loop 6
                i = 0
                3 + 0 >= 1
                ending = 0

            return ending == 0


        '''

        ending = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):

            if nums[i] + i >= ending:

                ending = i
        
        return ending == 0





        
sol = Solution()
start = time.time()
#print(sol.twoSum([3,3], 6))
#print(sol.isPalindrome(111))
#print(sol.romanToInt("LVIII"))
#print(sol.maxProfit([2,4,1]))
#print(sol.twoSum2([2,3,4], 6))
#print(sol.threeSum([-1,0,1,2,-1,-4]))
#print(sol.convert("ABC", 1))
#print(sol.maxArea([1,1]))
#print(sol.isValid("(])"))
#print(sol.isValidSudoku(board))
#print(sol.combinationSum([1,2], 3))
#print((sol.readBinaryWatch(5)))
#print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))
#print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
#print(sol.productExceptSelf([1,2,3,4]))
#print(sol.permute([1,2,0,0]))
#print(sol.search([4,5,6,7,0,1,2], 2))
#print(sol.coinChange([3,6],8))
#print(sol.countAndSay(5))
#print(sol.rob([2,7,9,3,1]))
#print(sol.numDecodings("06"))
#print(sol.uniquePaths(3,7))
#print(sol.canJump([3,1,1,2,0,4]))

print("--- %s seconds ---" % (time.time() - start))

