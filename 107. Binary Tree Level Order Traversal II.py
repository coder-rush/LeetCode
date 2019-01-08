# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        ans = []
        while len(level) != 0:
            #The trick is here, instead of adding the nodes to the end of the answer add it to the start of answer
            # so that the elements are added to the start of the list
            ans.insert(0, [node.val for node in level])
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = [node for node in next_level if node]

        return ans