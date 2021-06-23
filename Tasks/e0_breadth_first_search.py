from collections import deque
from typing import Hashable, List

import networkx as nx

start_node = 'A'
g = {}
g[start_node] = ['B', 'F']
g['B'] = ['G']
g['F'] = ['G']
g['G'] = ['C', 'H', 'I']
g['C'] = ['H']
g['I'] = ['H']
g['H'] = ['D', 'E', 'J']
g['E'] = ['D']
g['D'] = []
g['J'] = []


def bfs(g: [dict, nx.Graph], start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    search_queue = deque()
    search_queue += g[start_node]
    searched = [start_node]
    while search_queue:
        char = search_queue.popleft()
        if not char in searched:
            search_queue += g[char]
            searched.append(char)
    return searched


def main():
    print(bfs(g, 'A'))


if __name__ == '__main__':
    main()
