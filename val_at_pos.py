class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def list(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def display(self):
        if self.head is None:
            raise Exception('##<invalid>## check list')

        cur = self.head
        while cur:
            print('Head -->', end='')
            print(f'{cur.data} -->', end='')
            print('Tail')

    def find_val(self, pos):
        cur = self.head
        len_list = 0
        while cur:
            len_list += 1
            cur = cur.next

        position = len_list - pos - 1

        if position == 0:
            return self.head
        if position == len_list-1:
            return self.tail

        node = self.head
        while node:
            pass


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        ll = linkedlist()
        for _ in range(n):
            ll.list(input())
        p = int(input())

        ll.display()
        print('\n')
