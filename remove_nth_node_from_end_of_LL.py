def removeNthFromEnd(head,n):
	def length(head):
	    temp = head
	    
	    count = 0
	    while temp:
	        count +=1
	        temp= temp.next
	    return count
        
	value = length(head)
	lenn = value-n

	if head.next == None: # if only one element in LL
	    return None
	if value == n: # If length of LL == n
	    return head.next
	curr = head
	prev = head
	i =0
	while curr:
	    if i == lenn:
	        break
	    prev = curr
	    curr = curr.next
	    
	    i +=1
	prev.next = curr.next
	return head