class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        dic = dict()
        height = []
        for h,i in people:
            if h not in dic:
                dic[h] = [i]
                height.append(h)
            else:
                dic[h].append(i)
        height.sort()
        height = height[::-1]
        answer = []
        for h in height:
            indexes = dic[h]
            for i in sorted(indexes):
                answer.insert(i,[h,i])
        return answer