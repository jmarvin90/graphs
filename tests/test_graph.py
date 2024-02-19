from src.node import Node
from src.graph import Graph

import pytest

@pytest.fixture
def my_node() -> Node:
    return Node(name="my_node")

@pytest.fixture
def your_node() -> Node:
    return Node(name="your_node")

@pytest.fixture
def my_graph(my_node: Node, your_node: Node) -> Graph:    
    # Create an 'empty' graph
    my_graph = Graph()

    # Add our nodes to the graph
    my_graph += my_node
    my_graph += your_node

    # Connect our two nodes
    my_node >> your_node

    return my_graph

def test_nodes_are_present(
    my_graph: Graph, my_node: Node, your_node: Node
) -> None:
    assert (
        my_node in my_graph.nodes.values() and
        your_node in my_graph.nodes.values()
    )

def test_nodes_are_correct(my_graph: Graph) -> None:
    assert (
        my_graph.my_node in my_graph.your_node.parents and
        my_graph.your_node in my_graph.my_node.children
    )