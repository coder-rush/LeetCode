class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        serial = ""
        if not root:
            serial += 'None,'
            return serial
        serial += str(root.val) + ','
        serial += self.serialize(root.left)
        serial += self.serialize(root.right)
        return serial

    def deserialize(self, data):
        queue = collections.deque(data.split(","))
        root = self.rec(queue)
        return root

    def rec(self, queue):
        if queue[0] == 'None':
            queue.popleft()
            return None
        root = TreeNode(int(queue.popleft()))
        root.left = self.rec(queue)
        root.right = self.rec(queue)
        return root