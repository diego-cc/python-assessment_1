from typing import Union

""" Nodes of a tree contain three main elements: references to left and right nodes and a value (data) """


class Node:
    def __init__(self, key: int, value: Union[int, None] = None):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = value

    """ Conveniently determines whether there is a node at the left of this one """

    def is_left_empty(self) -> bool:
        return self.left is None

    """ Conveniently determines whether there is a node at the right of this one """

    def is_right_empty(self) -> bool:
        return self.right is None

    def set_key(self, new_key):
        self.key = new_key

    def set_value(self, new_value):
        self.value = new_value

    def __eq__(self, other) -> bool:
        return self.key == other.key

    def __str__(self) -> str:
        return f'Node key: {self.key}\nNode value: {self.value}'
