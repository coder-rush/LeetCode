class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        second_last = nums[0]
        last = max(nums[0], nums[1])
        profit = max(last, second_last)

        for current in nums[2:]:
            profit = max(last, second_last + current)
            second_last = last
            last = profit

        return profit