class slownik():
    def __init__(self,size):
        self.tab = [[] for i in range(size)]
        self.size = size
    def _hash(self,key): #to bedzie string
    
        total = 0
        prime = 103511  
        #key bedzie intem!
        minim = min(key+7,17)
        for i in range(minim):
            total = (total * prime + i) % self.size
        return abs(total)
    
    def _set(self,key,value): #separate chainings 
        index = self._hash(key)
        if len(self.tab[index]) == 0:
            self.tab[index].append([key,[value]])
        for i in range(len(self.tab[index])):
            if self.tab[index][i][0] == key:
                self.tab[index][i][1] =  [value]
    
    def _append(self,key,value):
        index = self._hash(key)
        if len(self.tab[index]) == 0:
            self.tab[index].append([key,[value]])
            return
        for i in range(len(self.tab[index])):
            if self.tab[index][i][0] == key:
                self.tab[index][i][1].append(value)
                return
        #jesli nie znajdziemy klucza, czyli doszlo do kolizji!
        self.tab[index].append([key,[value]])
    
    def _get(self,key):
        index = self._hash(key)
        for i in range(len(self.tab[index])):
            if self.tab[index][i][0] == key:
                return self.tab[index][i][1]
        return None
    
    def _traverse(self):
        for i in range(len(self.tab)):
            for elem in self.tab[i]:
                print((elem[0]," ->",elem[1]))
        print()
        for i in range(len(self.tab)):
            print(self.tab[i])
    

def init_Graph(G):
    Graph = slownik(len(G)*2)
    for u,v in G:
        Graph._append(u,v)
        Graph._append(v,u)
    Graph._traverse()



#mamy postac krawedziową grafu nieskierowanego typu [[ui, vi],[uj,vj]] z ui dochodzi do vi i vice versa 

G =[[1,2],[3,4],[2,5],[44,800],[67,2],[99,5]]

init_Graph(G)