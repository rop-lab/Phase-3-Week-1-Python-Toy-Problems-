# Phase-3-Week-1-Python-Toy-Problems-
# callenge_one
# Solution for Brick Stacking Problem

This solution is for a problem where there are N boxes arranged in a row, each containing a different number of bricks. The goal is to adjust the number of bricks in each box to make them all contain exactly 10 bricks. We can only add or remove bricks by moving them to adjacent boxes.

## Code Explanation

The function `solution(A)` takes an array `A` of length `N` representing the number of bricks in each box and returns the minimum number of moves needed to achieve the goal. If it's not possible to achieve exactly 10 bricks in each box, it returns -1.

Here's how the code works:

1. It iterates through each box in the array.
2. For each box, it calculates the difference between the current number of bricks and the target of 10 bricks.
3. If the difference is zero, it moves to the next box.
4. If the difference is negative, it tries to distribute bricks from the next box to make the current box contain 10 bricks. If it's not possible because it's the last box, it returns -1.
5. If the difference is positive, it removes excess bricks by updating the number of moves.
6. Finally, it returns the total number of moves needed.

## Example Usage

```python
print(solution([7, 15, 10, 8]))  # Output: 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # Output: 6
print(solution([7, 14, 10]))  # Output: -1
