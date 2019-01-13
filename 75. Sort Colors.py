class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        Beautiful O(n) solution        """
        i = 0
        j = 0
        k = 0
        for k in range(len(nums)):
            n = nums[k]
            nums[k] = 2
            if n<2:
                nums[j] = 1
                j+=1
            if n==0:
                nums[i] = 0
                i+= 1