class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = []
        m = len(board)
        n = len(board[0])
        if m == 1 and n == 1:
            return board[0][0] == word
        if len(word) == 1:
            ch = word[0]
            return any(ch in subl for subl in board)

        def dfs(i, j, char, string):
            if len(string) == 0:
                return True

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for d in directions:
                incx, incy = d
                nexti = i + incx
                nextj = j + incy

                if nexti < m and nexti >= 0 and nextj < n and nextj >= 0 and char == board[nexti][nextj] and (
                nexti, nextj) not in visited:

                    if len(string) < 2:
                        return True
                    nextchar = string[1]
                    visited.append((nexti, nextj))
                    val = dfs(nexti, nextj, nextchar, string[1:])
                    if val:
                        return True

            visited.remove((i, j))
            return False

        x = board[0][0]
        y = x[0]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = []
                    visited.append((i, j))
                    ret = dfs(i, j, word[1], word[1:])
                    if ret == True:
                        return True
        return False




