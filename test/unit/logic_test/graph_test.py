"""
Graph test module.
This module contains tests of graph module
"""

import unittest
from app.logic.graph import Graph
from app.logic.graph_exception import GraphException
from app.logic.node_not_found_exception import NodeNotFoundException
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

    def test_depth_first_search_simple_mode(self):
        #[ARRANGE]
        graph = Graph()
        #[ACT]
        string_result = graph.depth_first_search("A")
        #[ASSERT]
        self.assertEqual('A', string_result)

    def test_depth_first_search_normal_mode_1(self):
        #[ARRANGE]
        graph = Graph()
        graph.add_link("A", "B")
        graph.add_link("B", "C")
        #[ACT]
        string_result = graph.depth_first_search("C")
        #[ASSERT]
        self.assertEqual('A->B->C', string_result)

    def test_depth_first_search_normal_mode_2(self):
        #[ARRANGE]
        graph = Graph()
        graph.add_link("A", "B")
        graph.add_link("B", "C")
        graph.add_link("B", "D")
        graph.add_link("D", "E")
        #[ACT]
        string_result = graph.depth_first_search("E")
        #[ASSERT]
        self.assertEqual('A->B->D->E', string_result)

    def test_depth_first_search_with_exception(self):
        #[ARRANGE]
        graph = Graph()
        graph.add_link("A", "B")
        #[ACT]-[ASSERT]
        with self.assertRaises(NodeNotFoundException):
            graph.depth_first_search("E")
