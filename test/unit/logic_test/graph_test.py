"""
Graph test module.
This module contains tests of graph module
"""

import unittest
from app.logic.graph import Graph
from app.logic.graph_exception import GraphException
from app.logic.node import Node


class TestGraph(unittest.TestCase):
    def test_init_graph(self):
        #[ARRANGE]-[ACT]
        graph = Graph()
        #[ASSERT]
        self.assertIsNotNone(graph.root) 
        self.assertEqual("A", graph.root.id)
        
    def test_add_link_method(self):
        #[ARRANGE]
        graph = Graph()
        parent_id = "A"
        child_id = "B"
        #[ACT] 
        graph.add_link(parent_id, child_id)
        #[ASSERT]
        self.assertEqual(1, len(graph.root.children))
        self.assertEqual(child_id, graph.root.children[0].id)
        self.assertEqual("A", graph.root.children[0].parents[0].id)

    def test_add_link_another_variant(self):
        #[ARRANGE]
        graph = Graph()
        graph.root.add_child(Node("B"))
        graph.root.children[0].add_parent(graph.root)
        graph.root.children[0].add_child(Node("C"))
        graph.root.children[0].children[0].add_parent(
                graph.root.children[0])
        #[ACT]
        graph.add_link("B", "C")
        #[ASSERT]
        self.assertEqual(1, len(graph.root.children))
        self.assertEqual(1, len(graph.root.children[0].children))
        self.assertEqual(1, len(graph.root.children[0].parents))
        self.assertEqual(1, len(graph.root.children[0].children[0].parents))
        self.assertEqual("B", graph.root.children[0].id)
        self.assertEqual("C", graph.root.children[0].children[0].id)

    def test_add_link_another_variant_2(self):
        #[ARRANGE]
        graph = Graph()
        graph.root.add_child(Node("B"))
        graph.root.children[0].add_parent(graph.root)
        #[ACT]
        graph.add_link("B", "C")
        #[ASSERT]
        self.assertEqual(1, len(graph.root.children))
        self.assertEqual(1, len(graph.root.children[0].children))
        self.assertEqual(1, len(graph.root.children[0].parents))
        self.assertEqual(1, len(graph.root.children[0].children[0].parents))
        self.assertEqual("B", graph.root.children[0].id)
        self.assertEqual("C", graph.root.children[0].children[0].id)


    def test_add_link_with_exception(self):
        #[ARRANGE]
        graph = Graph()
        parent_id = "B"
        child_id = "C"
        #[ACT]-[ASSERT]
        with self.assertRaises(GraphException):
            graph.add_link(parent_id, child_id)
