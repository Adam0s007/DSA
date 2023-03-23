/*
One of the most famous and widely used algorithms around
Finds the shortest path between two vertices on a graph

*/

/*
"A" = [{node: "B", weight: 10}]

*/

/*
DIJKSTRA ALGO: (APPROACH)
1. Every time we look to visit a new node, we pick the node with the smallest known distance to visit first
2. Once we've moved to the node we're going to visit, we look at each of its neighbors
3. For each neighboring node, we calculate the distance by summing the total edges that lead to the node
we're checking from the starting node.
4. If the new total distance to a node is less than the parent total, we store the new, 
shorter distance for that node

*/


class WeightedGraph {
    constructor() {
        this.adjacencyList = {};
    }
    addVertex(vertex){
        if(!this.adjacencyList[vertex]) this.adjacencyList[vertex] = [];    
    }
    addEdge(v1,v2,weight){
        
        if(!this.adjacencyList[v1].includes(v2)) this.adjacencyList[v1].push({node:v2,weight});
        if(!this.adjacencyList[v2].includes(v1)) this.adjacencyList[v2].push({node:v1,weight});
    }
    Dijkstra(start,finish){ //nodes
        const nodes = new PriorityQueue();
        const distances = {};
        const parent = {};
        let smallest;
        let path = []; //to return at end
        //building up initial state
        for(let vertex in this.adjacencyList){
            if(vertex === start){
                distances[vertex] = 0;
                nodes.enqueue(vertex,0);
            }else{
                distances[vertex] =Infinity;
                nodes.enqueue(vertex,Infinity);
            }  
            parent[vertex] = null;
        }
        //as long as there is sth to visit
        while(nodes.values.length){
            smallest = nodes.dequeue().val; // "A", "B" itd.
            if(smallest === finish){
                //WE ARE DONE
                //BUILD UP PATH TO RETURN AT END
                while(parent[smallest]){ // w koncu bedzie nullem i petla sie zakonczy
                    path.push(smallest);
                    smallest = parent[smallest];
                }
                return [path.concat(smallest).reverse(),distances[finish]];
                break; // poniewaz node.values.length moze byc rozne od zera!!
            }
        
                for(let neighbor in this.adjacencyList[smallest]){//neighbor to typ number
                    //find neighboring node
                    let nextNode = this.adjacencyList[smallest][neighbor];
                    //calculate new distance to neightboring node
                    let candidate = distances[smallest] + nextNode.weight;
                    if(candidate < distances[nextNode.node]){
                        //updating new smallest distance to neighbor
                        distances[nextNode.node] = candidate;
                        //updating parent - how we got to neighbor
                        parent[nextNode.node] = smallest;
                        //enqueue in priority queue with new priority
                        nodes.enqueue(nextNode.node,candidate);
                    }
                }
            
        }


    }

}



class SimplePriorityQueue {
    constructor(){
        this.values = [];
    }
    enqueue(val,priority){
        this.values.push({val,priority});
        this.sort();
    };
    dequeue() {
        return this.values.shift();
    };
    sort() {
        this.values.sort((a,b) => a.priority - b.priority); //O(nlogn)
    };
}
class PriorityQueue{
    constructor(){
        this.values = [];
    }

    enqueue(val,priority) { //insert ,jesli chcemy aby najwyzszy priorutet == najnizsza liczba -> zmien znaki nierownosci
        let newNode = {val,priority};
        const values = this.values;//dla uproszczenia w zapisie
        values.push(newNode);
        let idx = values.length - 1;
        let parentIdx = Math.floor((idx - 1) / 2);

        // Bubbling up
        while (parentIdx >=0 &&  values[idx].priority < values[parentIdx].priority) { // <
            [values[idx], values[parentIdx]] = [values[parentIdx], values[idx]];
            idx = parentIdx; 
            parentIdx = Math.floor((idx - 1) / 2); //Math.floor(0-1/2) == -1 !!
        }
        return this;
    }
    
    dequeue(){ //extractMax  , jesli chcemy aby najwyzszy priorytet == najnizsza liczba -> zmien znaki nierownosci
        if(this.values.length ===0) return null;
        const values = this.values;
        const max = values[0]; //zmienna popped bedzie zwracana , zamien na min jesli zmienisz zn. nierownosci
        values[0] = values[values.length-1];
        let p = values.pop(); //to usuwamy juz na dobre
        if(values.length === 0) return max;
        
        const length = values.length;
        const element = values[0];
        let idx = 0;
        //trickle down
        while(true){
            let leftChildIdx = 2*idx + 1;
            let rightChildIdx = 2*idx + 2;
            let leftChild,rightChild;
            let swap = null;
            //moznaby tu robic mnostwo roznych ifow uwzgledniajac sytuacje, albo podejsc sprytniej z uzyciem zmiennej swap
            if(leftChildIdx < length){ 
                leftChild = values[leftChildIdx];
                if(leftChild.priority < element.priority){ // <
                    swap = leftChildIdx;
                }
            }
            if(rightChildIdx < length){ 
                rightChild = values[rightChildIdx];
                if((swap === null && rightChild.priority < element.priority) || // <
                    (swap ==! null && rightChild.priority < leftChild.priority) // <
                    ){
                    swap = rightChildIdx;
                }
            }
            if(swap === null) break;
            values[idx] = values[swap];
            values[swap] = element;
            idx = swap;
        }  
     return max;
    }
}



let graph = new WeightedGraph();
graph.addVertex("A");
graph.addVertex("B");
graph.addVertex("C");
graph.addVertex("D");
graph.addVertex("E");
graph.addVertex("F");

graph.addEdge("A","B",4);
graph.addEdge("A","C",2);
graph.addEdge("B","E",3);
graph.addEdge("C","D",2);
graph.addEdge("C","F",4);
graph.addEdge("D","E",3);
graph.addEdge("D","F",1);
graph.addEdge("E","F",1);

