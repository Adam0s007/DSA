# Python 3 program to sort a string
# of characters
 
MAX_CHAR = 26
 
# function to print string in sorted order
def sortString(str):
     
    # Hash array to keep count of characters.
    # Initially count of all characters is
    # initialized to zero.
    charCount = [0 for i in range(MAX_CHAR)]
     
    # Traverse string and increment
    # count of characters
    for i in range(0, len(str), 1):
         
        # 'a'-'a' will be 0, 'b'-'a' will be 1,
        # so for location of character in count
        # array we will do str[i]-'a'.
        charCount[ord(str[i]) - ord('a')] += 1
    
    # Traverse the hash array and print
    # characters
    for i in range(0, MAX_CHAR, 1):
        for j in range(charCount[i]):
            print(chr(ord('a') + i), end = "")
# Driver Code
if __name__ == '__main__':
    s = "geeksforgeeks"
    sortString(s)
     
# This code is contributed by
# Sahil_Shelangia