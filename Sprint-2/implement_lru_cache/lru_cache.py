from typing import Dict, Generic, Optional, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class _Node(Generic[K, V]):
    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value
        self.next: Optional["_Node[K, V]"] = None
        self.previous: Optional["_Node[K, V]"] = None


class LruCache(Generic[K, V]):
    def __init__(self, limit: int):
        if limit <= 0:
            raise ValueError("limit must be a positive integer")
        self.limit = limit
        self._entries: Dict[K, _Node[K, V]] = {}
        self._head: Optional[_Node[K, V]] = None
        self._tail: Optional[_Node[K, V]] = None

    def get(self, key: K) -> Optional[V]:
        """
        Look up the value previously associated with key, marking it as
        most recently used. Returns None if key is not present.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        node = self._entries.get(key)
        if node is None:
            return None
        self._move_to_head(node)
        return node.value

    def set(self, key: K, value: V) -> None:
        """
        Associate value with key, marking it as most recently used.
        Evicts the least recently used entry if the cache is at its limit.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        node = self._entries.get(key)
        if node is not None:
            node.value = value
            self._move_to_head(node)
            return

        if len(self._entries) >= self.limit:
            self._evict()

        node = _Node(key, value)
        self._entries[key] = node
        self._push_head(node)

    def _push_head(self, node: _Node[K, V]) -> None:
        node.next = self._head
        if self._head is not None:
            self._head.previous = node
        self._head = node
        if self._tail is None:
            self._tail = node

    def _unlink(self, node: _Node[K, V]) -> None:
        if node.previous is not None:
            node.previous.next = node.next
        else:
            self._head = node.next

        if node.next is not None:
            node.next.previous = node.previous
        else:
            self._tail = node.previous

        node.next = None
        node.previous = None

    def _move_to_head(self, node: _Node[K, V]) -> None:
        if self._head is node:
            return
        self._unlink(node)
        self._push_head(node)

    def _evict(self) -> None:
        lru = self._tail
        if lru is None:
            return
        self._unlink(lru)
        del self._entries[lru.key]
