from typing import Hashable, List
import networkx as nx


def dfs(g: [dict, nx.Graph], start_node: Hashable, path=None) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    if path is None:
        path = []
    path = path + [start_node]
    for node in g[start_node]:
        if not node in path:
            path = dfs(g, node, path)
    return path


def main():
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

    print(dfs(g, 'A'))


if __name__ == '__main__':
    main()
