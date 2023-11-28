#!/usr/bin/python3
"""
This module defines a Node class and a SinglyLinkedList class.

The Node class represents a node of a singly linked list.
It has private instance attributes, data and next_node, and
both have getter and setter methods

The SinglyLinkedList class has a private instance attribute,
head, and a public instance method sorted_insert that inserts
a new Node into the correct sorted position in the list
(increasing order)
"""


class Node:
    """
    The class represents a node of a singly linked list.

    It has private instance attributes, data and next_node, and
    both have getter and setter methods
    """
    def __init__(self, data, next_node=None):
        """
        Instantiates a class

        Args:
            data (int): Data
            next_node (Node): Link to the next node (default is None)
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves data attribute

        Returns:
            int: The data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data attribute

        Args:
            value (int): The new data value

        Raises:
            TypeError: If value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves next_node attribute

        Returns: The next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next_node attribute

        Args:
            value (int): The new next_node value

        Raises:
            TypeError: If value is not a Node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

        def __str__(self):
            """Returns a string representation of the list"""
            sll = ""
            current = self.__head
            while current is not None:
                sll1 += str(current.data) + "\n"
                current = current.next_node
            return sll1.strip()

        def __repr__(self):
            """Returns a string representation of the object."""
            return str(self)


class SinglyLinkedList:
    """
    This class defines a singly linked list

    It has a private instance attribute, head, and a public
    instance method, sorted_insert, that inserts a new Node
    into the correct sorted position in the list
    (increasing order)
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position
        in the list (increasing order).

        Args:
            value (int): The value to be inserted.

        Raises:
            TypeError: If value is not an integer.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

        def __str__(self):
            """Returns a string representation of the list"""
            sll = ""
            current = self.__head
            while current is not None:
                sll1 += str(current.data) + "\n"
                current = current.next_node
            return sll1.strip()

        def __repr__(self):
            """Returns a string representation of the object."""
            return str(self)
