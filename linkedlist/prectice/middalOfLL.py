class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
# ans flow let we have linked list 1->2->3->4->5->6->7->8
# fast go 1-->3-->5-->7 after this loop will break because fast.next will be null
# slow go 1-->2-->3-->4 loop break here and return slow which is 4 so middle node is 4

