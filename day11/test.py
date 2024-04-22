class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1,l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    if l2:
        current.next = l2
    return dummy.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

merged_list = mergeTwoLists(l1,l2)

while merged_list:
    print(merged_list.val,end = " ")
    merged_list = merged_list.next
