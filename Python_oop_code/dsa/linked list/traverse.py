class Node:
    def __init__(self, data,):
        self.data = data
        self.next = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(33)

n1.next = n2
n2.next = n3
head = n1
current = head
while current:
    print(current.data, "-->", end=" ")
    current = current.next
print(None)


