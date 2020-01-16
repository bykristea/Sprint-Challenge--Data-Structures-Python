from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # checking to see if at capacity
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)  # adding item to tail
            self.current = self.storage.head  # setting current to the head item
        # if at capacity delete the head item and remove from storage. add new item to back/tail
        elif self.storage.length == self.capacity:
            delete = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if delete == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head  # starts at the front/head of storage

        while current is not None:  # loops until end while value is not none
            list_buffer_contents.append(current.value)
            current = current.next  # move on to next item, keep going in the loop
            # add to array

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
