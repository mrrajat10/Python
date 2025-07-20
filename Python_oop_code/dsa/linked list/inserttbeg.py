class Node:
    def __init__(self, data,):
        self.data = data
        self.next = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(33)

n1.next = n2
n2.next = n3
# insert at beginning
head = n1
new_node = Node(44)
new_node.next = head
head = new_node

current = head
while current:
    print(current.data, "-->", end=" ")
    current = current.next
print(None)


# with functions
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def insert_at_beginning(head, data):
#     new_node = Node(data)
#     new_node.next = head
#     return new_node

# def print_list(head):
#     current = head
#     while current:
#         print(current.data, "-->", end=" ")
#         current = current.next
#     print("None")

# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(33)

# n1.next = n2
# n2.next = n3

# head = n1
# head = insert_at_beginning(head, 44)
# print_list(head)
