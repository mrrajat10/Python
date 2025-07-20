class Node:
    def __init__(self, data,):
        self.data = data
        self.next = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3
new_node = Node(40)
head = n1
current = head
while current.next is not None:
    current = current.next
current.next = new_node

current = head
# traversing and printing
while current:
    print(current.data, "-->", end=" ")
    current = current.next
print(None)
