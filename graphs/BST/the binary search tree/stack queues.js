//na podstawie SLL:

class Node{
    constructor(val){
        this.val = val;
        this.next = null;
    }
}
//LAST IN FIRST OUT
class Stack { //push & pop są jak shift i unshift zeby czas byl staly (w STLL shift i unshift maja O(1) )
    constructor(){
        this.first = null;
        this.last = null;
        this.size = 0;
    }
    push(val){
        let newNode = new Node(val);
        if(this.first == null){
            this.first = newNode;
            this.last = this.first;
        }
        else{
            //let oldFirst = this.first;
            //this.first = newNode;
            //this.first.next = oldFirst;
            //alternatywnie: (chyba lepsze)
            newNode.next = this.first; //newNode bedzie wskazywać na dotychczasową głowę
            this.first = newNode; // obecną głową teraz bedzie newNode
        }
        this.size++;
        return this.size;
    }
    
    pop(){
        if(!this.first){
            return null;
        }
        let oldFirst = this.first;
        this.first = oldFirst.next;
        oldFirst.next = null;
        this.size--;
        if(this.size === 0){
            this.first = null;
            this.last = null;
        }
        return oldFirst.val;

        /* alternatywnie:
        if(!this.first) return null;
        let temp = this.first;
        if(this.first === this.last){
            this.last = null;
        }
        this.first = this.first.next;
        this.size--;
        return temp.val;
        */
    }
    traverse(){
        let curr = this.first;
        while(curr != null){
            console.log(curr.val);
            curr = curr.next;
        }
    }
    empty(){
        if(!this.head) return True;
        return False
    }
}


//QUEUES!
//FIRST IN FIRST OUT
class Queue {
    constructor(){
        this.first = null;
        this.last = null;
        this.size = 0;
    }
    enqueue(val){ //jak push w SLL -> put
        let newNode = new Node(val);
        if(!this.first){
            this.first = newNode;
            this.last = this.first;
        }
        else{
            this.last.next = newNode; //kolejny element za obecnym ogonem bedzie nie nullem a nowym wezlem!
            this.last = newNode; //mamy nowy ogon, musimy ustawic nowy ogon na ten ostatni wezeł!
        }
        this.size++;
        return this.size;
    }
    dequeue(){ //jak shift w SLL -> get
        if(!this.first){
            return null;
        }
        let oldFirst = this.first;
        this.first = oldFirst.next;
        oldFirst.next = null;
        this.size--;
        if(this.size === 0){
            this.first = null;
            this.last = null;
        }
        return oldFirst.val;

        /* alternatywnie:
        if(!this.first) return null;
        let temp = this.first;
        if(this.first === this.last){
            this.last = null;
        }
        this.first = this.first.next;
        this.size--;
        return temp.val;
        */
    }
    traverse(){
        let curr = this.first;
        while(curr != null){
            console.log(curr.val);
            curr = curr.next;
        }
    }
    empty(){
        if(!this.head) return True;
        return False
    }
}

let stack = new Stack();
let queue = new Queue();