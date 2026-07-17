from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.next: Optional["Node[T]"] = None
        self.previous: Optional["Node[T]"] = None


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None

    def push_head(self, value: T) -> Node[T]:
        """
        Add an element to the start of the list.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns a handle that can be passed to `remove`.
        """
        node = Node(value)
        node.next = self.head
        if self.head is not None:
            self.head.previous = node
        self.head = node
        if self.tail is None:
            self.tail = node
        return node

    def pop_tail(self) -> T:
        """
        Remove and return the element at the end of the list.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.tail is None:
            raise IndexError("pop_tail from empty list")
        node = self.tail
        self._unlink(node)
        return node.value

    def remove(self, node: Node[T]) -> None:
        """
        Remove the element referenced by a handle returned from `push_head`.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self._unlink(node)

    def _unlink(self, node: Node[T]) -> None:
        if node.previous is not None:
            node.previous.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

        node.next = None
        node.previous = None
