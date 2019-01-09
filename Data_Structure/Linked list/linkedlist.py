class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        if self.next is None:
            return str(self.value)
        else:
            # return "{0}->{1}".format(self.value, self.next)
            return f"{self.value}->{self.next}"


class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def __str__(self):
        if self.head is None:
            return "<<E>>"
        else:
            return str(self.head)

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, value):
        new_node = Node(value)
        curr_node = self.head
        try:
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node
        except AttributeError:
            self.head = new_node

    def remove_first(self):
        if self.head is None:
            pass
        else:
            val = self.head.value
            self.head = self.head.next
            return val

    def remove_last(self):
        if self.head is None or self.head.next is None:
            self.head = None
        else:
            curr_node = self.head
            while curr_node.next.next is not None:
                curr_node = curr_node.next
            curr_node.next = None

    def clear(self):
        self.head = None

    def find(self, value):
        if self.head is None:
            return None
        else:
            curr_node = self.head
            while curr_node.next is not None and not curr_node.value == value:
                curr_node = curr_node.next
            return curr_node if curr_node.value == value else None


if __name__ == "__main__":
    n1 = Node(None, None)
    n1.value = "A"
    n2 = Node("B")
    n1.next = n2
    n3 = Node("C")
    n2.next = n3
    print(n1)
    l = LinkedList()
    l.head = Node("A")
    l.add_first("B")
    l.add_first("C")
    l.remove_last()
    l.add_last("D")
    l.remove_first()
    l.remove_last()
    l.remove_first()
    print(l)
