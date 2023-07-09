# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


# Q1 167
class Solution:

        # idea. use binary search.
        # build a helper function, input with right left
        # traverse the first index through the list
    def helper(self, numbers, remainder, left, right):
        while left <= right:
            mid = left + (right - left)//2
            if numbers[mid] == remainder:
                return mid
            elif numbers[mid] > remainder:
                right = mid - 1
            else:
                left = mid + 1
        return

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        for i in range(length - 1):
            # start from the first and end with the second to last
            r = target - numbers[i]
            idx2 = self.helper(numbers, r, i + 1, length - 1)
            # the right side is the last item of the array
            if idx2:
                return [i + 1, idx2 + 1]

# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Q2 278
class Solution:
    def firstBadVersion(self, n: int) -> int:

        l = 1
        r = n

        while l <= r:
            m = l + (r - l)//2
            if isBadVersion(m) == False:
                l = m + 1
            elif isBadVersion(m) == True and m ==1:
                return m
            elif isBadVersion(m) == True and m > 1:
                if isBadVersion(m - 1) == True:
                    r = m - 1
                else:
                    return m


# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/



# Q3 702
class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        l = 0
        r = 10**4

        while l <= r:
            mid = l + (r - l)//2
            res = reader.get(mid)
            if (res == 2**31 - 1) or (res > target):
                r = mid - 1
            elif res == target:
                return mid
            elif res < target:
                l = mid + 1

        return -1

# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
#Q4 852
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # if mid > mid + 1 , r = mid
        # if mid > mid - 1, l = mid
        # if l = r
        l , r = 0 , len(arr) - 1

        while l < r - 1:
            mid = l + (r - l)//2

            if arr[mid] > arr[mid + 1]:
                r = mid
            else:
                l = mid

        return r

# https://leetcode.com/problems/ugly-number-iii/description/
# Q5 1201


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        a, b, c = sorted((a, b, c)) # get the smallest

        l = a
        r = a * n

        def hcf(x, y):
            if x == 1 or y == 1:
                return 1
            elif x % y == 0:
                return y
            else:
                return hcf(y, x % y)

        p, q, t = hcf(a, b), hcf(b, c), hcf(a, c)
        s = hcf(p, c)
        x1 = (a * b)//p
        x2 = (b * c)//q
        x3 = (a * c)//t
        x4 = (a * b * c * s)// (p * q * t)
        # print(p, q, t, x1, x2, x3, x4)
        while l <= r:
            mid = l + (r - l)//2
            n_est = mid // a + mid // b + mid // c - (mid // x1 + mid // x2 + mid // x3) + mid // x4
            # print(f"{mid} is middle pointer, {n_est} is the n by far")
            if n_est < n:
                l = mid + 1
            elif n_est > n:
                r = mid -1
            elif (mid % a == 0) or (mid % b == 0) or (mid % c == 0):
                return mid
            else:
                r = mid - 1
