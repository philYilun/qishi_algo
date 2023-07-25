# https://leetcode.com/problems/find-if-path-exists-in-graph/
# 1971. Find if Path Exists in Graph

class Solution:


    def validPath(self, n: int, edges , source: int, destination: int) -> bool:
        node = self.initialize(n)
        # 1-2-5-6-7 3-8-9 4
        for (i, j) in edges:
            node = self.union(node, i, j)
        return self.connected(node, source, destination)

    def initialize(self, n):
        return [i for i in range(n)]

    def find(self, node, x):
        if x == node[x]:
            return x
        print("self.root[x]",node[x] , "self.find(self.root[x])",self.find(node, node[x]) )
        node[x] = self.find(node,node[x])
        return node[x]

    def union(self, node, x, y):
        rootX = self.find(node, x)
        rootY = self.find(node, y)
        print("rootX","rootY",rootX,rootY)
        if rootX != rootY:
            node[rootY] = rootX
        return node

    def connected(self,node, x, y):
        return self.find(node, x) == self.find(node, y)


def main():
    s = Solution()
    n = 50
    edges = [[31,5],[10,46],[19,31],[5,1],[31,28],[28,29],[8,26],[13,23],[16,34],[30,1],[16,18],[33,46],[27,35],[2,25],[49,33],[44,19],[22,26],[30,13],[27,12],[8,16],[42,13],[18,3],[21,20],[2,17],[5,48],[41,37],[39,37],[2,11],[20,26],[19,43],[45,7],[0,21],[44,23],[2,39],[27,36],[41,48],[17,42],[40,32],[2,28],[35,38],[3,9],[41,30],[5,11],[24,22],[39,5],[40,31],[18,35],[23,39],[20,24],[45,12]]
    source = 29
    destination = 46
    print(s.validPath(n, edges, source, destination))


if __name__=='__main__':
	main()


# https://leetcode.com/problems/find-the-town-judge/
# 997. Find the Town Judge


class Solution:
    def findJudge(self, n: int, trust) -> int:
        grid = self.initialize(n)
        # grid is a n by n matrix
        # the direction is i to j
        for (i, j) in trust:
            grid[i - 1][j - 1] = 1

        # calculate how many ppl trust person i


        for k in range(n):
            a = sum(i[k] for i in grid) # be trusted
            b = sum(grid[k])# be trust
            # print("k", k + 1, "a", "b" ,a, b)
            # print(grid)
            if (a == n - 1) & (b == 0):
                return k + 1
        return -1

    def initialize(self, n):
        return  [[0 for i in range(n)]  for i in range(n)]



def main():
    s = Solution()
    n =  3
    trust = [[1,3],[2,3],[3,1]]
    print(s.validPath(n, trust))


if __name__=='__main__':
	main()


# https://leetcode.com/problems/shortest-path-with-alternating-colors/
# 1129. Shortest Path with Alternating Colors



class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges , blueEdges) :
        """
        n: number of nodes
        redEdges: directed edge in color red
        blueEdges: directed edge in color blue
        output: a list of length n, the value is the shortest path needed from 0 to the node

        idea breadth first search
        start with record both edge in one dictionary
        start with the initial data point 0: index, 0: needed path, None: color of prev_edge
        note: for each node, always record 2 cases with 2 different previous edge color
        finally take the one matches
        """

        graph = dict()
        for i in range(n):
            if i not in graph:
                graph[i] = []

        for i, j in redEdges:
            graph[i].append((j, "r"))
        for i, j in blueEdges:
            graph[i].append((j, "b"))

        ans = [-1] * n # this is the array for final answeres.

        queue = deque([(0, 0, None)])
        visited = set()
        while queue:
            node, dist, precolor = queue.popleft()
            visited.add((node, precolor ))
            if ans[node] == -1:
                ans[node] = dist
            for next, color in graph[node]:
                if (color != precolor) and ( (next, color) not in visited):
                    queue.append((next, dist + 1, color))

        return ans


def main():
    s = Solution()
    n = 3
    redEdges = [[0,1],[1,2]]
    blueEdges = []

    print(s.shortestAlternatingPaths(n, redEdges, blueEdges))


if __name__=='__main__':
	main()

# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
# 2359. Find Closest Node to Given Two Nodes

