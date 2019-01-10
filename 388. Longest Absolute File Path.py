class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # Split Each Line
        lines = input.split("\n")
        maxlen = 0
        dic = {}
        for l in lines:
            tabs = l.count('\t')
            dic[tabs] = len(l.strip('\t'))
            s = 0
            if '.' in l:
                for i in range(0, tabs + 1):
                    s += dic[i]
                maxlen = max(maxlen, s + tabs)

        return maxlen



