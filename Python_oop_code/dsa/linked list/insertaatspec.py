class Node:
    def __init__(self, data,):
        self.data = data
        self.next = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(33)

n1.next = n2
n2.next = n3
new_node = Node(60)

head = n1
current = head
while current is not None and current.data != 20:
    current = current.next
new_node.next = current.next
current.next = new_node

current = head
while current:
    print(current.data, "-->", end=" ")
    current = current.next
print(None)