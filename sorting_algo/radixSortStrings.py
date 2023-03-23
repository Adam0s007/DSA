
def radixSort(arr:str):
    n = len(arr)
    maks= 0
    for elem in arr:
        maks = max(len(elem),maks)
    n = len(arr)
    output = ["" for i in range(n)] 
    count = [0]*(26)

    for y in range(-1,-maks-1,-1):
        output = ["" for i in range(n)] 
        count = [0]*(26)
        for i in range(0, n):
            if y >= -len(arr[i]):  index = ord(arr[i][y]) - ord('a')  
            else: index = ord(arr[i][0]) -   ord('a')
            count[index] += 1
        for i in range(1, 26):
            count[i] += count[i - 1]
        for i in range(n-1,-1,-1):
            if y >= -len(arr[i]):  index = ord(arr[i][y]) - ord('a')   
            else: index = ord(arr[i][0]) -   ord('a')
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        for i in range(n):
            arr[i] = output[i]


        




# Driver code
arr = ["aab","ac","aabc","ddbc","daa","aa","a","dc","abb","ab","ccc","dab","bbda"]

# Function Call
radixSort(arr)
 
for i in range(len(arr)):
    print(arr[i],end=" ")

a = "BCDEFG"
# This code is contributed by Mohit Kumra
# Edited by Patrick Gallagher