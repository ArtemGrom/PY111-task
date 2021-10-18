import heapq
from typing import Hashable, Mapping, Union, Any
import networkx as nx


def dijkstra_algo(g: [dict, nx.DiGraph], starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    priority_queue = []
    heapq.heappush(priority_queue, (0, starting_node))
    visited = {}
    while priority_queue:
        (current_distance, current) = heapq.heappop(priority_queue)

        visited[current] = current_distance

        if current not in g: continue
        for neighbour, distance in g[current].items():
            if neighbour in visited:
                continue
            new_distance = current_distance + distance
            heapq.heappush(priority_queue, (new_distance, neighbour))

    return visited


def main():
    g = {
        'A': {'B': 2, 'D': 8, 'G': 9},
        'B': {'F': 1},
        'F': {'C': 1, 'D': 4},
        'C': {'F': 5, 'D': 1, 'H': 2},
        'D': {'G': 2, 'C': 1},
        'H': {},
        'G': {'A': 2},
        'E': {'B': 5, 'G': 3}
    }

    print(dijkstra_algo(g, 'A'))


if __name__ == '__main__':
    main()
