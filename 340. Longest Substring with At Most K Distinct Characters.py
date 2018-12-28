class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = 0
        end = 0
        cache = {}
        maxlen = 0
        while end < len(s):
            cache[s[end]] = end
            if len(cache) > k:
                start = min(cache.values())
                cache.pop(s[start])
                start += 1
            maxlen = max(end - start + 1, maxlen)
            end += 1
        return maxlen




