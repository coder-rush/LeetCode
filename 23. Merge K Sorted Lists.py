# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Priority Queue
        pqueue = []
        # Add Roots of each node
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pqueue, [lists[i].val, lists[i]])

        if not pqueue:
            return []

        # Initialize Root Node
        _, root = heapq.heappop(pqueue)

        # Initialize Previous
        if root.next:
            heapq.heappush(pqueue, [root.next.val, root.next])
        prev = root

        # Pop from prioirity queue and push it's neighbours
        while pqueue:
            val, node = heapq.heappop(pqueue)
            if node.next:
                heapq.heappush(pqueue, [node.next.val, node.next])
            prev.next = node
            prev = node

        return root