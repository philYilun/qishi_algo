# Q1
# 108 Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 0:
            return None

        if n == 1:
            return TreeNode(nums[0])

        mid = n // 2
        left = nums[:mid]
        right = nums[mid + 1:]

        return TreeNode(val = nums[mid], left = self.sortedArrayToBST(nums[:mid]) , right = self.sortedArrayToBST(nums[mid + 1:]))


# Q2
# 169
from typing import List
class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
        # traverse the list with one counter
        # initialize the count and candidate variables
        count = 0
        candidate = None

        # iterate through the array
        for num in nums:
            # if count is 0, update the candidate variable
            if count == 0:
                candidate = num
            # increment or decrement count based on whether the current element is the candidate
            count += (1 if num == candidate else -1)

        # return the candidate variable
        return candidate

    def majorityElement2(self, nums: List[int]) -> int:
        # divide and concur
        # initialize the count and candidate variables
        return self.helper(nums, 0, len(nums))[0]

    def helper(self, nums: List[int], l: int, r: int)  :

        if l == r - 1:
            return nums[l], 1

        mid = l + ( r - l) // 2
        maj_left, cnt_left = self.helper(nums, l, mid )
        maj_right, cnt_right = self.helper(nums, mid, r)

        if maj_left == maj_right:
            return maj_left, cnt_left + cnt_right

        elif cnt_left > cnt_right:
            maj = maj_left
            cnt = cnt_left - cnt_right
            return maj, cnt
        else:
            return maj_right, cnt_right - cnt_left

# Q3
# 240
# https://leetcode.com/problems/search-a-2d-matrix-ii/
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true

# find a middle point, compare it with target, and then use the sub area to do split again.
# exit point: when the area is 1 row 1 col, do compare
# use a close range i.e. include the mid point

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def recurse(ur, lr, lc, rc): # upper row, lower row, left col, right col
            if ur > lr or lc > rc:
                return False

            if ur == lr and lc == rc:
                return matrix[ur][lc] == target

            m_min, m_max = matrix[ur][lc], matrix[lr][rc]

            if m_min <= target <= m_max:
                mr, mc = ur + (lr - ur) // 2 , lc + (rc - lc) // 2
                return recurse(ur, mr, lc, mc) or recurse(ur, mr, mc + 1, rc) or recurse(mr + 1, lr, lc, mc) or recurse(mr + 1, lr , mc + 1, rc)
            return False

        return recurse(0,  len(matrix) - 1, 0,len(matrix[0]) - 1)

# Q4
# 932
# https://leetcode.com/problems/beautiful-array/
# Input: integer
# Output: a list satisfy the condition

# based on observation, the condition satisfy when there is no 2 items that with distance > 1 is both even or both odd.
# so we need to swap the list till there is only 1 element on a sublist

class Solution:
    def beautifulArray(self, n: int)  :
        return self.rec(list(range(1, n + 1)))


    def rec(self,list):
        if len(list) <= 1:
            return list
        else:
            return self.rec(list[::2]) + self.rec(list[1::2])

# Q5
# 973
import random

class Solution:
    def kClosest(self, points , k: int) :

        distances = [(x**2 + y**2, (x, y)) for x,y in points]


        def partition(l, r):
            index = random.randint(l, r)  #randonly pick a point
            pivot = distances[index][0]   # get the value of the point
            distances[index], distances[r] = distances[r], distances[index] # move this index to the right end
            storeIndex = l # start from left end
            for i in range(l, r):    # traverse from left to right
                if distances[i][0] < pivot:  # if less than the random point
                    distances[storeIndex], distances[i] = distances[i], distances[storeIndex] # one by one switch to move the smaller one to the front
                    storeIndex += 1

            distances[storeIndex], distances[r] = distances[r], distances[storeIndex]
            return storeIndex   # how many item is less than the random one

        def quickselect(l, r, k):
            if l < r:
                pindex = partition(l, r)
                if pindex == k:
                    return
                elif pindex < k:
                    quickselect(pindex + 1, r, k)
                else:
                    quickselect(l, pindex - 1, k)

        distances = [(x**2 + y**2, (x,y)) for x,y in points]
        quickselect(0, len(distances)-1, k)
        return [coord for _, coord in distances[:k]]

# Q6
# 23
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1 , list2 )  :
        # create a separate ListNode to store the sorted list
        if list1 and list2:
            if list1.val <= list2.val :
                head, list1 = list1, list1.next
            else:
                head, list2 = list2, list2.next

            head.next = self.mergeTwoLists(list1, list2)
            return head
        else:
            return list1 or list2

    def mergeKLists(self, lists ) :
        if not lists:
            return null
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.mergeTwoLists(lists[0],lists[1])
        else:
            n = len(lists)
            m = n // 2
            return self.mergeTwoLists(self.mergeKLists(lists[: m]),self.mergeKLists(lists[m:]))
