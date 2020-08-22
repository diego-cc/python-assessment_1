from binary_tree import BinaryTree
from node import Node

if __name__ == "__main__":
    """ Initialise tree with root node value = 2 """
    tree = BinaryTree(Node(2))

    tree.add(5)
    tree.add(3)
    tree.add(1)
    tree.add(8)
    tree.add(6)
    tree.add(10)
    tree.add(7)
    tree.add(15)
    tree.add(9)

    print(f'In-order traversal: {tree.traverse_in_order(tree.root)}')
    print(f'Pre-order traversal: {tree.traverse_pre_order(tree.root)}')
    print(f'Post-order traversal: {tree.traverse_post_order(tree.root)}')

    print()
    print(f'Deleted 5: {tree.delete(5)}')
    print(f'Deleted 1: {tree.delete(1)}')
    print()

    print(f'In-order traversal: {tree.traverse_in_order(tree.root)}')
    print(f'Pre-order traversal: {tree.traverse_pre_order(tree.root)}')
    print(f'Post-order traversal: {tree.traverse_post_order(tree.root)}')

    """ Replace 7 with another value and see the output """
    print(f'Search for 7: {tree.find(7)}')
    print(f'Search for 10: {tree.find(10)}')
