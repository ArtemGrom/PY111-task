"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple, Dict

# import networkx as nx

root: Optional[Dict] = None


def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    global root
    new_node = {"key": key, "value": value, "left": None, "right": None}
    if root is None:
        root = new_node
        return

    current_node = root
    while True:
        if key > current_node["key"]:
            if current_node["right"] is None:
                current_node["right"] = new_node
                return
            else:
                current_node = current_node["right"]
        elif key < current_node["key"]:
            if current_node["left"] is None:
                current_node["left"] = new_node
                return
            else:
                current_node = current_node["left"]

        else:
            root["value"] = value
            return


def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    global root
    current_node = root
    prev_node = None
    while True:
        if key > current_node["key"]:
            if current_node["right"] is None:
                return None
            prev_node = current_node["key"]
            current_node = current_node["right"]
        elif key < current_node["key"]:
            if current_node["left"] is None:
                return None
            prev_node = current_node["key"]
            current_node = current_node["left"]
        else:
            if current_node["right"] is current_node["left"] is None:
                if current_node["key"] < prev_node["key"]:
                    prev_node["left"] = None
                else:
                    prev_node["right"] = None

            elif current_node["right"] is None or current_node["left"] is None:
                if current_node["left"] is None:

                    prev_node["right"] = current_node["right"]
                else:
                    prev_node["left"] = current_node["left"]

            # else:
            #     min_node = current_node["right"]
            #
            #     while current_node:








def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    global root
    if root is None:
        raise KeyError

    current_node = root
    while True:
        if key > current_node["key"]:
            if current_node["right"] is None:
                raise KeyError
            current_node = current_node["right"]
        elif key < current_node["key"]:
            if current_node["left"] is None:
                raise KeyError
            current_node = current_node["left"]
        else:
            return current_node["value"]


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    global root
    root = None


def main():
    clear()
    insert(10, 10)
    # print(root)
    insert(15, 15)
    # print(root)
    insert(5, 5)
    # print(root)
    insert(20, 20)
    # print(root)
    print(find(5))


if __name__ == '__main__':
    main()
