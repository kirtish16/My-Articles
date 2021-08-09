# Python implementation of the approach
def fact(N):

	# Base Case
	if (N == 1 or N == 0):
		return 1

	# Find the factorial recursively
	return N * fact(N - 1)


# Function to find the prefix
# factorial array
def prefixFactorialArray(arr, N):

	# Find the prefix sum array
	for i in range(1, N):
		arr[i] += arr[i - 1]

	# Find the factorials of each
	# array element
	for i in range(N):
		arr[i] = fact(arr[i])

		# Print the resultant array
	for i in range(N):
		print(arr[i], end=" ")

# Driver Code
if __name__ == "__main__":

	arr = [1, 2, 3, 4]
	N = len(arr)
	prefixFactorialArray(arr, N)

# This code is contributed by kirtishsurangalikar
