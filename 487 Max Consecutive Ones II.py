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
        #Works for different k
        for i in range(len(nums)):
            if nums[end] == 0:
                zeroCount += 1
            while zeroCount > k:
                #If count of zero is greater than k, bring start to the point where this happened.
                if nums[start] == 0:
                    zeroCount -= 1
                start += 1
            maxlen = max(maxlen, end - start + 1)
            end += 1

        return maxlen