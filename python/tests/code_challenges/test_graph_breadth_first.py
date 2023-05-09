import pytest
from code_challenges.graphs.graph import Graph, Vertex


def test_exists():
    assert Graph


# @pytest.mark.skip("TODO")
def test_bfs(graph):
    nodes = graph.get_nodes()
    root = nodes[0]
    print(root.value)
    actual = graph.breadth_first(root)
    expected = ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Narnia", "Naboo"]
    assert actual == expected

    # DANGER: Metroville/Monstropolis could be switched as well as Narnia/Naboo and still be valid BFS. What to do?


def test_one_node():
    graph_one = Graph()
    apple = graph_one.add_node('apple')
    actual = graph_one.breadth_first(apple)
    expected = ['apple']
    assert actual == expected


def test_no_node():
    graph_two = Graph()
    vertex = Vertex('apple')
    with pytest.raises(KeyError):
        graph_two.breadth_first(vertex)


def test_invalid_node(graph):
    vertex = Vertex('apple')
    with pytest.raises(KeyError):
        graph.breadth_first(vertex)


@pytest.fixture
def graph():

    realms = Graph()

    pandora = realms.add_node("Pandora")
    arendelle = realms.add_node("Arendelle")
    metroville = realms.add_node("Metroville")
    monstropolis = realms.add_node("Monstropolis")
    narnia = realms.add_node("Narnia")
    naboo = realms.add_node("Naboo")

    realms.add_edge(pandora, arendelle)

    realms.add_edge(arendelle, pandora)
    realms.add_edge(arendelle, metroville)
    realms.add_edge(arendelle, monstropolis)

    realms.add_edge(metroville, arendelle)
    realms.add_edge(metroville, monstropolis)
    realms.add_edge(metroville, narnia)

    realms.add_edge(monstropolis, arendelle)
    realms.add_edge(monstropolis, metroville)
    realms.add_edge(monstropolis, naboo)

    realms.add_edge(narnia, metroville)
    realms.add_edge(narnia, naboo)

    realms.add_edge(naboo, metroville)
    realms.add_edge(naboo, monstropolis)
    realms.add_edge(naboo, narnia)

    return realms
