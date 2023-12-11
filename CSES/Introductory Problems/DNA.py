# Read the input DNA sequence
sequence = input().strip()

# Initialize variables to track the current character and repetition count
current_char = sequence[0]
current_count = 1
max_count = 1  # Initialize the maximum repetition count to 1

# Iterate through the sequence starting from the second character
for i in range(1, len(sequence)):
    if sequence[i] == current_char:
        # If the current character is the same as the previous one, increment the count
        current_count += 1
    else:
        # If the current character is different, update the maximum count if needed
        max_count = max(max_count, current_count)
        # Reset the current character and count
        current_char = sequence[i]
        current_count = 1

# Update the maximum count one last time (for the last character)
max_count = max(max_count, current_count)

# Print the length of the longest repetition
print(max_count)
