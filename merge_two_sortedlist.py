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
            raise Exception('***<invalid>*** ---> check list')
        cur = self.head
        print('Head -->', end='')
        while cur:
            print(f'{cur.data} -->', end='')
            cur = cur.next
        print('Tail')


def merge_lists(head1, head2):
    h1 = head1
    h2 = head2
    s = None
    new_ll = linkedlist()

    if not h1 and h2:
        return None
    if not h1:
        return h2
    if not h2:
        return h1
    if h1.data <= h2.data:
        s = h1
        h1 = s.next
    else:
        s = h2
        h2 = s.next
    new_ll.head = s

    while h1 and h2:
        if h1.data <= h2.data:
            s.next = h1
            s = h1
            h1 = s.next
        else:
            s.next = h2
            s = h2
            h2 = s.next
    s.next = h2 if not h1 else h1

    return new_ll


if __name__ == '__main__':
    for _ in range(int(input())):
        n1 = int(input())
        ll1 = linkedlist()
        for _ in range(n1):
            ll1.list(input())

        n2 = int(input())
        ll2 = linkedlist()
        for _ in range(n2):
            ll2.list(input())
    ll1.display()
    print('\n')
    ll2.display()
    print('\n')
    new_list = merge_lists(ll1.head, ll2.head)
    new_list.display()
