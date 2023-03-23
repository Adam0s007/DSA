import heapq

class Node:
    def __init__(self):
        self.left = None 
        self.right = None
        self.freq = 0
        self.val = None
    
    def __lt__(self,other): #for heapq!!!
        return self.freq < other.freq

def TraverveThroughText(text): #O(n) n - nr of characters
    ans = []
    mapMe = {}
    for elem in text:
        mapMe[elem] = mapMe.get(elem,0) + 1 
    for key,value in mapMe.items():  #letter : freq
        node = Node() 
        node.val = key
        node.freq = value
        ans.append(node)
    
    heapq.heapify(ans)
    return ans
 

def huffman(C): # C - text a tablica q na ktorej jest zrobiony heapify i zaw dane postaci [freq, Node] O(nlogn)
    q = TraverveThroughText(C) 
    n = len(q)
    while len(q) > 1:
        z = Node()
        x = heapq.heappop(q)
        y = heapq.heappop(q)
        z.left = x
        z.right = y 
        z.freq = x.freq + y.freq
        heapq.heappush(q,z) 
    return heapq.heappop(q)

def traverse(root):
    if not root: return
    print(root.freq,root.val)
    traverse(root.left)
    traverse(root.right)

def build_map(root):
    def dfs(root,code,encoding_map):
        if not root: return
        if root.val:
            encoding_map[root.val] = ''.join(code)
        else:
            code.append('0')
            dfs(root.left,code,encoding_map)
            code.pop()
            code.append('1')
            dfs(root.right,code,encoding_map)
            code.pop()

    encoding_map = {}
    dfs(root,[],encoding_map)
    return encoding_map


def encode(text):
    root = huffman(text)
    encoding_map =build_map(root)
    return ''.join([encoding_map[ch] for ch in text])

def decode(encoded,root):
    if root.val:
        return root.val * len(encoded)
    decoded = []
    node = root
    for bit in encoded:
        if bit == "0":
            node = node.left
        else: 
            node = node.right
        if node.val:
            decoded.append(node.val)
            node = root
    return ''.join(decoded)

text = "a"

root = huffman(text)
coding_map = build_map(root)
print(coding_map)
encoded_text =encode(text)
print(encoded_text)
print(decode(encoded_text,root))
#deepest nodes <=> least frequent characters



