class LinkedListNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        self.head = LinkedListNode(value, self.head)

    def insert(self, index, value):
        if self.head is None:
            self.head = LinkedListNode(value, None)
        elif index == 0:
            self.add(value)
        else:
            current = self.head
            while current.next is not None and index > 0:
                current = current.next
                index = index - 1

                current.next - LinkedListNode(value, value.next)

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def length(self):
        result = 0
        current = self.head

        while current is not None:
            result += 1
            current = current.next

        return result

    def remove(self):
        if self.head is None:
            return None

        value = self.head.value
        self.head = self.head.next

        return value

    def remove_At(self, index):
        if self.head is None:
            return None

        elif index == 0 or self.head.next is None:
            return self.remove()

        else:
            current = self.head
            while current.next.next is not None and index > 0:
                current = current.next
                index -= 1

                value = current.value
                current.next = current.next.next

                return value



