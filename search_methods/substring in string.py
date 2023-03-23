#How many times smaller string occures in larger string?

def naive_search(strn,word):
    leng = len(word)
    count = 0
    for i in range(len(strn)-leng+1):
        for j in range(len(word)):
            if strn[j+i] != word[j]:
                break
            if j + 1 == len(word):
                count+=1  
    return count

print(naive_search("wowomgzomg", "omg"))
print(naive_search("abcdhdhdabcghabc","abc"))

#KMP algorythm
# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            print ("Found pattern at index " + str(i-j))
            j = lps[j-1] #we want to find all matching patterns!!
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
                
 #https://www.youtube.com/watch?v=GTJr8OvyEVQ 
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
    lps[0] = 0  # lps[0] is always 0
    i = 1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0: len = lps[len-1]
            else:
                lps[i] = 0
                i += 1
    #print(lps)
  
txt = "ABABDABACDABABCABABXJXJX"
pat = "AB"
#lps for that: [0, 0, 1, 2, 0, 1, 2, 3, 4]
KMPSearch(pat, txt)
  
# This code is contributed by Bhavya Jain


