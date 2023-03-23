//max/min binary heap:
/*
- each parent has at most two child nodes 
- the value of each parent node is always greater tham its child nodes
- in a max Binary Heap the parent is greater than the children, 
but there are no guarantees between sibling nodes.
- a binary heap is as compact as possible. All the children of each node are 
as full as they can be and left children are filled out first
- in min binary heaps the smallest element in on the top and larger are below
- first we fill the left child and then the right child
- why do we need to know this?
 >binary heaps are used to implement Priority Queues, which are very commonly used data structures
 >used quite a bit, with graph traversal algorithms


 // FOR ANY INDEX OF AN ARRAY N...
 // the left child is stored at 2n + 1
 //the right child is at 2n + 2

 //for any child node at index n...
 //its parent is at index (n-1)/2 floored
*/

//priority queue:
/* 
A data structure where each element has a priority.
Elements with higher priorities are served before 
elements with lower priority

// binaryHeaps:
/*
insertion - O(logN)
Removal - O(logN)
Search - O(N)

*/


class MaxBinaryHeap{
    constructor(){
        this.values = [];
    }

    insert(val) {
        const values = this.values;//dla uproszczenia w zapisie
        values.push(val);
        let idx = values.length - 1;
        let parentIdx = Math.floor((idx - 1) / 2);
     
        // Bubbling up
        while (parentIdx >=0 &&  values[idx] > values[parentIdx]) {
            [values[idx], values[parentIdx]] = [values[parentIdx], values[idx]];
            idx = parentIdx; 
            parentIdx = Math.floor((idx - 1) / 2); //Math.floor(0-1/2) == -1 !!
        }
        return this;
    }
    
    extractMax(){
        //najpierw musimy element ostatni wlozyc na pierwsze miejsce (ofc do tego usunac ostatnie polozenie) i w petli odpowiednio odnalezc jego miejsce
        if(this.values.length ===0) return null;
        const values = this.values;
        const max = values[0]; //zmienna popped bedzie zwracana
        values[0] = values[ values.length-1];
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

            if(leftChildIdx < length){
                leftChild = values[leftChildIdx];
                if(leftChild > element){
                    swap = leftChildIdx;
                }
            }
            if(rightChildIdx < length){
                rightChild = values[rightChildIdx];
                if((swap === null && rightChild > element) ||
                    (swap ==! null && rightChild > leftChild)
                    ){
                    swap = rightChildIdx;
                }
            }
            if(swap === null) break; //oznacza to ze element jest na prawidlowym miejscu
            values[idx] = values[swap];
            values[swap] = element;
            idx = swap;
        }  
     return max;
    }
}

let heap = new MaxBinaryHeap();
heap.insert(41);
heap.insert(39);
heap.insert(33);
heap.insert(18);
heap.insert(27);
heap.insert(12);
heap.insert(55);
heap.extractMax();

//PRIORITY QUEUE:

class PriorityQueue{
    constructor(){
        this.values = [];
    }

    enqueue(val,priority) { //insert ,jesli chcemy aby najwyzszy priorutet == najnizsza liczba -> zmien znaki nierownosci
        let newNode = new Node(val,priority);
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
class Node {
    constructor(val,priority){
        this.val =val;
        this.priority = priority;
    }
}

let ER  = new PriorityQueue();
ER.enqueue("common cold",5);
ER.enqueue("gunshot wound",1);
ER.enqueue("high fever",4);
ER.enqueue("broken arm",2);
ER.enqueue("glass in foot",3);

/* Simpler PriorityQueue: */

class SimplePriorityQueue {
    construtor(){
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
        this.values.sort((a,b) => a.priority - b.priority);
    };
}

q = new PriorityQueue();
q.enqueue("A",0);
q.enqueue("B",1);
q.enqueue("C",8);
q.enqueue("D",6);
q.enqueue("E",4);
q.enqueue("F",7);