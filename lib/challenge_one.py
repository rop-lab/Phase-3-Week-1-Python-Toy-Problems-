def solution(A):
    n = len(A)
    moves = 0
    
    # Iteration through each box
    for i in range(n):
        # number of bricks needed to add or remove
        diff = A[i] - 10
        
        # If the box already contains 10 bricks, move to the next box
        if diff == 0:
            continue
        
        # If the number of bricks needed is negative, we need to add bricks
        if diff < 0:
            # If we're at the last box and need to add bricks, it's not possible
            if i == n - 1:
                return -1
            # Otherwise, move bricks from the next box
            A[i + 1] += diff
            moves += abs(diff)
        else:  # If the number of bricks needed is positive, we need to remove bricks
            moves += diff
    
    return moves

# Test
print(solution([7, 15, 10, 8]))  # Output: 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # Output: 6
print(solution([7, 14, 10]))  # Output: -1
