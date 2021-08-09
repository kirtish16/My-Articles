# Python3 program to find paths with maximum number
# of 'a' from (1, 1) to (X, Y) vertically
# or horizontally
n = 3
dp = [[0 for i in range(n)]
		for j in range(n)]

# Function to answer queries
def answerQueries(queries, q):

	# Iterate till query
	for i in range(q):
		
		# Decrease to get 0-based indexing
		x = queries[i][0]
		x -= 1
		y = queries[i][1]
		y -= 1

		# Print answer
		print(dp[x][y])

# Function that pre-computes the dp array
def pre_compute(a):

	# Check for the first character
	if a[0][0] == 'a':
		dp[0][0] = 0
	else:
		dp[0][0] = 1

	# Iterate in row and columns
	for row in range(n):
		for col in range(n):
			
			# If not first row or not first column
			if (row != 0 or col != 0):
				dp[row][col] = 9999

			# Not first row
			if (row != 0):
				dp[row][col] = min(dp[row][col],
								dp[row - 1][col])

			# Not first column
			if (col != 0):
				dp[row][col] = min(dp[row][col],
								dp[row][col - 1])

			# If it is not 'a' then increase by 1
			if (a[row][col] != 'a' and (row != 0 or
										col != 0)):
				dp[row][col] += 1

# Driver code
if __name__ == '__main__':
	
	# Character N X N array
	a = [ ('a', 'b', 'a'),
		('a', 'c', 'd'),
		('b', 'a', 'b') ]

	# Queries
	queries = [ (1, 3), (3, 3) ]

	# Number of queries
	q = 2

	# Function call to pre-compute
	pre_compute(a)

	# function call to answer every query
	answerQueries(queries, q)

# This code is contributed by kirtishsurangalikar
