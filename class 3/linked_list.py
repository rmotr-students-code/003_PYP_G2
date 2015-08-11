"""
A Linked List (https://en.wikipedia.org/wiki/Linked_list) is a linear data structure. You can think of it as an implementation of a regular Python List.

Using Object Oriented programming, build a simple Linked List that shares the same interface with Python Lists:

    l = LinkedList()

    l.append(2)
    l.count()  # Should return 1

    l + [2, 3]     # Should return [1, 2, 3] but not mutate the original list
    l += [3, 4]   # Should return None and append [3, 4] to the original list

    l.pop(0)       # Should remove and return the first element.

    # Important. This should be True:
    LinkedList([1, 2, 3]) == LinkedList([1, 2, 3])

To ease your task, a LinkedList is constructed using different Nodes. Each node has a reference to other Node, what makes it a recursive class, it'll point to itself.

"""

class Node(object):
    def __init__(self, data):
        self.elem = data
        self.next = None
    def set_next_value(self, next_value):
        self.next = next_value
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.elem == other.elem

class LinkedList(object):
    def __init__(self, data=None):
        self.start = None
        self.size = 0
        if data != None:
            for d in data:
                self.append(d)
    
    def __len__(self):
        return self.size
    
    def __eq__(self,other):
        
        if type(self) != type(other):
            return False
        
        if len(self) != len(other):
            return False

        iterator_1 = self.start
        iterator_2 = other.start
        while iterator_1:
            if iterator_1.elem != iterator_2.elem:
                return False
            iterator_1 = iterator_1.next
            iterator_2 = iterator_2.next
        return True
                
    def append(self, data):
        
        new_node = Node(data)
        iterator = self.start
        
        if not iterator:
            self.start = new_node
        else:
            while iterator.next:
                iterator = iterator.next
            iterator.next = new_node
            
        self.size += 1
        
    def count(self):
        return self.size
        
    def __getitem__(self, index):
        
        if index > self.size - 1:
            raise IndexError
        
        i = 0
        node = self.start
        while True:
            if i == index:
                return node.elem
            node = node.next
            i += 1

        
import unittest

class LinkedListTestCase(unittest.TestCase):

    def test_creation_and_equal(self):
        l1 = LinkedList([1, 2, 3])

        self.assertTrue(l1.start is not None)
        self.assertEqual(l1.start.elem, 1)

        self.assertTrue(l1.start.next is not None)
        self.assertEqual(l1.start.next.elem, 2)

        self.assertTrue(l1.start.next.next is not None)
        self.assertEqual(l1.start.next.next.elem, 3)

    def test_equals(self):
        self.assertEqual(
            LinkedList([1, 2, 3]),
            LinkedList([1, 2, 3]))

        self.assertEqual(
            LinkedList([]),
            LinkedList([]))

        self.assertEqual(
            LinkedList([1]),
            LinkedList([1]))

        self.assertNotEqual(
            LinkedList([1, 2]),
            LinkedList([1, 2, 3]))

        self.assertNotEqual(
            LinkedList([1]),
            LinkedList([]))
            
    def test_count(self):
        self.assertEqual(LinkedList([1, 2, 3]).count(), 3)

    def test_append(self):
        my_list = LinkedList()

        my_list.append(1)
        self.assertEqual(my_list.start.elem, 1)
        self.assertEqual(my_list.start.next, None)

        my_list.append(2)
        self.assertEqual(my_list.start.elem, 1)
        self.assertEqual(my_list.start.next, Node(2))
        self.assertEqual(my_list.start.next.elem, 2)
        self.assertEqual(my_list.start.next.next, None)

        self.assertEqual(my_list.count(), 2)
        
    def test_get_item(self):
        my_list = LinkedList([1, 2, 3, 4])
        self.assertEqual(my_list[0], 1)
        self.assertEqual(my_list[2], 3)
        self.assertEqual(my_list[3], 4)

        with self.assertRaises(IndexError):
            my_list[4]

        
"""



    def test_iterate(self):
        my_list = LinkedList([1, 2, 3, 4])
        count = 0
        for elem in my_list:
            count += 1
        self.assertEqual(count, 4)

    def test_add_list(self):
        my_list = LinkedList([1, 2])
        new_list = my_list + LinkedList([3, 4, 5])
        self.assertNotEqual(id(my_list), id(new_list))
        self.assertEqual(new_list, LinkedList([1, 2, 3, 4, 5]))

    def test_iadd_list(self):
        my_list = LinkedList([1, 2])
        my_list += LinkedList([3, 4, 5])
        self.assertEqual(my_list, LinkedList([1, 2, 3, 4, 5]))

    def test_len(self):
        my_list = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(len(my_list), 5)

    def test_pop(self):
        my_list = LinkedList([1])
        self.assertEqual(my_list.pop(), 1)
        self.assertEqual(my_list.count(), 0)

        my_list = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(my_list.pop(), 5)
        self.assertEqual(my_list.count(), 4)

        my_list = LinkedList([1, 2, 3])
        self.assertEqual(my_list.pop(1), 2)
        self.assertEqual(my_list.count(), 2)
        self.assertEqual(my_list, LinkedList([1, 3]))
"""

if __name__ == '__main__':
    unittest.main()