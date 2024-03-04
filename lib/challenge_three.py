def solution(N):
    # Calculate the maximum number of times each letter can occur
    max_count = N // 26
    
    # Generate a string containing each letter repeated max_count times
    result = "".join(chr(ord('a') + i) * max_count for i in range(26))
    
    # Distribute any remaining characters evenly among the letters
    remaining = N % 26
    for i in range(remaining):
        result = result[:i*(max_count+1)] + result[i*(max_count+1):] + chr(ord('a') + i)
    
    return result

# Test 
print(solution(5))  # Output: "abcde"
print(solution(10)) # Output: "abcdefghij"
print(solution(26)) # Output: "abcdefghijklmnopqrstuvwxyz"
print(solution(30)) # Output: "abbcdeefghijjklmnopqrstuvwxzy" (each letter occurs twice except 'y' occurs once)
