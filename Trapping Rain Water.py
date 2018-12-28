class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left = [height[i - 1] for i in range(0, len(height))]
        left[0] = 0
        right = [height[i + 1] for i in range(0, len(height) - 1)]
        right.append(0)

        for i in range(1, len(height)):
            left[i] = max(height[:i])

        for i in range(1, len(height) - 1):
            right[i] = max(height[i + 1:])

        area = 0
        for i in range(len(height)):
            a = min(left[i], right[i]) - height[i]
            if a > 0:
                area += a
        return area