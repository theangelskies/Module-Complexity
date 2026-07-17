def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.

    Precomputes the set of characters present in s once (O(len(s))), so that both the "is this
    upper-case letter's lower-case form present" check and the outer loop run over that set of
    unique characters (at most the alphabet size) rather than rescanning the whole string for
    every upper-case letter encountered.
    """
    present = set(s)
    only_upper = set()
    for letter in present:
        if is_upper_case(letter) and letter.lower() not in present:
            only_upper.add(letter)
    return len(only_upper)


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
