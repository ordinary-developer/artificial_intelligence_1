"""
Graph module
This module contains graph implementation
"""


from app.logic.node import Node
from app.logic.graph_exception import GraphException
from app.logic.node_not_found_exception import NodeNotFoundException


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

    def depth_first_search(self, node_id):
        #[initialize]
        cs = self.root
        sl = [self.root]
        nsl = [self.root]
        dl = []
        #[working]
        while len(nsl) > 0:
            if  cs.id == node_id:
                return self.get_string_representation(sl)
            else:
                if (len(cs.children) != 0):
                    for child in cs.children:
                        nsl.insert(0, child)
                    cs = nsl[0]
                    sl.insert(0, cs)
                else:
                    while len(sl) != 0 and cs == sl[0]:
                        dl.insert(0, cs)
                        sl.pop()
                        nsl.pop()
                        if len(nsl) != 0:
                            cs = nsl[0]
                    sl.insert(0, cs)
        raise NodeNotFoundException("Can't find the node")

    def get_string_representation(self, source_list):
        delimiter = '->'
        source_list.reverse()
        string_list = [node.id for node in source_list]
        return delimiter.join(string_list)

