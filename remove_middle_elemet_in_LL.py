

def deleteMiddle(head):
	slow = head.next # [1,2,3,4] slow and fast start with 2
	fast = head.next
	prev_node = head # it store previous node value starts from 1

	if head.next == None:
	    return None
        
	else :
	    while fast.next and fast.next.next:
	        # print(prev_node.val,slow.val)
	        prev_node = slow
	        slow = slow.next

	        fast = fast.next.next
	    # print(prev_node.val,slow.val)    
	    prev_node.next = slow.next
	    return head


# input : - [1,2,3,4,5]

# ouput : - [1,2,4,5]