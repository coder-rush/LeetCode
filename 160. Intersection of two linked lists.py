# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""NOT AN O(1) SPACE COMPLEXITY SOLUTION, THAT WOULD REQUIRE A TWO POINTER APPROACH"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeA = headA
        nodeB = headB
        dic = dict()
        while nodeA:
            dic[nodeA] = nodeA.val
            nodeA = nodeA.next
        while nodeB:
            if nodeB in dic:
                return nodeB
            nodeB = nodeB.next
        return None

"""
TWO POINTER APPROACH
"""
"""
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None
"""