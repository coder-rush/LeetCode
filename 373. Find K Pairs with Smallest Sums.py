class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        queue = []

        def push(queue, i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])

        pairs = []
        push(queue, 0, 0)
        while queue and len(pairs) < k:
            s, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(queue, i + 1, j)

            if i == 0:
                push(queue, 0, j + 1)

        return pairs