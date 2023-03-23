def power(a,k,n=10):
    r = 1 #result
    x = a%n
    while k>0:
        if k%2==1: r = r*x%n #if((k & 1) == 1)
        x **=2
        x %= n #x = (x*x)%n
        k //= 2 # k = k >> 1

    return r
print(power(145,17,17))


def power2(x,k,n=10): #a bit more efficient
    r = 1 #result
    x = x%n
    while k>0:
        if ((k & 1) == 1): r = r*x%n #if((k & 1) == 1)
        x = (x*x)%n
        k = k >> 1 

    return r
print(power2(145,17,17))


# Iterative Python3 program
# to compute modular power

# Iterative Function to calculate
# (x^y)%p in O(log y)
def power(x, y, p) :
	res = 1	 # Initialize result

	# Update x if it is more
	# than or equal to p
	x = x % p
	
	if (x == 0) :
		return 0

	while (y > 0) :
		
		# If y is odd, multiply
		# x with result
		if ((y & 1) == 1) :
			res = (res * x) % p

		# y must be even now
		y = y >> 1	 # y = y/2
		x = (x * x) % p
	return res
	

# Driver Code

x = 145; y = 17; p = 17

print("Power is ", power(x, y, p))


# This code is contributed by Nikita Tiwari.
