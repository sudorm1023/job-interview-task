#!/usr/bin/env python3

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        def value(i, j):
            return sum(map(int, list(str(i) + str(j))))

        def dfs (i, j, k):
            if not 0<=i<m or not 0<=j<n or visited[i][j] or value(i, j)>k:
                return
            
            visited[i][j] = 1
            dfs(i, j+1, k)
            dfs(i, j-1, k)
            dfs(i+1, j, k)
            dfs(i-1, j, k)            

        visited = [[0] * n for _ in range(m)]
        dfs(0, 0, k)
        return sum([a.count(1) for a in visited])