class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next  # pointer
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
            node.next.prev = node

    def print_backwards(self):
        llstr = ''
        if self.head is None:
            print("empty list")
            return
        itr = self.head
        while itr.next is not None:
            itr = itr.next
        llstr += str(itr.data) + "<---"
        while itr.prev is not None:
            llstr += str(itr.prev.data) + "<---"
            itr = itr.prev

        print(llstr)


        pass
    def print(self):
        if self.head is None:
            print("empty list")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next

        print(llstr)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beggining(3)
    ll.insert_at_beggining(2)
    ll.insert_at_beggining(1)
    ll.print_backwards()
    ll.print()
