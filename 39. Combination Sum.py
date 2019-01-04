class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        answer = []

        def dfs(res, nums, target, start):
            if target < 0:
                return
            if target == 0:
                answer.append(res[:])
                return
            else:
                for i in range(start, len(nums)):
                    dfs(res + [nums[i]], nums, target - nums[i], i)

        dfs([], candidates, target, 0)
        return answer