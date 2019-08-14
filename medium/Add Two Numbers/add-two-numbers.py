# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        headNode = currNode = ListNode(0)
        carry = 0
        
        while(l1 or l2 or carry):
            currSum = carry
            if(l1):
                currSum += l1.val
                l1 = l1.next
            if(l2):
                currSum += l2.val
                l2 = l2.next
            currNode.next = ListNode(currSum % 10)
            carry = currSum // 10
            currNode = currNode.next
        return headNode.next
