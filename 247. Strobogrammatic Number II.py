class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = self.helper(n, n)
        return answer

    def helper(self, n, m):
        if n == 0:
            return [""]
        elif n == 1:
            return ["0", "8", "1"]

        l = self.helper(n - 2, m)
        result = []
        for val in l:
            if n != m:
                result.append("0" + val + "0")
            result.append("1" + val + "1")
            result.append("6" + val + "9")
            result.append("8" + val + "8")
            result.append("9" + val + "6")
        return result


