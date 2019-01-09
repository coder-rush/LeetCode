# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # First Duplicate each node in the list and add it to next of duplicated node
        if not head:
            return head
        node = head
        while (node):
            newNode = RandomListNode(node.label)
            newNode.next = node.next
            node.next = newNode
            node = newNode.next

        # Add Random Pointers for new nodes
        node = head
        while (node):
            newNode = node.next
            if node.random:
                newNode.random = node.random.next
            else:
                newNode.random = None
            node = newNode.next
        # Remove connections with old nodes
        new_head = head.next

        newNode = new_head
        node = head

        while node:
            node.next = node.next.next
            newNode.next = newNode.next.next if newNode.next else None
            node = node.next
            newNode = newNode.next

        return new_head