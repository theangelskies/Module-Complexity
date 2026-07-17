/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n^2) - for each of the n items, the inner loop scans the
 *   uniqueItems array built so far (up to n items) to check whether it's a duplicate.
 * Space Complexity: O(n) - uniqueItems can grow up to n items in the worst case
 *   (no duplicates).
 * Optimal Time Complexity: O(n) - track items already seen in a Set instead of an
 *   array. Set membership checks are O(1) average, so a single pass over the input
 *   (still O(n) for the pass itself) replaces the O(n) inner scan, giving O(n) overall.
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  const seen = new Set();
  const uniqueItems = [];

  for (const item of inputSequence) {
    if (!seen.has(item)) {
      seen.add(item);
      uniqueItems.push(item);
    }
  }

  return uniqueItems;
}
