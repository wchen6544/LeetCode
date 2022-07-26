class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(cur, prev):
            if cur is None:
                return prev
            else:
                next = cur.next
                cur.next = prev
                return reverse(next, cur)

        return reverse(head, None)

    '''
    
    - Example Linked List :  1 => 2

    Flow
                  cur     prev
        reverse( 1 => 2 , None )

            next = 2
            cur.next = None
            cur = [ 1 => None ]

            reverse ( 2, 1 => None )

                next = None
                cur.next = [ 2 => 1 => None]

                reverse (None, 2 => 1 => None)

                return [ 2 => 1 => None] b/c cur = None

        - answer = [ 2 => 1 ] get rid of last None b/c it doesn't exist


    '''


    def deleteNode(self, node):
        
        cur = node.next
        node.val = cur.val
        node.next = node.next.next

    '''

    - node = the thing you want to delete
    - set node value to equal the next node value
    - set node next to equal node next stuff

    '''


    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = head
        p2 = head
        
        while p2 and p2.next:
            
            
            p2 = p2.next.next
            p1 = p1.next
            
        return p1
    
    '''
    
    - 2 pointer question
    - first pointer moves 1 per loop
    - second pointer moves 2 per loop
    - while loop checks for both 
    ( if second pointer exist ) and ( if second pointer next exist)


    '''


    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        p1 = headA
        p2 = headB
        
        while p1 != p2:
            
            p1 = p1.next if p1.next else headB
            p2 = p2.next if p2.next else headA
        
        return p1
    
    '''
    
    - not looking for when the VALUES of headA and headB are equal, 
    actually looking for when headA node is equal to headB node.
    
    - while loop, keep looping if they are not equal
    
    - keep moving the 2 pointers next, if there is no more next, set the pointer
    to the other pointers beginning. Example: p1 => headB, p2 => headA

    '''