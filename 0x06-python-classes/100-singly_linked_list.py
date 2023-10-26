#!/usr/bin/python3
"""class for linked list"""


class Node:
    """defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Instantiation:
        data: data of new node
        next_node: next node to the current node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get the data"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        """next node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    class SinglyLinkedList:
        """Singly Linked List"""

        def __init__(self):
            """Simple instantiation"""
            self.__head = None

        def sorted_insert(self, value):
            """ insert new node"""

            new = Node(value)
            if self.__head == None:
                new.next_node = None
                self.__head = new
            elif self.__head.data > value:
                new.next_node = self.__head
                self.__head = new
            else:
                tmp = self.__head
                while (tmp.next_node is not None and
                        tmp.next_node.data < value):
                    tmp = tmp.next_node
                new.next_node = tmp.next_node
                tmp.next_node = new

            def __str__(self):
                """represent linked list"""
                values = []
                tmp = self.__head
                while tmp is not None:
                    values.append(str(tmp.data))
                    tmp = tmp.next_node
                return '\n'.join(values)
