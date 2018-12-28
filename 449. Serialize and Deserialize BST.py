# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        serial = []
        if not root:
            return []

        def preorder(node):
            if node:
                serial.append(node.val)
                if node.left:
                    preorder(node.left)
                if node.right:
                    preorder(node.right)

        preorder(root)
        serial = map(str, serial)
        serial = ' '.join(serial)
        return serial

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return []
        data = data.split(" ")
        serial = [int(x) for x in data]
        queue = collections.deque(serial)
        print(queue)

        def buildTree(minVal, maxVal):
            if queue and minVal < queue[0] < maxVal:
                val = queue.popleft()
                node = TreeNode(val)
                node.left = buildTree(minVal, val)
                node.right = buildTree(val, maxVal)
                return node

        # return buildTree(float('-infinity'), float('infinity'))
        root = buildTree(float('-inf'), float('inf'))

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))