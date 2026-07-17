import random
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")

MAX_LEVEL = 16
LEVEL_PROBABILITY = 0.5


class _Node(Generic[T]):
    def __init__(self, value: Optional[T], level: int):
        self.value = value
        self.forward: List[Optional["_Node[T]"]] = [None] * (level + 1)


class SkipList(Generic[T]):
    def __init__(self):
        self._head: _Node[T] = _Node(None, MAX_LEVEL - 1)
        self._level = 0
        self._size = 0

    def insert(self, value: T) -> None:
        """
        Insert value into the skip list, keeping elements sorted.

        Time Complexity: O(log n) expected
        Space Complexity: O(log n) expected
        """
        update: List[_Node[T]] = [self._head] * MAX_LEVEL
        node = self._head
        for i in range(self._level, -1, -1):
            while node.forward[i] is not None and node.forward[i].value < value:
                node = node.forward[i]
            update[i] = node

        new_level = self._random_level()
        if new_level > self._level:
            for i in range(self._level + 1, new_level + 1):
                update[i] = self._head
            self._level = new_level

        new_node = _Node(value, new_level)
        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

        self._size += 1

    def __contains__(self, value: T) -> bool:
        """
        Check whether value is present in the skip list.

        Time Complexity: O(log n) expected
        Space Complexity: O(1)
        """
        node = self._head
        for i in range(self._level, -1, -1):
            while node.forward[i] is not None and node.forward[i].value < value:
                node = node.forward[i]
        node = node.forward[0]
        return node is not None and node.value == value

    def to_list(self) -> List[T]:
        """
        Return all elements in sorted order.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = []
        node = self._head.forward[0]
        while node is not None:
            result.append(node.value)
            node = node.forward[0]
        return result

    def __len__(self) -> int:
        return self._size

    def _random_level(self) -> int:
        level = 0
        while level < MAX_LEVEL - 1 and random.random() < LEVEL_PROBABILITY:
            level += 1
        return level
