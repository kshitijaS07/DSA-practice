class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
    #CREATE 3 SEPERATE NODES
node1 = ListNode(10)     # [10 | none]
node2 = ListNode(20)     # [20 | none]
node3 = ListNode(30)     # [30 | none]

# LINK THEMTO EACH OTHER
#node1's "next" pointer points to node 2

node1.next = node2
node2.next = node3
#node3 already points to none

head = node1
current = head
while current is not None:
    print(current.val, end=" ->")
    current = current.next
print("None")    


