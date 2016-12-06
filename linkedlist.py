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

    # Theta(n)
    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        go = True
        current = None
        if self.head is None:
            return []
        else:
            current = self.head
        while go:
            result.append(current.data)
            if current is self.tail or current.next is None:
                go = False
            else:
                current = current.next
        return result

    # Theta(1)
    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None


    # O(n)
    # Omega(1)
    # Theta(n)
    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        if self.head == self.tail and self.head is not None:
            return 1
        elif self.is_empty():
            return 0
        finished = False
        count = 1
        current_node = self.head
        while not finished:
            if current_node is not self.tail and current_node.next is not None:
                count += 1
                current_node = current_node.next
            else:
                finished = True
        return count
        pass

    # O(1)
    # Omega(1)
    # Theta(1)
    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # append given item
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            old_tail = self.tail
            old_tail.next = new_node
            self.tail = new_node
        pass

    # O(1)
    # Omega(1)
    # Theta(1)
    def prepend(self, item):
        # prepend given item
        """Insert the given item at the head of this linked list"""
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        pass

    # O(n)
    # Omega(1)
    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # find given item and delete if found
        before_node = self.findPreviousNode(lambda item: item is item)
        node_to_delete = self.findNode(lambda item: item is item)

        # Node is found
        if node_to_delete is not None:

            # Node is head
            if self.head is node_to_delete:
                print(self.head.data)
                print(self.tail.data)
                print(node_to_delete)
                self.head = node_to_delete.next
                print("Node is head")
                return
                pass
            print("passed head check")
            # Node is tail
            if self.tail is node_to_delete:
                # if before_node is not self.head:
                print(self.head.data)
                print(self.tail.data)
                self.tail == before_node
                before_node.next = None
                print("Node is tail")

                return
                pass

            # Node is not head or tail
            after_node = node_to_delete.next
            before_node.next = after_node
            pass
        else:
            print("item doesnt exist in list")
            # raise ValueError("Item doesnt exist in linked list")
        pass

    # O()
    # Omega(1)
    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # find item where quality(item) is True
        myList = self.as_list()
        for item in myList:
            if quality(item):
                return item
                pass
        return None
        pass

    def findNode(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # find item where quality(item) is True

        finished = False
        current_node = self.head

        while not finished:

            if quality(current_node):
                print("return")
                return current_node
            if current_node.next is not None:
                print("went to next")
                current_node = current_node.next
            else:
                finished = True
        return None

    def findPreviousNode(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # find item where quality(item) is True
        finished = False
        current_node = self.head
        previous_node = self.head
        while not finished:
            if quality(current_node):
                return previous_node
            if current_node is not self.tail:
                previous_node = current_node
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
