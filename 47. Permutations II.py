class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def permute_helper(nums, chosen, result):
            dic = {x: 1 for x in nums}
            if len(nums) == 0:
                result.append(chosen[:])
                return
            for i in range(len(nums)):
                if dic[nums[i]] == 1:
                    permute_helper(nums[:i] + nums[i + 1:], chosen + [nums[i]], result)
                    dic[nums[i]] = 0

        permute_helper(nums, [], result)
        return result
