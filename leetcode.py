from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    theMap = dict()
    for i in range(len(nums)):
        if nums[i] not in theMap:
            theMap[nums[i]] = i
        if target - nums[i] in theMap and i != theMap[target - nums[i]]:
            print(theMap)
            return [theMap[target - nums[i]], i]


def reverse(x: int) -> int:
    negative = 1
    if x <= 0:
        negative = -1
        num = x * -1
        if num < 10:
            return num
    else:
        num = x
    pos_nums = []
    while num != 0:
        pos_nums.append(str(num % 10))
        num = num // 10
    sol = int(''.join(pos_nums)) * negative
    if abs(sol) > 2 ** 31:
        return 0
    return sol


def climbStairs(n: int) -> int:
    one, two = 1, 1
    for i in range(n - 1):
        one = one + two
        two = one - two
    return one


def threeSum(nums: List[int]) -> List[List[int]]:
    solutions = []
    if len(nums) < 3:
        return []
    a = dict()
    for i in range(len(nums)):
        a[nums[i]] = i
    aa = dict()
    for i in range(len(nums)):
        for k in range(i + 1, len(nums)):
            if (nums[i] + nums[k]) * -1 in a:
                if i != k and i != a[(nums[i] + nums[k]) * -1] and k != a[(nums[i] + nums[k]) * -1]:
                    if tuple(sorted([nums[i], nums[k], (nums[i] + nums[k]) * -1])) not in aa:
                        aa[tuple(sorted([nums[i], nums[k], (nums[i] + nums[k]) * -1]))] = ""
                        solutions.append([nums[i], nums[k], (nums[i] + nums[k]) * -1])
    return solutions


def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    strX = list(str(x))
    revStrX = list(str(x))
    revStrX.reverse()
    print(strX, revStrX)
    if strX == revStrX:
        return True
    return False


def romanToInt(s: str) -> int:
    conversions = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i != len(s) - 1 and conversions[s[i]] < conversions[s[i + 1]]:
            total -= conversions[s[i]]
        else:
            total += conversions[s[i]]
    return total


def addBinary(self, a: str, b: str) -> str:
    total = int(a, 2) + int(b, 2)
    return str(int(self.decToBin(total)))


def decToBin(self, num):
    if num == 0:
        return 0
    else:
        return str(self.decToBin(num // 2)) + str((num % 2))


def longestCommonPrefix(strs: List[str]) -> str:
    string = ""
    shortest = strs[0]
    if shortest == "":
        return ""
    else:
        for i in strs:
            if len(i) < len(shortest):
                shortest = i
        for i2 in range(len(strs)):
            strs[i2] = strs[i2][0:len(shortest)]
        for i3 in range(len(strs[0])):
            for i4 in range(1, len(strs), 1):
                if strs[0][i3] != strs[i4][i3]:
                    return string
            string += strs[0][i3]
    return string
