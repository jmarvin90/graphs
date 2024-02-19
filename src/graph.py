from __future__ import annotations

from src.node import Node

class Graph:
    def __init__(self): 
        self.__graph = 0

    @property
    def graph(self):
        """Return the graph."""
        return self.__graph

    @property
    def nodes(self) -> list:
        """Return a dictionary of all nodes as name:node."""
        return {
            key: value for key, value in self.__dict__.items()
            if type(value) == Node
        }

    @property
    def size(self) -> int:
        """Get the size of the graph as number of nodes."""
        return len(self.__nodes)

    def __add__(self, node: Node) -> Graph:
        """Add a node to the graph (e.g. graph + node)."""
        if node.name not in self.__dict__.keys():
            self.__dict__[node.name] = node

        return self

    def __sub__(self, node: Node) -> Graph:
        """Remove a node from the graph (e.g. graph - node)."""
        if node.name in self.__dict__.keys():
            del(self.__dict__[node.name])

        return self