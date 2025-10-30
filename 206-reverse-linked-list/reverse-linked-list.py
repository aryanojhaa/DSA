class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        stack=[]
        while(temp!=None):
            stack.append(temp.val)
            temp=temp.next
        temp=head
        while(temp!=None):
            e = stack.pop()
            temp.val = e
            temp=temp.next
        return head








        
                    