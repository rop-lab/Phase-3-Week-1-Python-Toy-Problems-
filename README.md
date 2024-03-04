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
print(solution([7, 15, 10, 8]))  
print(solution([11, 10, 8, 12, 8, 10, 11]))  
print(solution([7, 14, 10])) 
```

## Challenge_two
## Pair Sum with Equal Digit Sums

This Python script provides a solution to find the maximum sum of pairs of numbers from a given list where each pair has equal digit sums.

# Functionality

The script includes the following functions:

### `digit_sum(num)`

This function calculates the sum of digits of a given number.

#### Arguments

- `num`: The input number.

#### Returns

- The sum of the digits of the input number.

### `solution(A)`

This function finds the maximum sum of pairs of numbers from a given list `A`, where each pair has equal digit sums.

#### Arguments

- `A`: A list of integers.

#### Returns

- The maximum sum of pairs of numbers with equal digit sums. If no such pairs exist, it returns -1.

## Example Usage

```python
print(solution([51, 71, 17, 42]))  # Output: 93 (51 + 42)
print(solution([42, 33, 60]))      # Output: 102 (42 + 60)
print(solution([51, 32, 43]))      # Output: -1 (No pairs with equal digit sum)
```

## Challenge_three

# Letter Distribution

This Python script generates a string of lowercase letters, distributing them evenly based on the given integer input `N`.

## Function Description

The `solution(N)` function takes an integer `N` as input and returns a string where each lowercase letter occurs a specific number of times, determined by the value of `N`. The distribution is such that each letter appears as many times as possible, with any remaining characters evenly distributed among the letters.

## Algorithm

1. Calculate the maximum number of times each letter can occur by dividing `N` by 26.
2. Generate a string containing each letter repeated `max_count` times.
3. Distribute any remaining characters evenly among the letters.
4. Return the resulting string.

## Usage

To use the script, call the `solution(N)` function with an integer `N` as input.

```python
print(solution(5))   # Output: "abcde"
print(solution(10))  # Output: "abcdefghij"
print(solution(26))  # Output: "abcdefghijklmnopqrstuvwxyz"
print(solution(30))  # Output: "abbcdeefghijjklmnopqrstuvwxzy" (each letter occurs twice except 'y' occurs once)
```
