class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        curr = head
        temp = None
        while curr and curr.next:
            if curr.val == curr.next.val:
                temp = curr.next
                curr.next = curr.next.next
                del temp # optional in Python due to garbage collection 
            else:
                curr = curr.next

        return head
# ans flow let we have linked list 1->1->2->3->3
# curr start from 1 and check next node if same then skip next node by pointing curr.next to curr.next.next
# so first 1 will point to 2 now curr move to 2 and check next node which is 3 not same so curr move to 3
# now curr is 3 and next node is also 3 so skip next node by pointing curr.next to curr.next.next which is null
# finally return head which is 1->2->3 no duplicate nodes