class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = 0
        start = 0
        end = 0
        zeroCount = 0
        k = 1
        for i in range(len(nums)):

            if nums[end] == 0:
                zeroCount += 1
            while zeroCount > k:
                if nums[start] == 0:
                    zeroCount -= 1
                start += 1
            maxlen = max(maxlen, end - start + 1)
            end += 1

        return maxlen