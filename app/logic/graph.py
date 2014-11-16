"""
Graph module
This module contains graph implementation
"""


from app.logic.node import Node
from app.logic.graph_exception import GraphException


class Graph:
    def __init__(self):
        self.root = Node("A")

    def add_link(self, parent_id, child_id):
        parent_node = self.root.find_node(parent_id)
        child_node = self.root.find_node(child_id)
        if parent_node == None:
            raise GraphException("No parents with value {}".format(parent_id))
        else:
            child_node = Node(child_id) if child_node == None else child_node
            child_node.add_parent(parent_node) 
            parent_node.add_child(child_node)