class Solution:
    def closestMeetingNode(self, edges, node1: int, node2: int) -> int:
        """
        input
        edges: List[int], index is from, the value is t o
        node 1 and node 2 are 2 index
        output
        return the node that takes least step
        """
        queue1 = deque([node1])
        queue2 = deque([node2])
        visited1 = set()
        visited2 = set()
        res = []

        while queue1 or queue2:
            if queue1:
                node = queue1.popleft()
                visited1.add(node)
                #print("queue1",queue1, "queue2",queue2,"node", node, "visited2", visited2,"visited1", visited1, "self.res", self.res)
                if node in visited2:
                    res.append(node)
                else:
                    if (edges[node] != -1) and (edges[node] not in visited1):
                        queue1.append(edges[node])

            if queue2:
                node = queue2.popleft()
                visited2.add(node)
                #print("queue2",queue2, "queue1",queue1,"node", node, "visited1", visited1,"visited2", visited2, "self.res", self.res)
                if node in visited1:
                    res.append(node)
                else:
                    if  edges[node] != -1  and (edges[node] not in visited2):
                        queue2.append(edges[node])
            if res:
                return min(res)
        return -1


def main():
    s = Solution()
    n = 3
    redEdges = [[0,1],[1,2]]
    blueEdges = []
    print(s.shortestAlternatingPaths(n, redEdges, blueEdges))


if __name__=='__main__':
	main()


# https://leetcode.com/problems/number-of-good-paths/
# 2421. Number of Good Paths

class Solution:
    def numberOfGoodPaths(self, vals , edges ) -> int:
        """
        input
        vals: List[int], index is node, the value is value of the node
        edges: how nodes linked to each other
        output
        return the number of good path
        good path is 1) start and end at the same number 2) all number in the middle is smaller
        note: this result still have TLE, will optimize
        """
        self.res = 0

        # create a dictionary with key as in and a list as out
        dir_map = dict()
        for i in range(len(vals)):
            if i not in dir_map:
                dir_map[i] = []
        for i, j in edges:
            dir_map[i].append(j)
        for j, i in edges:
            dir_map[i].append(j)
        print(dir_map)

        for i in range(len(vals)):
            visited = set()

            self.bfs(i, i, dir_map, vals, visited)

        return (self.res + len(vals))//2



    def bfs(self, init, curr, dir_map, vals, visited = set() ):
        """
        bfs function
        init is where the path started
        curr is where the path currently at

        """

        start_ = vals[init]
        curr_ = vals[curr]


        if curr_ > start_:
            print(" init, curr , visited, start_,curr_ , self.res, exit",  init, curr,    visited, start_,curr_, self.res)
            return
        if curr in visited:
            print(" init, curr , visited, start_,curr_ , self.res, exit",  init, curr,   visited, start_,curr_, self.res)
            return
        visited.add(curr)
        if curr_ == start_:
            self.res += 1
            print(" init, curr , visited, start_,curr_ , self.res",  init, curr,   visited, start_,curr_, self.res)
        for i in dir_map[curr]:
            self.bfs(init, i,  dir_map, vals, visited)

def main():
    s = Solution() 
    vals = [1,3,2,1,3] 
    edges =  [[0,1],[0,2],[2,3],[2,4]]  
    print(s.numberOfGoodPaths( vals, edges))


if __name__=='__main__':
	main()


# https://leetcode.com/problems/number-of-good-paths/
# 2421. Number of Good Paths

class Solution:
    def longestPath(self, parent , s: str) -> int:
        """
        use recursion to reduce repeated calc
        """
        # create a map
        dir_map = dict()
        for i, j in enumerate(parent):
            if (j!= -1) :
                if j not in dir_map: dir_map[j] = []
                dir_map[j].append(i)

        self.max = 1
        # print(dir_map)
        def rec(i):
            if i not in dir_map:
                return 1
            cnt = 1 # base for current best
            for j in dir_map[i]:
                sub_best = rec(j)
                if s[i] != s[j]:
                    self.max = max(self.max,sub_best + cnt)
                    # print(self.max)
                    cnt = max(cnt, sub_best + 1)
                    # print('post cnt', cnt)
            return cnt

        rec(0)
        return self.max


def main():
    s = Solution()
    # edges = [2,2,3, 4,-1]
    # node1 = 0
    # node2 = 3
    parent = [-1,0,0,1,1,2]
   # [1,1,2,2,3]
    s =  "abacbe"
    # [[0,1],[1,2],[2,3],[2,4]]


    print(s.longestPath( parent, s))


if __name__=='__main__':
	main()
