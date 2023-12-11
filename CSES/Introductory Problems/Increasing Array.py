# Read the input values
n = int(input())
arr = list(map(int, input().split()))

# Initialize the minimum moves counter to 0
moves = 0

# Iterate through the array, starting from the second element
for i in range(1, n):
    if arr[i] < arr[i - 1]:
        # If the current element is smaller than the previous one,
        # increment it to make it at least as large as the previous one
        moves += (arr[i - 1] - arr[i])
        arr[i] = arr[i - 1]  # Update the current element

# Print the minimum number of moves required
print(moves)
