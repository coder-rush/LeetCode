class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        temp = []
        l = len(low)
        h = len(high)

        for c in range(l, h + 1):
            temp.extend(self.helper(c, c))
        count = 0
        for num in temp:
            if int(low) <= int(num) <= int(high):
                count += 1
        return count

    def helper(self, n, m):
        if n == 0:
            return [""]
        elif n == 1:
            return ['0', '1', '8']

        l = self.helper(n - 2, m)
        res = []
        for val in l:
            if n != m:
                res.append('0' + val + '0')
            res.append('1' + val + '1')
            res.append('6' + val + '9')
            res.append('8' + val + '8')
            res.append('9' + val + '6')

        return res

