"""
My little Stack
"""
from typing import Any

_stack = []


def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    _stack.append(elem)


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    if len(_stack) == 0:
        return None
    del_elem = _stack.pop()
    return del_elem


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    if len(_stack) == 0:
        return None
    if ind < len(_stack):
        ind = (ind + 1) * -1
        return _stack[ind]


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    _stack.clear()
