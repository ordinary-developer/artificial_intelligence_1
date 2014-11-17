"""
Node test module
This module contains tests for ./app/logic/node.py module
(The path is relative from root directory)
"""


import unittest
from app.logic.node import Node


class TestNode(unittest.TestCase):
    def test_create_node_instance(self):
        #[ARRANGE]-[ACT]
        id = 'A'
        node = Node(id)
        #[assert]
        self.assertIsNotNone(node)
        self.assertIsNotNone(node.id)
        self.assertEqual(id, node.id)
        self.assertIsNotNone(node.parents)
        self.assertIsNotNone(node.children)

    def test_create_two_different_nodes(self):
        #[ARRANGE]-[ACT]
        node1, node2 = Node("A"), Node("B")
        #[assert]
        self.assertFalse(node1 == node2)
        self.assertTrue(node1 != node2)

    def test_create_two_equal_nodes(self):
        #[ARRANGE]-[ACT]
        node1, node2 = Node("A"), Node("A")
        #[assert]
        self.assertTrue(node1 == node2)
        self.assertFalse(node1 != node2)

    def test_add_parent_node(self):
        #[ARRANGE]
        parent_node = Node("A")
        child_node = Node("B")
        #[ACT]
        child_node.add_parent(parent_node)
        #[assert]
        self.assertEqual(1,len(child_node.parents))
        self.assertEqual(parent_node, child_node.parents[0])

    def test_add_parent_nodes_with_different_nodes(self):
        #[ARRANGE]
        parent_node1, parent_node2 = Node("A"), Node("B")
        child_node = Node("C")
        #[ACT]
        child_node.add_parent(parent_node1)
        child_node.add_parent(parent_node2)
        #[ASSERT]
        self.assertEqual(2, len(child_node.parents))
        self.assertEqual(parent_node1, child_node.parents[0])
        self.assertEqual(parent_node2, child_node.parents[1])    

    def test_add_parent_node_with_two_equal_nodes(self):
        #[ARRANGE]
        parent_node1, parent_node2 = Node("A"), Node("A")
        child_node = Node("B")
        #[ACT]
        child_node.add_parent(parent_node1)
        child_node.add_parent(parent_node2)
        #[assert]
        self.assertEqual(1, len(child_node.parents))
        self.assertEqual(parent_node1, child_node.parents[0])
        
    def test_add_child_node(self):
        #[ARRANGE]
        parent_node = Node("A")
        child_node = Node("B")
        #[ACT]
        parent_node.add_child(child_node)
        #[ASSERT]
        self.assertEqual(1, len(parent_node.children))
        self.assertEqual(child_node, parent_node.children[0])

    def test_add_child_node_with_different_nodes(self):
        #[ARRANGE]
        parent_node = Node("A")
        child_node1, child_node2 = Node("B"), Node("C")
        #[ACT]
        parent_node.add_child(child_node1)
        parent_node.add_child(child_node2)
        #[ASSERT]
        self.assertEqual(2, len(parent_node.children))
        self.assertEqual(child_node1, parent_node.children[0])
        self.assertEqual(child_node2, parent_node.children[1])

    def test_add_2_equal_child_nodes(self):
        #[ARRANGE]
        parent_node = Node("A")
        child_node1, child_node2 = Node("B"), Node("B")
        #[ACT]
        parent_node.add_child(child_node1)
        parent_node.add_child(child_node2)
        #[ASSERT]
        self.assertEqual(1, len(parent_node.children))
        self.assertEqual(child_node1, parent_node.children[0])

    def test_find_return_current_node(self):
        #[ARRANGE]
        id = "A"
        node = Node(id)
        #[ACT]
        result_node = node.find_node(id)
        #[ASSERT]
        self.assertIsNotNone(result_node)
        self.assertEqual(id, result_node.id)

    def test_find_return_none_value(self):
        #[ARRANGE]
        node = Node("A")
        #[ACT]-[ASSERT] 
        self.assertIsNone(node.find_node("B"))

    def test_find_return_none_value_another_variant(self):
        #[ARRANGE]
        node = Node("A")
        node.add_parent(Node("B"))
        #[ACT]-[ASSERT]
        self.assertIsNone(node.find_node("C"))

    def test_find_with_nested_nodes(self):
        #[ARRANGE]
        node1 = Node("A")
        node2 = Node("B")
        find_id = "C"
        node3 = Node(find_id)
        node1.add_child(node2)
        node2.add_child(node3)
        #[ACT]
        result = node1.find_node(find_id)
        #[ASSERT]
        self.assertIsNotNone(result)
        self.assertEqual(find_id, result.id)
