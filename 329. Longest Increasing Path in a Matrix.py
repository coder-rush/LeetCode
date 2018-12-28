class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        path = list(list())
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        print(m, n)
        cache = [[0 for j in range(n)] for i in range(m)]
        print(cache)

        def dfs(i, j):
            if cache[i][j] != 0:
                return cache[i][j]

            directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
            for d in directions:
                x, y = d
                ip = i + x
                jp = j + y
                if ip >= 0 and jp >= 0 and ip < m and jp < n and matrix[ip][jp] > matrix[i][j]:
                    cache[i][j] = max(cache[i][j], dfs(ip, jp))
            cache[i][j] += 1
            return cache[i][j]

        # Main
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        return ans