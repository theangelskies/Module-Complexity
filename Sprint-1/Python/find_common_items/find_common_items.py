from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n * m) - for every item in first_sequence (n items), the inner
        loop scans second_sequence (m items) looking for a match, and `i not in
        common_items` scans the results collected so far too.
    Space Complexity: O(n) - common_items holds at most n unique items from
        first_sequence.
    Optimal time complexity: O(n + m) - build a set from second_sequence once (O(m))
        so each membership check against it is O(1), then make a single pass over
        first_sequence (O(n)), tracking items already added with a set to avoid
        rescanning the result list.
    """
    second_set = set(second_sequence)
    seen = set()
    common_items: List[ItemType] = []
    for item in first_sequence:
        if item in second_set and item not in seen:
            seen.add(item)
            common_items.append(item)
    return common_items
