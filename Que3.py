# Python3 implementation of the approach

# Function to multiply two square matrices
def multiplyMatrices(arr1, arr2):

	order = len(arr1)
	ans = [[0 for i in range(order)] for j in range(order)]

	for i in range(order):
		for j in range(order):
			for k in range(order):
				ans[i][j] += arr1[i][k] * arr2[k][j]

	return ans


# Function to find all the pairs that
# can be connected with exactly 'k' edges
def solve(arr, k):
	res = [[0 for i in range(len(arr))] for j in range(len(arr))]

	# Copying arr to res,
	# which is the result for k=1
	for i in range(len(arr)):
		for j in range(len(arr)):
			res[i][j] = arr[i][j]

	# Multiplying arr with itself
	# the required number of times
	for i in range(2, k+1):
		res = multiplyMatrices(res, arr)

	for i in range(len(arr)):
		for j in range(len(arr)):

			# If there is a path between 'i'
			# and 'j' in exactly 'k' edges
			if (res[i][j] > 0):
				print(i, "->", j, "in", res[i][j], "way(s)")


# Driver Code
if __name__ == "__main__":

	arr = [1, 2, 3, 4]
	arr = [[0 for i in range(5)] for j in range(5)]
	arr[0][1] = 1
	arr[1][2] = 1
	arr[2][3] = 1
	arr[2][4] = 1
	arr[3][0] = 1
	arr[4][2] = 1
	k = 3

	solve(arr, k)
	
# This code is contributed by kirtishsurangalikar
