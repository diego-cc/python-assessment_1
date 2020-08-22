from typing import Union
from node import Node


class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    """ Add a new node to the tree """

    def add(self, key: int, value: Union[int, None] = None) -> bool:
        if self.root is None:
            self.root = Node(key, value)
            return True

        current_pos = self.root

        while True:
            if key < current_pos.key:
                if current_pos.is_left_empty():
                    new_node = Node(key, value)
                    new_node.parent = current_pos
                    current_pos.left = new_node
                    return True
                else:
                    current_pos = current_pos.left

            elif key > current_pos.key:
                if current_pos.is_right_empty():
                    new_node = Node(key, value)
                    new_node.parent = current_pos
                    current_pos.right = new_node
                    return True
                else:
                    current_pos = current_pos.right
            else:
                # Trying to add a node with an existing key, ignore it
                return False

    """ Search for a node with a given key -> O(logN) """

    def find(self, key: int) -> Union[Node, None]:
        current_pos = self.root

        while current_pos is not None:
            if key < current_pos.key:
                current_pos = current_pos.left
            elif key > current_pos.key:
                current_pos = current_pos.right
            else:
                return current_pos

        return None

    def delete(self, key: int) -> bool:
        if self.root is None:
            return False

        current_pos = self.root

        while True:
            if current_pos is None:
                # node to be deleted not found
                break
            elif current_pos.key < key:
                current_pos = current_pos.right
            elif current_pos.key > key:
                current_pos = current_pos.left
            else:
                # node to be deleted was found
                break

        if current_pos.key == key:
            if current_pos.is_left_empty() and not current_pos.is_right_empty():
                # current_pos.right replaces current_pos
                current_pos.right.parent = current_pos.parent
                if current_pos.parent.right == current_pos:
                    # current_pos is situated at the right-hand side of its parent
                    # link parent to current_pos.right
                    current_pos.parent.right = current_pos.right
                else:
                    # current_pos is situated at the left-hand side of its parent
                    current_pos.parent.left = current_pos.right
            elif not current_pos.is_left_empty() and current_pos.is_right_empty():
                # current_pos.left replaces current_pos
                current_pos.left.parent = current_pos.parent
                current_pos = current_pos.left
            elif current_pos.is_left_empty() and current_pos.is_right_empty():
                # current_pos won't be missed!
                if current_pos.parent.right == current_pos:
                    # current_pos is situated at the right-hand side of its parent
                    # link parent to current_pos.right
                    current_pos.parent.right = None
                else:
                    # current_pos is situated at the left-hand side of its parent
                    current_pos.parent.left = None
            else:
                # did current_pos come from current_pos.parent.left or current_pos.parent.right?
                if current_pos.parent.left == current_pos:
                    # shift current_pos.left to current_pos
                    current_pos.left.parent = current_pos.parent
                    current_pos.right.parent = current_pos.left
                    current_pos.parent.left = current_pos.left

                    current_pos = current_pos.left

                elif current_pos.parent.right == current_pos:
                    # shift current_pos.right to current_pos
                    current_pos.right.parent = current_pos.parent
                    current_pos.left.parent = current_pos.right
                    current_pos.parent.right = current_pos.right

                    current_pos = current_pos.right

            return True

        return False

    """ Traverse the tree in-order (Left -> Root -> Right) """

    def traverse_in_order(self, start_node: Node = None):
        t = []

        if start_node:
            t += self.traverse_in_order(start_node.left)
            t.append(start_node.key)
            t += self.traverse_in_order(start_node.right)

        return t

    """ Traverse the tree pre-order (Root -> Left -> Right) """

    def traverse_pre_order(self, start_node: Node = None):
        t = []

        if start_node:
            t.append(start_node.key)
            t += self.traverse_pre_order(start_node.left)
            t += self.traverse_pre_order(start_node.right)

        return t

    """ Traverse the tree post-order (Left -> Right -> Root) """

    def traverse_post_order(self, start_node: Node = None):
        t = []

        if start_node:
            t += self.traverse_post_order(start_node.left)
            t += self.traverse_post_order(start_node.right)
            t.append(start_node.key)

        return t
