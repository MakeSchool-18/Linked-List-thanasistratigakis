#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        if self.head == self.tail:
            return 1
        finished = False
        count = 0
        current_node = self.head
        while not finished:
            if current_node is not self.tail:
                count += 1
                current_node = current_node.next
            else:
                finished = True
        return count
        pass

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # append given item
        new_node = Node(item)
        old_tail = Node(self.tail)
        old_tail.next = new_node
        self.tail = new_node
        pass

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # prepend given item
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        pass

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # find given item and delete if found
        try:
            before_node = findNode(lambda item: item.next is item)
            after_node = item.next
            before_node.next = after_node
            pass
        except Exception as e:
            raise ValueError("Item doesnt exist in linked list")
        pass

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # find item where quality(item) is True
        finished = False
        current_node = self.head
        while not finished:
            if current_node is not self.tail:
                if quality(current_node):
                    return current_node.data
                current_node = current_node.next
            else:
                finished = True
        return None

        pass

    def findNode(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # find item where quality(item) is True
        finished = False
        current_node = self.head
        while not finished:
            if current_node is not self.tail:
                if quality(current_node):
                    return current_node
                current_node = current_node.next
            else:
                finished = True
        return None

def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()
