class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {}
        start = 0
        end = 0
        maxlen = 0
        while (end < len(s)):
            slen = 0
            cache[s[end]] = end
            if len(cache) > 2:
                start = min(cache.values())
                cache.pop(s[start])
                start += 1
            slen = end - start + 1
            maxlen = max(slen, maxlen)
            end += 1
        return maxlen
