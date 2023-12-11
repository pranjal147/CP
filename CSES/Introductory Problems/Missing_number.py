# Read the input value of 'n'
n = int(input())

# Read the (n-1) distinct numbers as a list
numbers = list(map(int, input().split()))

# Calculate the sum of all numbers from 1 to n
total_sum = (n * (n + 1)) // 2

# Calculate the sum of the given (n-1) numbers
given_sum = sum(numbers)

# Find the missing number by subtracting the given sum from the total sum
missing_number = total_sum - given_sum

# Print the missing number
print(missing_number)
