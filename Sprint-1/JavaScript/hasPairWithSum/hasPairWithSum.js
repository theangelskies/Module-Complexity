/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n^2) - the nested loops compare every pair of numbers (i, j):
 *   for each of the n items, the inner loop scans up to n more, giving n * n comparisons.
 * Space Complexity: O(1) - no extra data structures are used, just loop counters.
 * Optimal Time Complexity: O(n) - walk the array once, and for each number check whether
 *   its complement (target - number) has already been seen. A Set gives O(1) average
 *   lookup/insert, so the whole pass is linear instead of quadratic.
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seen = new Set();
  for (const num of numbers) {
    if (seen.has(target - num)) {
      return true;
    }
    seen.add(num);
  }
  return false;
}
