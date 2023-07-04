## 108

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(l,r):
            """
            helper function to identify root and categorize left and right
            """
            if l > r:
                return None

            # choose left middle node as root
            p = (l + r) // 2

            # preorder node left right
            root = TreeNode(nums[p])
            root.left = helper(l,p-1)
            root.right = helper(p+1,r)
            return root
        
        return helper(0,len(nums)-1)
    
## 169
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def helper(l,r):
            # base case
            if l == r:
                return nums[l]
            
            m = (r - l)//2 + l
            left = helper(l,m)
            right = helper(m+1,r)

            if left == right:
                return left
            
            else:
                leftc = sum(1 for i in range(l,r+1) if nums[i]==left)
                rightc = sum(1 for i in range(l,r+1) if nums[i]==right)
            
                return left if leftc > rightc else right
            
        return helper(0,len(nums)-1)
    
## 240
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # empty
        if not matrix:
            return False

        def helper(l,u,r,d):
            if l > r or u > d:
                return False
            
            if target < matrix[u][l] or target > matrix[d][r]:
                return False

            m = l + (r - l) // 2

            row = u
            while row <= d and matrix[row][m] <= target:
                if matrix[row][m] == target:
                    return True

                row += 1

            return helper(l,row,m-1,d) or helper(m+1,u,r,row-1)
        m = len(matrix[0]) - 1
        n = len(matrix) - 1 
        return helper(0, 0, m, n)

## 932
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        # memoization init
        mem = {1:[1]}
        def helper(n):
            if n not in mem:
                odd = helper( (n+1) // 2 )
                even = helper( n // 2 )
                mem[n] = [2 * i - 1 for i in odd] + [2 * i for i in even]
            return mem[n]
        
        return helper(n)
    
# 973
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x):
            return x[0] ** 2 + x[1] ** 2

        points.sort(key = dist)
        return points[:k]
    

# 23
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @classmethod
    def merge2L(self,list1,list2):
        # init
        p = ListNode(0) # points
        h = p

        while list1 and list2:
            if list1.val > list2.val:
                p.next = list2
                list2 = list1
                list1 = p.next.next
            else:
                p.next = list1
                list1 = list1.next
            p = p.next

        if list1:
            p.next = list1
        else:
            p.next = list2
        return h.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        count = 1 
        while count < n:
            for i in range(0, n - count, 2 * count):
                lists[i] = self.merge2L(lists[i], lists[i + count])

            count = 2 * count
            
        if n > 0:
            return lists[0]
        else:
            return None