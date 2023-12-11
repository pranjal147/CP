# Read the input value of 'n'
n = int(input())

# Initialize a list to store the sequence of 'n' values
sequence = []

# Add the initial 'n' to the sequence
sequence.append(n)

# Simulate the algorithm until 'n' becomes 1
while n != 1:
    if n % 2 == 0:
        # If 'n' is even, divide it by 2
        n = n // 2
    else:
        # If 'n' is odd, multiply it by 3 and add 1
        n = 3 * n + 1
    # Add the updated 'n' value to the sequence
    sequence.append(n)

# Print the sequence of 'n' values
print(" ".join(map(str, sequence)))
