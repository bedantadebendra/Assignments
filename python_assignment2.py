# Function to calculate the minimum number of players to be shot
def min_players_to_shot(N, K, heights):
    if len(heights) != N:
        return "wrong no of input given"
    count = 0
    for height in heights:
        if height >= K:
            count += 1
    return count

# Read the number of test cases
T = int(input("Enter the number of test cases:"))
for _ in range(T):
    # Read input for each test case
    N, K = map(int, input().split())
    heights = list(map(int, input().split()))
    
    # Calculate and print the result for each test case
    result = min_players_to_shot(N, K, heights)
    print(result)
