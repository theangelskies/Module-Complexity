from typing import Dict, List


class _TrieNode:
    def __init__(self):
        self.children: Dict[str, "_TrieNode"] = {}
        self.count = 0


def find_longest_common_prefix(strings: List[str]) -> str:
    """
    find_longest_common_prefix returns the longest string common at the start of any two strings in the passed list.

    In the event that an empty list, a list containing one string, or a list of strings with no common prefixes is passed, the empty string will be returned.

    Precomputes a trie of all strings (O(total characters) to build), tracking how many strings
    pass through each node. The answer is the prefix at the deepest node visited by at least two
    strings, avoiding the need to compare every pair of strings directly.
    """
    root = _TrieNode()
    longest = ""

    for string in strings:
        node = root
        for i, letter in enumerate(string):
            node = node.children.setdefault(letter, _TrieNode())
            node.count += 1
            if node.count >= 2 and i + 1 > len(longest):
                longest = string[: i + 1]

    return longest
