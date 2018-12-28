# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        c = 0
        level = [root]
        res = []
        flag = 1
        while (level):
            c += 1
            flag *= -1
            res.append([node.val for node in level[::flag]])
            next_level = []

            for node in level:
                next_level.append(node.right)
                next_level.append(node.left)
            level = [node for node in next_level if node]

        return res

