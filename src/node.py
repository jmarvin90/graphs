from __future__ import annotations
from typing import Optional, List

class Node:
    def __init__(self, name):
        self.name = name
        self.__children = ()
        self.__parents = ()

    @property
    def children(self) -> tuple:
        """Return the current node's children."""
        return self.__children

    @property
    def parents(self) -> tuple:
        """Return the current node's parents."""
        return self.__parents

    def __lshift__(self, node: Node) -> Node:
        """Set a child:parent relationship to a given node."""
        node.add_child(self)
        return node

    def __rshift__(self, node: Node) -> Node:
        """Set a parent:child relationship to a given node."""
        self.add_child(node)
        return node

    def __floordiv__(self, node: Node) -> None:
        """Remove any relationships to a given node."""
        if node in self.__children:
            self.remove_child(node)
        if node in self.__parents:
            self.remove_parent(node)

    def add_child(self, node: Node) -> tuple:
        """Add a specified node as a child."""
        if node not in self.__children:
            self.__children = (*self.__children, node)
            node.add_parent(self)

        return self.__children

    def remove_child(self, node: Node) -> tuple:
        """Remove a parent:child relationship to a specified node."""
        if node in self.__children:
            self.__children = filter(
                lambda x: x is not node, self.__children
            )
            node.remove_parent(self)

        return self.__children

    def add_parent(self, node: Node) -> tuple:
        """Add a specified node as a parent."""
        if node not in self.__parents:
            self.__parents = (*self.__parents, node)
            node.add_child(self)

        return self.parents

    def remove_parent(self, node: Node) -> tuple:
        """Remove a child:parent relationship to a specified node."""
        if node in self.__parents:
            self.__parents = filter(
                lambda x: x is not node, self.__parents
            )
            node.remove_child(self)

        return self.__parents

    def __route(
        self, 
        end: Node, 
        direction: str, 
        path: Optional[List]=[], 
        start: Optional[Node]=None,
        prev: Optional[Node]=None
    ) -> list:
        """Return all nodes connecting the instance to a relative."""
        if direction == "to":
            collection_to_search = self.children
        
        if direction == "from":
            collection_to_search = self.parents

        if start is None:
            start = self

        path = path + [start]

        if start == end:
            return [path]

        paths = []

        for node in collection_to_search:
            if node not in path:
                newpaths = node.__route(
                    start=node, end=end, direction=direction, path=path
                )

                for newpath in newpaths:
                    paths.append(newpath)

        return paths 

    def route_to(self, node: Node) -> list:
        """Return nodes linking source and target via parental connections."""
        return self.__route(node, "to")

    def route_from(self, node: Node) -> list:
        """Return nodes linking source and target via child connections."""
        return self.__route(node, "from")
