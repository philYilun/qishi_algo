from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode()
        cur = pre_head
        while list1 and list2:
            if list1.val < list2.val:
                cur.next, list1 = list1, list1.next
            else:
                cur.next, list2 = list2, list2.next
            cur = cur.next
        cur.next = list1 or list2
        return pre_head.next



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def helper(n):
            if (n == 2) or (n == 1) :
                return True 
            elif n <= 0 :
                return False
            elif n % 2 == 0:
                return helper(n/2)
            else:
                return False
        return helper(n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head_tmp = ListNode()
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        
        if head.val == val:
            head = head.next
        
        return head


#q4
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_value = sum(nums)
        if total_value % k != 0:
            return False
        
        sub_sum = total_value // k
        subset = [0] * k
        nums.sort(reverse = True)

        def recurse(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if subset[j] + nums[i] <= sub_sum:
                    subset[j] += nums[i]

                    if recurse(i + 1):
                        return True
                    
                    subset[j] -= nums[i]

                    if subset[j] == 0:
                        break
            return False
        return recurse(0)


#q5
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
 
# The validate state has 2 criteria
# the state is at the middle of the game
# the state is valid
#   1) num of Xs - num of Os is 0 or 1
#   2) the state is not a winning state:
#      X is not a winner if the # of moves is even, and
#      O is not a winner if the # of moves is odd.
        # map the character to number
        m = {'X': 1, 
             'O': -1, 
             ' ': 0}               
        
        # transform the 1x3 str array to a 1x9 int array
        s = [m[char] for char in ''.join(board)]        
        # Ex: ["XOX"," X ","   "] --> [1,-1,1,0,1,0,0,0,0]
        
        sm = sum(s)

        # identify invalid state
        if sm>>1: return False        
        
        if sm == 1: 
            n = -3 
        else :
            n = 3     
        
        # identify not winning state
        if n in {s[0]+s[1]+s[2], s[3]+s[4]+s[5], s[6]+s[7]+s[8], 
                 s[0]+s[3]+s[6], s[1]+s[4]+s[7], s[2]+s[5]+s[8],         
                 # the elements of the set are 
                 s[0]+s[4]+s[8], s[2]+s[4]+s[6]}: return False           
                 # the rows, cols, and diags
        
        return True                                                 
        # <-- both criteria are true


#q6
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # start location is 0
        l = 0
        # log if substring is ascending first and then descending
        balance = 0
        # log the latest string
        sublist = []
        # sublist is a list for all fragmented items

        # go through the start of the string, check when the sum of a substring is of balance == 0
        
        # 2 pointer?
        # r is the pointer go through the entire string
        # l is the pointer to log where the substring started
        # log all the substring to a list
        # rank the list descending
        # combine the list to the final output
        # recursion is used to do swap within a substring
        for r in range(len(s)):
            balance += 1 if s[r]=='1' else -1
            if balance==0:
                sublist.append("1" + self.makeLargestSpecial(s[l+1:r])+ "0")
                l = r+1
        
        sublist.sort(reverse=True)
        return ''.join(sublist)
        sublist.sort(reverse=True)
        return ''.join(sublist)
