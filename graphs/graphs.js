/*
weighted graph - edges with values!
unweighted graph - edges without values

---------------------------------------------

                    DIFFERENCES & BIG-O:
                    |V| - nr of vertices
                    |E| - nr of edges

    OPERATION       |   ADJACENCY LIST      |       ADJACENCY MATRIX
1)  add vertex      |   O(1)                |       O(|V^2|)         
2)  add edge        |   O(1)                |       O(1)
3)  remove vertex   |   O(|V| + |E|)        |       O(|V^2|)
4)  remove edge     |   O(|E|)              |       O(1)
5)  query           |   O(|V| + |E|)        |       O(1)
6)  storage         |   O(|V| + |E|)        |       O(|V^2|)

Adjacency List:
> Can take up less space (in sparse graphs)
> Faster to iterate over all edges
> Can be slower to lookup specific edge

Adjacency Matrix:
> Takes up more space (in sparse graphs)
> Slower to iterate over all edges
> Faster to lookup specific edge

*/

class Graph{ //undirected, unweighted - the simplest
    constructor(){
        this.adjacencyList = {}; //object
    }

    addVertex(vertex){
        if(!this.adjacencyList[vertex]){
            this.adjacencyList[vertex] = [];
            return this.adjacencyList[vertex];
        }
        return false;   
    }

    addEdge(v1,v2){
        
        if(!this.adjacencyList[v1].includes(v2)) this.adjacencyList[v1].push(v2);
        if(!this.adjacencyList[v2].includes(v1)) this.adjacencyList[v2].push(v1);
    }
    addEdgeOneWay(from_v1,to_v2){
        if(!this.adjacencyList[from_v1].includes(to_v2)) this.adjacencyList[from_v1].push(to_v2);
    }  
    
    removeConnectionOneWay(v1,offgoing_v2){
        this.adjacencyList[v1] = this.adjacencyList[v1].filter( (v)=> {
            return v !== offgoing_v2;
        });


    }
    removeEdge(v1,v2){
        this.adjacencyList[v1] = this.adjacencyList[v1].filter( (v)=> {
            return v !== v2;
        });
        this.adjacencyList[v2] = this.adjacencyList[v2].filter( (v)=> {
            return v !== v1;
        });
    }
    //ta wersja removeVertex dzialaja dla grafow nieskierowanych!!!
    removeVertex(v){
        if(this.adjacencyList[v]){ //jesli istnieje to...
            while(this.adjacencyList[v].length){
                const adjacentVertex = this.adjacencyList[v].pop();
                this.removeEdge(v,adjacentVertex);
            }
            delete this.adjacencyList[v];
        }
    }
    
    
    edgeSeparation(v1,v2,v){
        if(!this.adjacencyList[v1] || !this.adjacencyList[v2]) return false;
        let separate = (vertex1,vertex2,newVertex) => {
            this.addVertex(newVertex);
            for(let i = 0; i < this.adjacencyList[vertex1].length;i++){
                if(this.adjacencyList[vertex1][i] === vertex2) {
                    this.adjacencyList[vertex1][i] = newVertex;
                    break;
                }
            }
            this.adjacencyList[newVertex].push(vertex2);
        }
        //checking whether is there an edge, is it undirected or directed edge itd.
        if(!this.adjacencyList[v1].includes(v2) && !this.adjacencyList[v2].includes(v1)) return false //no edge
        else if(this.adjacencyList[v1].includes(v2) && !this.adjacencyList[v2].includes(v1)) separate(v1,v2,v) // v1 --> v2
        else if(!this.adjacencyList[v1].includes(v2) && this.adjacencyList[v2].includes(v1)) separate(v2,v1,v) // v2 --> v1
        else if(this.adjacencyList[v1].includes(v2) && this.adjacencyList[v2].includes(v1)){ // v1 <---> v2
            separate(v2,v1,v);
            separate(v1,v2,v);
        }
        return g;
    }

    depthFirstRek(start){
        const result = [];
        const visited = {};
        
        const dfs = (vertex) => {
            if(!vertex) return null;
            visited[vertex] = true;
            result.push(vertex);
            this.adjacencyList[vertex].forEach(neighbor => {
                if(!visited[neighbor]){
                    dfs(neighbor); //mozna dac return ale nie trzeba
                }
            })

        }
        dfs(start);
        return result
    }
    depthFirstIter(start){
        const result = [];
        const visited = {};
        const stack = [start];
        visited[start] = true;
        let vertex;
        while(stack.length > 0){
            vertex = stack.pop();
            result.push(vertex); 
            this.adjacencyList[vertex].forEach(neighbor => {
                if(!visited[neighbor]){
                    stack.push(neighbor);  
                    visited[neighbor] = true;
                }    
            })
        }
        return result;
    }
    breadthFirstIter(start){ //tu podobnie moznaby zastosowac zamiast stosu to kolejke (jak w BFS dla binary search)
        const result = [];
        const visited = {};
        const queue = [start];
        visited[start] = true;
        let vertex;
        while(queue.length > 0){
            vertex = queue.shift();
            result.push(vertex); 
            this.adjacencyList[vertex].forEach(neighbor => {
                if(!visited[neighbor]){
                    queue.push(neighbor);  
                    visited[neighbor] = true;
                }    
            })
        }
        return result;
    }
    

    
}
let g = new Graph();
g.addVertex("A");
g.addVertex("B");
g.addVertex("C");
g.addVertex("D");
g.addVertex("E");
g.addVertex("F");

g.addEdge("A","B");
g.addEdge("A","C");
g.addEdge("B","D");
g.addEdge("C","E");
g.addEdge("D","E");
g.addEdge("D","F");
g.addEdge("E","F");