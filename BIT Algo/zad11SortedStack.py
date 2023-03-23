# Zaproponuj algorytm, ktory w czasie O(nlogn) posortuje stos o rozmiarze n.
# Dozwolone jest tylko wykorzystywanie operacji udostepnionych przez interfejs stosu:
# push(), pop(), top(),isEmpty() oraz dodatkowych stosow.

class stos:
    def __init__(self,stack=None):
        if stack == None:
            self.tab = []
            self.size = 0
        else: 
            self.tab = stack.tab
            self.size = stack.size
    
    def isEmpty(self):
        if self.size > 0 : return False
        else: return True

    def push(self,val):
        self.tab.append(val)
        self.size +=1
        return self
    
    def _pop(self):
        if not(self.isEmpty()):
            self.size -=1
            return self.tab.pop()
        else: return None

    def top(self):
        if not(self.isEmpty()):
            return self.tab[self.size-1]
        else: return None
    def display(self):
        print(self.tab)
    
    
def mergeSortStack(stack):
    s1 = stos()
    s2 = stos()
    if stack.isEmpty(): return stack
    while not(stack.isEmpty()):
        if stack.size % 2==0: 
            s1.push(stack._pop())
        else: 
            s2.push(stack._pop())
    if s1.size >1:
        mergeSortStack(s1)
    if s2.size >1:
        mergeSortStack(s2)
    return merge_stos(s1,s2)


def merge_stos(stack1,stack2):
    if stack1.size == 0:
        return stack2
    if stack2.size == 0:
        return stack1
    merged_stack = stos()
    while stack1.size > 0 and stack2.size > 0:
        if stack1.top() < stack2.top(): merged_stack.push(stack1._pop())
        else: merged_stack.push(stack2._pop())

    while stack1.size >0: merged_stack.push(stack1._pop())
    while stack2.size>0: merged_stack.push(stack2._pop())
    merged_stack.display()
    return merged_stack

stosik1   = stos()
stosik1.push(1)
stosik1.push(6)
stosik1.push(15)
stosik1.push(5)
stosik1.push(8)
stosik1.push(13)
stosik1.push(14)
# stosik = merge_stos(stosik1,stosik2)
# while stosik.size > 0:
#     print(stosik._pop())

stosik1 = mergeSortStack(stosik1)
stosik1.display()


    




            



