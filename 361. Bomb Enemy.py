class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rowHits = 0
        colHits = [0] * len(grid[0])
        m = len(grid)
        n = len(grid[0])
        maxHits = 0
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j - 1] == 'W':
                    rowHits = 0
                    k = j
                    while k < n and grid[i][k] != 'W':
                        if grid[i][k] == 'E':
                            rowHits += 1
                        k += 1
                if i == 0 or grid[i - 1][j] == 'W':
                    k = i
                    colHits[j] = 0
                    while k < m and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            colHits[j] += 1
                        k += 1
                if grid[i][j] == '0':
                    maxHits = max(maxHits, rowHits + colHits[j])
        return maxHits



