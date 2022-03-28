class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next  # pointer


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, list_data):
        self.head = None
        for data in list_data:
            self.insert_at_end(data)

    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, position):
        if position < 0 or position > self.get_lenght():
            raise Exception("invalid index")
        if position == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:

            if count == position - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_at(self, position, data):
        if position < 0 or position > self.get_lenght():
            raise Exception("invalid index")
        if position == 0:
            self.insert_at_beggining(data)
        count = 0
        itr = self.head
        while itr:

            if count == position - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next

                break
            itr = itr.next

    # 1 -> 2 -> 3
    def invert_linked_list(self):
        curr = self.head
        prev = None
        next_num = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = next_num
            if next_num:
                next_num = next_num.next

        self.head = prev







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
    ll.insert_values([1, 2, 3, 4])
    # ll.insert_at(1, 5)
    # ll.insert_after_value(5, 1)
    # ll.remove_by_value(5)
    ll.invert_linked_list()

    ll.print()
