class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        if len(nums) < 3:
            mid = end
        while target != nums[mid]:
            # Left Side Sorted
            if nums[start] < nums[mid] and nums[start] <= target < nums[mid]:
                end = mid

            # Right Side Sorted
            if nums[mid] < nums[end] and nums[mid] <= target <= nums[end]:
                start = mid

            # Left Side Unsorted
            if nums[start] > nums[mid]:
                end = mid

            # Right Side Unsorted
            if nums[mid] > nums[end]:
                start = mid

            pre = mid
            mid = (start + end) // 2
            if pre == mid:
                if nums[end] == target:
                    return end
                if nums[start] == target:
                    return start
                return -1

        return mid
