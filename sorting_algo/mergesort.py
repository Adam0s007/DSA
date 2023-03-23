# Python program for implementation of MergeSort
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

# Code to print the list
 

#iterative merge sort:

# Iterative Merge sort (Bottom Up)

# Iterative mergesort function to
# sort arr[0...n-1]

# perform bottom up merge
def mergeSort(a):
	# start with least partition size of 2^0 = 1
	width = 1
	n = len(a)										
	# subarray size grows by powers of 2
	# since growth of loop condition is exponential,
	# time consumed is logarithmic (log2n)
	while (width < n):
		# always start from leftmost
		l=0
		while (l < n):
			r = min(l+(width*2-1), n-1)
			m = (l+r)//2
			# final merge should consider
			# unmerged sublist if input arr
			# size is not power of 2
			if (width>n//2):	
				m = r-(n%width)
			merge(a, l, m, r)
			l += width*2
		# Increasing sub array size by powers of 2
		width *= 2
	return a

# Merge Function
def merge(a, l, m, r):
	n1 = m - l + 1
	n2 = r - m
	L = [0] * n1
	R = [0] * n2
	for i in range(0, n1):
		L[i] = a[l + i]
	for i in range(0, n2):
		R[i] = a[m + i + 1]

	i, j, k = 0, 0, l
	while i < n1 and j < n2:
		if L[i] > R[j]:
			a[k] = R[j]
			j += 1
		else:
			a[k] = L[i]
			i += 1
		k += 1

	while i < n1:
		a[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		a[k] = R[j]
		j += 1
		k += 1


# Driver code
a = [12, 11, 13, 5, 6, 7]
print("Given array is ")
print(a)

mergeSort(a)

print("Sorted array is ")
print(a)

# Contributed by Madhur Chhangani [RCOEM]
# corrected and improved by @mahee96




# Driver Code
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]


# This code is contributed by Mayank Khanna
