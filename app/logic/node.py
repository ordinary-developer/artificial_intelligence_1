"""
Node module
This modules contains node logic
"""

class Node:
    def __init__(self, id):
        self.id = id
        self.parents = []
        self.children = []

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return True if self.id == other.id else False

    def __ne__(self, other):
        if not isinstance(other, Node):
            return True 
        return True if self.id != other.id else False

    def add_parent(self, parent_node):
        if not parent_node in self.parents:
            self.parents.append(parent_node)

    def add_child(self, child_node):
        if not child_node in self.children:
            self.children.append(child_node)

    def find_node(self, id):
        node = None
        if self.id == id:
            return self
        if len(self.children) == 0:
            return None
        else:
            for current_node in self.children:
                node = current_node.find_node(id)
                if node != None:
                    break
        return node
