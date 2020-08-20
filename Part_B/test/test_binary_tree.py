import unittest
from binary_tree import BinaryTree
from node import Node


class TestBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        # initialise binary tree with "2" as root node before each test
        self.tree = BinaryTree(Node(2))

    def test_add_node_3_right_of_root(self):
        self.tree.add(1)
        added_3 = self.tree.add(3, 8)

        self.assertTrue(added_3)
        self.assertIsNotNone(self.tree.find(3))
        self.assertEqual(self.tree.root.right, self.tree.find(3))
        self.assertEqual(self.tree.find(3).value, 8)

    def test_add_node_1_left_of_root(self):
        self.tree.add(3)
        added_1 = self.tree.add(1)

        self.assertTrue(added_1)
        self.assertIsNotNone(self.tree.find(1))
        self.assertEqual(self.tree.root.left, self.tree.find(1))

    def test_delete_node_5_rearranges_tree(self):
        self.tree.add(1)
        self.tree.add(5)
        self.tree.add(-5)
        self.tree.add(10)
        self.tree.add(8)
        self.tree.add(6)

        deleted_5 = self.tree.delete(5)

        self.assertTrue(deleted_5)
        self.assertIsNone(self.tree.find(5))
        self.assertEqual(self.tree.root.right, self.tree.find(10))
        self.assertEqual(self.tree.find(10).left, self.tree.find(8))
        self.assertEqual(self.tree.find(8).left, self.tree.find(6))

    def test_traverse_pre_order(self):
        self.tree.add(1)
        self.tree.add(5)
        self.tree.add(-5)
        self.tree.add(10)
        self.tree.add(8)
        self.tree.add(6)

        expected = [2, 1, -5, 5, 10, 8, 6]
        actual = self.tree.traverse_pre_order(self.tree.root)

        self.assertEqual(expected, actual)

    def test_traverse_in_order(self):
        self.tree.add(1)
        self.tree.add(5)
        self.tree.add(-5)
        self.tree.add(10)
        self.tree.add(8)
        self.tree.add(6)

        expected = [-5, 1, 2, 5, 6, 8, 10]
        actual = self.tree.traverse_in_order(self.tree.root)

        self.assertEqual(expected, actual)

    def test_traverse_post_order(self):
        self.tree.add(1)
        self.tree.add(5)
        self.tree.add(-5)
        self.tree.add(10)
        self.tree.add(8)
        self.tree.add(6)

        expected = [-5, 1, 6, 8, 10, 5, 2]
        actual = self.tree.traverse_post_order(self.tree.root)

        self.assertEqual(expected, actual)


