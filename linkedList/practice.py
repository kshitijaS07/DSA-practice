class ListNode:
    def __intt__(self, val = 0):
        self.val = val
        self.next = None

node1 = ListNode(40)
node2 = ListNode(70)
node3 = ListNode(90)

node1.next = node2
node2.next = node3

head = node1
current = head
while current is not None:
    print(current.val, end="->")
    current = current.next

print("None")    