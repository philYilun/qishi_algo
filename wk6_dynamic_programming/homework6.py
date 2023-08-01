# https://leetcode.com/problems/climbing-stairs/description/
# Q1 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        base1 = 1
        base2 = base1 + 1
        basek = base(k - 1) + base(k - 2)
        """
        if n < 3:
            return n
        skip1 = 1
        skip2 = 2
        for i in range(3, n + 1):
            skip1, skip2 = skip2, skip2 + skip1
        return skip2

# https://leetcode.com/problems/predict-the-winner/
# Q2 486. Predict the Winner


class Solution:
  def PredictTheWinner_r(self, nums ):
       # recursion
        def twoPointer(nums, left, right ):
            # return player1 score - player2 score
            if left == right:
                # when two pointer met, the difference will be the value
                return nums[left]

            score_diff_l = nums[left] - twoPointer(nums, left + 1, right)
            score_diff_r = nums[right] - twoPointer(nums, left, right - 1)
            return max(score_diff_l, score_diff_r)

        max_diff = -1
        max_diff = twoPointer(nums, 0, len(nums) - 1)
        return max_diff >= 0

    def PredictTheWinner_rm(self, nums ):
        """
        recursion with memory
        """
        memory = {} # dictionary, log when left = i, right = j, the best return

        def rec(i, j):
            if i == j:
                return nums[i]

            if (i, j) in memory:
                return memory[(i, j)]

            else:
                score = max(nums[i] - rec(i + 1, j), nums[j] - rec(i, j - 1))
                memory[(i, j)] = score
                return score

        return rec(0, len(nums) - 1) >= 0

    def PredictTheWinner_dp(self, nums ):
        """
        dp
        state, i, j. each dp[i][j] means the max benefit of this, given the value of next step.
        this is the easist way to understand.
        """
        size = len(nums)
        dp = [[-1 for i in range(size)] for j in range(size)]
        for i,j in enumerate(nums):
            dp[i][i] = j

        for i in range(size - 2, -1, -1): #left item, till the second to last
            for j in range(i + 1, size): #right item, from left + 1, till the last
                choose_left = nums[i] - dp[i + 1][j]
                choose_right = nums[j] - dp[i][j - 1]
                dp[i][j] = max(choose_left, choose_right)

        return dp[0][-1] >= 0

    def PredictTheWinner_1d_dp(self, nums ):
        """
        1 dimension dp
        when update dp[i][j], the item used is dp[i][j - 1] and dp[i + 1][j]
        use dp j to represent dp i + 1, j
        """
        dp = nums[:]

        for i in range(size - 2, -1, -1): #left item, till the second to last
            for j in range(i + 1, size): #right item, from left + 1, till the last
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[-1] > = 0

# https://leetcode.com/problems/unique-paths/
# Q3 62. Unique Paths

class Solution:
    def uniquePaths_math(self, m: int, n: int) -> int:
        def factorial(c: int, a: int):
            #choose a out of c
            res = c
            cnt = 1
            while cnt < a:
                res = res * (c - cnt)
                cnt += 1
            return res

        if m == 1 or n == 1:
            return 1
        return int(factorial(m + n - 2, n - 1)/factorial(n - 1, n - 1))

    def uniquePaths_dp(self, m: int, n: int) -> int:
        """
        dp state
        i, j represent the ith row and jth col
        transition
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        start from top left
        """
        dp = [[1 for i in range(n + 1)] for j in range(m + 1)]
        dp[0] = [0] * n
        for j in range(1, m + 1):
            dp[j][0] = 0
        dp[0][0] = 1
        for i in range(2, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]



# https://leetcode.com/problems/russian-doll-envelopes/
# Q4 354. Russian Doll Envelopes

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def ldd(nums):
            holder = []
            for i in range(len(nums)):
                idx = bisect_left(holder, nums[i])
                if idx == len(holder):
                    holder.append(nums[i])
                else:holder[idx] = nums[i]
            return len(holder)

        return ldd([x[1] for x in envelopes])

# https://leetcode.com/problems/super-egg-drop/description/
# Q5 887. Super Egg Drop

class Solution:
    def superEggDrop_rec(self, k: int, n: int) -> int:
        def dp(k, n):
            if n == 0:
                return 0
            if k == 1:
                return n
            lo, hi = 1, n

            while lo + 1 < hi:
                x = lo + (hi - lo)//2
                t1 = dp(k - 1, x - 1)
                t2 = dp(k, n - x)

                if t1 < t2:
                    lo = x
                elif t1 > t2:
                    hi = x
                else:
                    lo = hi = x

            return 1 + min(max(dp(k - 1, x - 1), dp(k, n - x))for x in (lo, hi))

        return dp(k, n)

    def superEggDrop(self, k: int, n: int) -> int:

        dp = range(n + 1)

        for j in range(2, k + 1):
            dp2 = [0]
            x = 1
            for m in range(1, n + 1):
                while x < m and max(dp[x - 1], dp2[m - x]) > max(dp[x], dp2[m - x - 1]):
                    x += 1
                dp2.append(1 + max(dp[x - 1], dp2[m - x]))
            dp = dp2
        return dp[-1]

# https://leetcode.com/problems/distinct-subsequences/
# Q6 115. Distinct Subsequences
class Solution:
    def numDistinct_rec_memo(self, s: str, t: str) -> int:
        memo = {}

        def uniqueSubSequence(i, j):
            if i == len(s) or j == len(t) or len(s) - i < len(t) - j:
                return int(j == len(t))
            if (i, j) in memo:
                return memo[i, j]
            ans = uniqueSubSequence(i + 1, j)
            if s[i] == t[j]:
                ans += uniqueSubSequence(i + 1, j + 1)
            memo[i, j] = ans
            return ans
        return uniqueSubSequence(0, 0)
    def numDistinct_dp(self, s: str, t: str) -> int:
        dp = [ [0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)] # row number s, col number, t
        # transition matrix, recording by far how many distinct subset met

        # end status
        for x in range(len(s) + 1):
            dp[x][len(t)] = 1

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
        return dp[0][0]
