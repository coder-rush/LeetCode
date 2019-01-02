class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = list()

        def permute_helper(nums, chosen):
            if len(nums) == 0:
                k = chosen[:]
                answer.append(k)
            else:
                for index in range(len(nums)):
                    n = nums.pop(index)
                    chosen.append(n)

                    permute_helper(nums, chosen)

                    nums.insert(index, n)
                    chosen.remove(n)

        permute_helper(nums, [])
        return answer