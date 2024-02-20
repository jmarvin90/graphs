from __future__ import annotations

from src.node import Node

class Graph:

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
        return len(self.nodes.keys())

    @property
    def node_index(self) -> dict:
        """Create an dictionary of node:index number for nodes in the graph."""
        return {node: _+1 for _, node in enumerate(self.nodes.values())}

    def __conn_bit(self, node_1: Node, node_2: Node) -> int:
        """Decimal value for bit representing connection between two nodes."""
        from_ = (self.size - self.node_index[node_1]) + 1
        to_ = (self.size - self.node_index[node_2]) + 1
        base = self.size * from_
        val = base - (self.size - to_)
        return 2**(val -1)

    @property
    def graph(self):
        """Return the decimal value representing the graph."""
        graph = 0

        for node in self.nodes.values():
            for child in node.children:
                graph |= self.__conn_bit(node, child)

        return graph

    def __str__(self) -> str:
        """Return a string representation of the adjacency matrix."""
        binval = bin(self.graph)
        strval = str(binval[2:]).rjust(self.size**2, "0")
        output = ""

        for row in range(0, self.size**2, self.size):
            output += strval[row:row+self.size] + "\n"

        return output

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