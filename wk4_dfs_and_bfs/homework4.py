# https://leetcode.com/problems/word-ladder/
# Q1 127


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # exception
        if endWord not in wordList:
            return 0

        l = len(beginWord)

        possible_list = dict()

        for word in wordList:
            for i in range(l):
                key = word[:i] + "_" + word[i+1:]
                if key not in possible_list:
                    possible_list[key] = []
                possible_list[key].append(word)

        # print(possible_list)
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        while queue:
            # print(queue)
            word, cnt = queue.popleft()
            for i in range(l):
                key = word[:i] + "_" + word[i+1:]
                # print(key)
                if key in possible_list:
                    # print(key, "in possible list")
                    for _ in possible_list[key]:
                        if _ == endWord:
                            return cnt + 1
                        if _ not in visited:
                            # print(_, "not visited")
                            visited.add(_)
                            queue.append((_, cnt + 1))

        return 0

# https://leetcode.com/problems/minimum-knight-moves/
# Q2 1197


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        def dp(x,y):
            if x + y == 0:
                return 0
            elif x + y == 2:
                return 2
            else:
                return min(dp(abs(x-1),abs(y-2)), dp(abs(x-2),abs(y-1))) + 1
        return dp(abs(x),abs(y))





        list_of_dir = [[1, 2],[-1, 2],[1, -2],[-1, -2], [2, 1],[-2, 1],[2, -1],[-2, 1]]

        # move to any direction need // 2 step
        x_prime = (x - 2) % 2
        y_prime = (y - 2) % 2
        pre_step = ( x + y - 4)//3

        steps = []
        def dfs_move_from_to(x_s, y_s, x_d, y_d, prev_step):
            if abs(x_d - x_s) + abs(y_d - y_s) == 3:
                return 1
            elif  abs(x_d - x_s) + abs(y_d - y_s) == 2 :
                return 2
            elif abs(x_d - x_s) + abs(y_d - y_s) == 1:
                return 3
            else:
                    dfs_move_from_to(x_s, y_x, x_d, y_d, prev_step)




        q = collections.deque([(0 , 0, 0)])
        x , y, visited  = max(abs(x), abs(y)), min(abs(x), abs(y)), set([(0,0)])
        while q:
            a, b, step = q.popleft()
            if (a, b) == (x, y): return step
            elif x - a > y - b + 2:
                q.append( a + 2, b + 1, step + 1)
            elif x - a = y - b + 1:
                q.append( a + 2, b + 1, step + 1)
            for dx, dy in [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1)]:
                if (a + dx, b + dy) not in visited and -1 <= a + dx <= x + 2 and -1 <= b + dy <= y + 2 and (a + dx - (b + dy)) > -2 :
                    visited.add((a + dy, b + dy))
                    q.append((a + dx, b + dy, step + 1))
        return -1


# https://leetcode.com/problems/course-schedule/
# Q3 207


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = {_ : [0,[]]  for _ in range(numCourses)}



        for course, prereq in prerequisites:
            in_degree[course][0] += 1
            in_degree[prereq][1].append(course)

        course_available = [ course  for course in in_degree if in_degree[course][0] == 0]

        queue = deque(course_available)
        while queue:
            course_ = queue.popleft()
            numCourses -= 1
            for j in in_degree[course_][1]:
                in_degree[j][0] -= 1
                if in_degree[j][0] == 0:
                    queue.append(j)

        return numCourses == 0

# 1644. Lowest Common Ancestor of a Binary Tree II
# Q4 1644


class Solution: 
    def __init__(self):
        self.answer=None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def bfs(r):
            if not r:
                return 0
            res = bfs(r.left) + bfs(r.right) + (r == p) + (r == q)
            if res >= 2:
                self.answer= r
                return 0
            else:
                return res

        bfs(root)

        # pprint("ans is validation", ans.val)
        return self.answer

# 110. Balanced Binary Tree
# Q5 110


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(node):
            if not node:
                return 0
            else:
                return max(get_depth( node.left), get_depth( node.right)) + 1

        if not root:
            return True
        elif abs(get_depth( root.left) - get_depth( root.right)) > 1:
                return False
        elif not (self.isBalanced( root.left) & self.isBalanced( root.right)) :
                return False
        else:
            return True

# https://leetcode.com/problems/word-search/description/
# Q6 79


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

def dfs(board, word, r, c, visited):
    if not word:
        return True

    if (
        (r, c) in visited
        or r < 0
        or r >= len(board)
        or c < 0
        or c >= len(board[0])
        or board[r][c] != word[0]
    ):
        return False

    return (
        dfs(board, word[1:], r + 1, c, visited + [(r, c)])
        or dfs(board, word[1:], r - 1, c, visited + [(r, c)])
        or dfs(board, word[1:], r, c + 1, visited + [(r, c)])
        or dfs(board, word[1:], r, c - 1, visited + [(r, c)])
    )


class Solution:
    def exist(self, board, word):
        for r, row in enumerate(board):
            for c, l in enumerate(row):
                if dfs(board, word, r, c, []):
                    return True
        return False
