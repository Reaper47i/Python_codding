# ways to create a linked list ---->


class llNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        node = llNode(data, None)
        if self.head is None:
            self.head = node
            return

        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = node
                break
            current_node = current_node.next

    def insert_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert(data)

    def display(self):
        if self.head is None:
            print("enter elements")

        current_node = self.head
        while current_node is not None:
            print(str(current_node.data) + '-->', end='')
            current_node = current_node.next
        print("Null")

    def get_len(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def remove_at(self, index):
        if index < 0 or index > self.get_len():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        current_node = self.head
        while current_node:
            if count == index - 1:
                current_node.next = current_node.next.next
                break
            current_node = current_node.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_len():
            raise Exception("Invaid Index")

        if index == 0:
            node = llNode(data, None)
            self.head = node
            return

        count = 0
        current_node = self.head
        while current_node:
            if count == index - 1:
                node = llNode(data, current_node.next)
                current_node.next = node
                break
            current_node = current_node.next
            count += 1


if __name__ == '__main__':
    ll = linked_list()
    ll.insert_list([1, 2, 3, 4, 5, 6, 7])
    ll.insert_at(3, 101)
    ll.display()


'''class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def printLinkedList(head):
    if head is None:
        print("Empty Linked List")

    current_node = head
    while current_node is not None:
        print(str(current_node.data))
        current_node = current_node.next


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
'''
