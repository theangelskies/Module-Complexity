from typing import Dict, List


def calculate_sum_and_product(input_numbers: List[int]) -> Dict[str, int]:
    """
    Calculate the sum and product of integers in a list.

    Note: the sum is every number added together
    and the product is every number multiplied together
    so for example: [2, 3, 5] would return
    {
        "sum": 10, // 2 + 3 + 5
        "product": 30 // 2 * 3 * 5
    }
    Time Complexity: O(n) - two separate loops each iterate over the n numbers once
        (2n steps total), which is still linear overall since constants are dropped
        in Big-O notation.
    Space Complexity: O(1) - only a fixed number of accumulator variables are used.
    Optimal time complexity: O(n) - every number must be read at least once to sum
        and multiply it, so linear time is already optimal; the complexity class
        can't be reduced further. The refactor below combines the two loops into one
        to halve the constant factor (n steps instead of 2n), but it stays O(n).
    """
    # Edge case: empty list
    if not input_numbers:
        return {"sum": 0, "product": 1}

    sum = 0
    product = 1
    for current_number in input_numbers:
        sum += current_number
        product *= current_number

    return {"sum": sum, "product": product}
