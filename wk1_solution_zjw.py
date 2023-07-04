## 21

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        print(list1)
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2

## 231
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        elif (n%2 != 0):
            return False
        
        return self.isPowerOfTwo(n/2)

## 203
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # create a pseudo node
        sentinel = ListNode(0)
        sentinel.next = head
        
        # 2 pointers
        pre, curr = sentinel, head

        while curr:
            if curr.val == val:
                pre.next = curr.next # it will skip the current node and directly link the pre node to next of current node
            else:
                pre = curr
            curr = curr.next
        
        return sentinel.next # always link to head
    
## 698
# backtrack + sort + memoization
class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        summ = sum(arr)
        
        # not divisible
        if summ % k != 0:
            return False

        target_sum = summ // k

        # sorting will accelerate
        arr.sort(reverse=True)

        taken = ['0'] * n
        
        memo = {} # memoization
        
        def backtrack(index, count, curr_sum):
            n = len(arr)
            taken_str = ''.join(taken)

            if count == k - 1:
                return True
            
            if curr_sum > target_sum:
                return False
            
            if taken_str in memo:
                return memo[taken_str]
            
            if curr_sum == target_sum:
                memo[taken_str] = backtrack(0, count + 1, 0)
                return memo[taken_str]
         
            for j in range(index, n):
                if taken[j] == '0':
                    # init
                    taken[j] = '1'
                    
                    if backtrack(j + 1, count, curr_sum + arr[j]):
                        return True
                    # Backtrack step.
                    taken[j] = '0'
                    
            memo[taken_str] = False
            return memo[taken_str] 
        
        return backtrack(0, 0, 0)
    

    
## 794
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        d = {"X":1,"O":-1," ":0}
        board_int = [d[strs] for strs in "".join(board)] # int list
        summ = sum(board_int)
        # ensure X - O ==1 or 0, that is, sum of board ==1
        if summ < 0 or summ >1: 
            return False
        
        # if it has winner but no end, it is also a failure; that means we need to check the set of row/col/diag summations
        cases = {
            sum(board_int[:3]), sum(board_int[3:6]), sum(board_int[6:9]), # row
            board_int[0]+board_int[3]+board_int[6], # col1
            board_int[1]+board_int[4]+board_int[7], # col2
            board_int[2]+board_int[5]+board_int[8], # col3
            board_int[0]+board_int[4]+board_int[8], board_int[2]+board_int[4]+board_int[6] # diag
        }
        
        if summ==1: # one more X than O
            n = -3 # if there is 3 O, then it is conflicting
        else: # X == # O, that means X just finished, and final O goes
            n = 3 # X wins, which is conflicting

        if n in cases:
            return False

        return True
    
## 761
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return s

        peak_strings = []
        anchor = balance = 0

        for i, char in enumerate(s):
            if char == '1':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                special = self.makeLargestSpecial(s[anchor + 1: i])
                peak_strings.append("1{}0".format(special))
                anchor = i + 1

        peak_strings.sort(reverse=True)
        result = "".join(peak_strings)
        return result

    
