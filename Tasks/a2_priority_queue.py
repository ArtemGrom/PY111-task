"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

_priority_queue = {i: [] for i in range(11)}


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    _priority_queue.setdefault(priority, elem)
    _priority_queue[priority].append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    _priority_queue.clear()


if __name__ == '__main__':
    print(_priority_queue)
    enqueue("a", 4)
    print(_priority_queue)
    enqueue("a", 5)
    print(_priority_queue)
    enqueue("b", 4)
    print(_priority_queue)
    # enqueue("a", 1)
    # print(_priority_queue)