# Matrix chain multiplication problem: Determine the 
# optimal parenthesization of a product of n matrices.

# Matrix chain multiplication (or Matrix Chain Ordering Problem, MCOP) 
# is an optimization problem that to find the most efficient way to multiply a given 
# sequence of matrices. The problem is not actually to perform the multiplications 
# but merely to decide the sequence of the matrix multiplications involved.

 
# The matrix multiplication is associative as no matter how the product is parenthesized,
#  the result obtained will remain the same. For example, 
# for four matrices A, B, C, and D, we would have:
# ((AB)C)D = ((A(BC))D) = (AB)(CD) = A((BC)D) = A(B(CD))

 
# However, the order in which the product is parenthesized affects the number of simple arithmetic 
# operations needed to compute the product. 
# For example, if A is a 10 × 30 matrix, B is a 30 × 5 matrix, and C is a 5 × 60 matrix, 
# then computing (AB)C needs (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations 
# while computing A(BC) needs (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations. 
# Clearly, the first method is more efficient.


import sys
 
 
# Function to find the most efficient way to multiply
# a given sequence of matrices
def matrixChainMultiplication(dims, i, j, lookup): #O(n^3)
 
    # base case: one matrix
    if j <= i + 1:
        return 0
    # stores the minimum number of scalar multiplications (i.e., cost)
    # needed to compute matrix `M[i+1] … M[j] = M[i…j]`
    min = sys.maxsize
 
    # if the subproblem is seen for the first time, solve it and
    # store its result in a lookup table
    if lookup[i][j] == 0:
        # take the minimum over each possible position at which the
        # sequence of matrices can be split
        '''
            (M[i+1]) × (M[i+2]………………M[j])
            (M[i+1]M[i+2]) × (M[i+3…………M[j])
            …
            …
            (M[i+1]M[i+2]…………M[j-1]) × (M[j])
        '''
        for k in range(i + 1, j):
            # recur for `M[i+1]…M[k]` to get an `i × k` matrix
            cost = matrixChainMultiplication(dims, i, k, lookup)
 
            # recur for `M[k+1]…M[j]` to get an `k × j` matrix
            cost += matrixChainMultiplication(dims, k, j, lookup)
 
            # cost to multiply two `i × k` and `k × j` matrix
            cost += dims[i] * dims[k] * dims[j]
 
            if cost < min:
                min = cost
 
        lookup[i][j] = min
 
    # return the minimum cost to multiply `M[j+1]…M[j]`
    return lookup[i][j]
 
 
if __name__ == '__main__':
 
    # Matrix `M[i]` has dimension `dims[i-1] × dims[i]` for `i=1…n`
    # input is 10 × 30 matrix, 30 × 5 matrix, 5 × 60 matrix
    dims = [10, 30, 5, 60]
 
    # lookup table to store the solution to already computed subproblems
    lookup = [[0 for x in range(len(dims))] for y in range(len(dims))]
 
    n = len(dims)
    print('The minimum cost is', matrixChainMultiplication(dims, 0, n - 1, lookup))




#written same thing:
    def matrixChainMultiplication(dims, i, j, lookup): #O(n^3)
        if j <= i + 1:
            return 0
        min = sys.maxsize
        if lookup[i][j] == 0:
            for k in range(i + 1, j):
                cost = matrixChainMultiplication(dims, i, k, lookup)
                cost += matrixChainMultiplication(dims, k, j, lookup)
                cost += dims[i] * dims[k] * dims[j]
                if cost < min:
                    min = cost
            lookup[i][j] = min
        return lookup[i][j]
 

    dims = [10, 30, 5, 60]
    lookup = [[0 for x in range(len(dims))] for y in range(len(dims))]
 
    n = len(dims)
    print('The minimum cost is', matrixChainMultiplication(dims, 0, n - 1, lookup))