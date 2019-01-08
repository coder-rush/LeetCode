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

"""
Effiecient Solution
"""
#Generate strobogrammatic numbers from low to the next high, if the diff b/w low and high includes an entire digit increase we will use digit_num
class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        low_len, high_len = len(low), len(high)
        if low_len > high_len: return 0
        def digits_num(digits):
            if digits == 0: return 0
            elif digits == 1: return 3
            elif digits%2 == 0: return 4 * (5**(digits/2 -1))
            else: return 4*3*(5**(digits/2-1))
        def generate_number(length):
            if length == 1: return ["0", "8", "1"]
            elif length == 2: return ["00", "88", "69", "96", "11"]
            else:
                res = []
                for s in generate_number(length - 2):
                    res.append("0" + s + "0")
                    res.append("8" + s + "8")
                    res.append("6" + s + "9")
                    res.append("1" + s + "1")
                    res.append("9" + s + "6")
                return res
        if high_len > low_len:
            hh = len([l for l in generate_number(high_len) if l <= high and  (l[0] != "0" or len(l) == 1)]) + len([l for l in generate_number(low_len) if l >= low and (l[0] != "0" or len(l) == 1)])
        else:
            hh = len([l for l in generate_number(high_len) if low <= l <= high and  (l[0] != "0" or len(l) == 1)])
        for l in range(low_len + 1, high_len):
            hh += digits_num(l)
        return hh

