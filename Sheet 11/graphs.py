from typing import Generator


def is_graph[T](d: dict[T, set[T]]) -> bool:
    key_list = []
    value_list = []
    new_value_list = []
    for k, v in d.items():
        key_list.append(k)
        value_list.append(list(v))

    for i in value_list:
        new_value_list += i

    value_set = set(new_value_list)
    newest_value_list = list(value_set)

    return newest_value_list == key_list


example = {0: {1, 2}, 1: {2, 3}, 2: {0, 1, 2}, 4: {0}}
assert not is_graph(example)
example_graph = example | {3: set()}
assert is_graph(example_graph)
assert not is_graph({"a": {"a", "aa"}})
assert is_graph({})


def to_graph[T](d: dict[T, set[T]]) -> dict[T, set[T]]:
    if not is_graph(d):
        key_list: list = []
        value_list: list = []
        new_value_list: list = []
        missing: list = []
        for k, v in d.items():
            key_list.append(k)
            value_list.append(list(v))

        for i in value_list:
            new_value_list += i

        value_set: set = set(new_value_list)

        newest_value_list: list = list(value_set)

        for element in newest_value_list:
            if element not in key_list:
                missing.append(element)

        for i in missing:
            d[i] = set()  # type: ignore

        return d

    else:
        return d


assert to_graph(example) == to_graph(example_graph) == example_graph
assert to_graph(example_graph) is not example_graph
assert to_graph({"a": {"a", "aa"}}) == {"a": {"a", "aa"}, "aa": set()}
assert to_graph({}) == {}


def nodes(graph: dict) -> Generator:
    return (node for node in graph)


def edges(graph: dict) -> Generator:
    for source_node, target_nodes in graph.items():
        for target_node in target_nodes:
            yield (source_node, target_node)


assert set(nodes(example_graph)) == {0, 1, 2, 3, 4}
assert len(list(nodes(example_graph))) == 5
assert set(nodes({})) == set()
assert set(edges(example_graph)) == {
    (0, 1), (0, 2), (1, 2), (1, 3),
    (2, 0), (2, 1), (2, 2), (4, 0)
}
assert len(list(edges(example_graph))) == 8
assert set(edges({})) == set()


def invert_graph(graph: dict) -> dict:

    inverted_graph = {}

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if neighbor in inverted_graph:
                inverted_graph[neighbor].add(node)
            else:

                inverted_graph[neighbor] = {node}

    return to_graph(inverted_graph)


assert invert_graph(example_graph) == {
    0: {2, 4}, 1: {0, 2}, 2: {0, 1, 2}, 3: {1}, 4: set()
}
assert invert_graph(invert_graph(example_graph)) == example_graph
assert invert_graph({"a": {"a"}}) == {"a": {"a"}}
assert invert_graph({}) == {}
