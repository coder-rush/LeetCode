# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#Ae halo
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        level = [root]
        #Initialize level 1 with root
        while level:
            #Append all the nodes at this level to the answer
            ans.append([node.val for node in level])
            next_level = []
            #Calculate nodes at next level, i.e for each node at this level at add next level
            for node in level:
                next_level.append(node.left)
                next_level.append(node.right)
            level = []
            for node in next_level:
                if node:
                    level.append(node)
        return ans