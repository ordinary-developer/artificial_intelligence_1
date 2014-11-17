"""
Main module
"""


from app.logic.graph import Graph
from app.logic.node import Node


if __name__ == '__main__':
    #[INIT]
    # 1-st layer
    graph = Graph()
    # 2-nd layer
    graph.add_link("A", "B")
    graph.add_link("A", "C")
    graph.add_link("A", "D")
    # 3-d layer
    graph.add_link("B", "E")
    graph.add_link("B", "F")
    graph.add_link("C", "G")
    graph.add_link("C", "H")
    graph.add_link("D", "I")
    graph.add_link("D", "J")
    # 4-th layer
    graph.add_link("E", "K")
    graph.add_link("E", "L")
    graph.add_link("F", "L")
    graph.add_link("F", "M")
    graph.add_link("G", "N")
    graph.add_link("H", "O")
    graph.add_link("H", "P")
    graph.add_link("I", "P")
    graph.add_link("I", "Q")
    graph.add_link("J", "R")
    #[RUN]
    # breadth-first-search
    print('Breadth-first search for "N": [{}]'.format(
                graph.breadth_first_search("N")))
    # additional links
    graph.add_link("C", "M")
    graph.add_link("D", "Q")
    # depth-first-search
    print('Depth-first search for "I": [{}]'.format(
                graph.depth_first_search("I")))
