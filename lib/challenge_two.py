def digit_sum(num):
    """Calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(num))

def solution(A):
    max_sum = -1
    
    # Iterate through each pair of numbers
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if digit_sum(A[i]) == digit_sum(A[j]):
                pair_sum = A[i] + A[j]
                max_sum = max(max_sum, pair_sum)
    
    return max_sum

# Test cases
print(solution([51, 71, 17, 42]))  # Output: 93 (51 + 42)
print(solution([42, 33, 60]))      # Output: 102 (42 + 60)
print(solution([51, 32, 43]))      # Output: -1 (No pairs with equal digit sum)
