class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Bucket
        bucket = collections.defaultdict(list)
        freq_map = collections.Counter(nums)

        for num, freq in freq_map.items():
            bucket[freq].append(num)

        result = []
        for i in range(len(nums), 0, -1):
            if i in bucket:
                result.extend(bucket[i])
                k -= len(bucket[i])
                if k == 0:
                    return result