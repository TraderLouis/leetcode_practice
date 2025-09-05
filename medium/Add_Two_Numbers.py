# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def get_new_node(self, node_val, carry_num):
        new_node_val = (node_val + carry_num) % 10 
        carry_num = (node_val + carry_num) // 10
        return carry_num, ListNode(new_node_val)


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        current_1 = l1
        current_2 = l2
        carry_num = 0
        head = None
        current = None

        while current_1 and current_2:
            val1 = current_1.val
            val2 = current_2.val
            node_val = val1 + val2
            carry_num, new_node  = self.get_new_node(node_val, carry_num)

            if head == None:
                head = new_node 
                current = new_node 
            else:
                current.next = new_node 
                current = new_node 

            current_1 = current_1.next
            current_2 = current_2.next

        if current_1 == None:
            while current_2:
                carry_num, new_node  = self.get_new_node(current_2.val, carry_num)
                current.next = new_node 
                current = new_node 
                current_2 = current_2.next

            if carry_num > 0:
                current.next = ListNode(carry_num)

        else:
            while current_1:
                carry_num, new_node  = self.get_new_node(current_1.val, carry_num)
                current.next = new_node 
                current = new_node 
                current_1 = current_1.next

            if carry_num > 0:
                current.next = ListNode(carry_num)

        return head
        






            

