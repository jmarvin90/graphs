from typing import NoReturn

from src.node import Node

import pytest

@pytest.fixture
def my_node() -> Node:
    return Node(name="my_node")

@pytest.fixture
def your_node() -> Node:
    return Node(name="your_node")

@pytest.fixture
def our_node() -> Node:
    return Node(name="our_node")

@pytest.fixture
def some_node() -> Node:
    return Node(name="some_node")

@pytest.fixture
def other_node() -> Node:
    return Node(name="other_node")

@pytest.fixture
def this_node() -> Node:
    return Node(name="this_node")

@pytest.fixture
def that_node() -> Node:
    return Node(name="that_node")

def test_rshift(my_node: Node, your_node: Node) -> NoReturn:
    my_node >> your_node
    assert (
        your_node in my_node.children and
        my_node in your_node.parents
    )

def test_lshift(my_node: Node, your_node: Node) -> NoReturn:
    my_node << your_node
    assert (
        my_node in your_node.children and
        your_node in my_node.parents
    )

def test_l_and_r_shift(my_node: Node, your_node: Node, our_node: Node) -> NoReturn:
    my_node << your_node >> our_node
    assert (
        my_node in your_node.children and
        our_node in your_node.children and
        your_node in my_node.parents and
        your_node in our_node.parents
    )

def test_floordiv(my_node: Node, your_node: Node) -> NoReturn:
    my_node >> your_node
    connection_was_made = my_node in your_node.parents
    my_node // your_node
    assert(
        connection_was_made and
        my_node not in your_node.parents
    )

def test_routing_for_non_connected_nodes(
    my_node: Node, 
    your_node: Node,
    our_node: Node
) -> NoReturn:
    my_node >> your_node
    my_node >> our_node

    assert not your_node.route_to(our_node)


