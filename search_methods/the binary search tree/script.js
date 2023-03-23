class Node_bin {
    constructor(value){
        this.value = value;
        this.left = null;
        this.right = null;
        //dodatek:
        this.count = 1;
    }
}


class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    insert(value){
        let newNode = new Node_bin(value);
        if(this.root === null){
            this.root = newNode;
            return this;
        }
        else{
            let current = this.root;
            while(true){
                if(value === current.value){
                    current.count++;
                    return this;
                }
                if(value < current.value){
                    if(current.left === null){
                        current.left = newNode;
                        return this;
                    }else{
                        current = current.left; //zmierzamy do lewego rozgalezienia i tam bedziemy ponownie rozpatrywać wartosc zadaną w current.left (aktualnie wiemy ze tam jest wartosc!)
                    }
                    
                }else if(value > current.value){
                    if(current.right === null){
                        current.right = newNode;
                        return this;
                    }else{
                        current = current.right;
                    }
                }
            }
        }
    }
    //koniec insertu
    find(value){
        if(this.root === null) return false;
        else{
            let current = this.root;
            while(current != null){
                if(value < current.value){
                    current = current.left; //zmierzamy do lewego rozgalezienia i tam bedziemy ponownie rozpatrywać wartosc zadaną w current.left (aktualnie wiemy ze tam jest wartosc!)      
                }else if(value > current.value){
                    current = current.right;  
                } else{
                    return true;
                }
            }
            return false;
        }
    }
    //tree traversal
    depthFirstSearch_preOrderREK(){
        let curr = this.root;
        function rek(curr){
            if(curr !== null){
                console.log(curr.value);
                rek(curr.left);
                rek(curr.right);
                //w przeciwienstwie do wersji iteracyjnej,
                //bedziemy szli od lewej do prawej przy takiej
                //kolejnosci jak przy BFS (queue) 
                
            }   
        }
        rek(curr); 
    }
    depthFirstSearch_preOrder(){
        //let data = [];
        let curr = this.root;
        let stos = [];
        if(curr != null) stos.push(curr);
        while(stos.length > 0){
            curr = stos.pop();
            console.log(curr.value);
            //data.push(curr)
            if(curr.right != null) stos.push(curr.right);
            if(curr.left != null) stos.push(curr.left);
            //ta kolejnosc sprawi ze najpierw sprawdzi lewe rozgalezienia, i potem prawe!!
            //odwrotna kolejnosc ifow sprawi ze najpierw prawe potem lewe (zgodnie z dzialaniem stosu)
            

        }
        //return data
    }

    depthFirstSearch_postOrderREK(){
        let curr = this.root;
        function rek(curr){
                if(curr.left) rek(curr.left);
                if(curr.right) rek(curr.right);
                console.log(curr.value); 
        }
        rek(curr); 
    }


    depthFirstSearch_postOrder(){ //tu juz niestety trzeba zrobic tablice zapamietujaca elementy
        let data = [];
        let curr = this.root;
        let stos = [];
        if(curr != null) stos.push(curr);
        while(stos.length > 0){
            curr = stos.pop();
            //console.log(curr.value);
            data.unshift(curr.value) //bedziemy od konca je czytac, wiec najlepiej w ten sposob zaimportowac do tablicy
            if(curr.left != null) stos.push(curr.left);
            if(curr.right != null) stos.push(curr.right);  
            //jak widac, w preOrder, zeby przejsc z lewej do prawej musielibysmy najpierw dac prawego ifa a potem lewego! (bo stos tak dziala)
            //ale tutaj robimy unshifta do tablicy data, robimy odwrotną kolejnosc ze wzgledu na to wiec ify porzadkujemy jak przy kolejce w Breath First Search!
        }
        return data
    }
    
    depthFirstSearch_inOrderREK(){
        let curr = this.root;
        function rek(curr){
                if(curr.left) rek(curr.left);
                console.log(curr.value); //i to juz dziala! wypisze wszystko po kolei uporzadkowane!
                if(curr.right) rek(curr.right);
                
        }
        rek(curr); 
    }

    
    
    
    //Breath First Search approach:
    //we want to visit every single node on the same level! 
    //before we look at the child
    // we work horizontally:
    breadthFirstSearch(){
        let queue=[], 
        node=this.root;
        //let data = [];
        queue.push(node);
        while(queue.length){
            node = queue.shift()
            //data.push(node);
            console.log(node.value);
            if(node.left) queue.push(node.left)
            if(node.right) queue.push(node.right)
            //kolejnosc: najpierw if "lewy" potem "prawy" sprawia, ze bedzie szlo od lewej do prawej poziomo
            //odwrotna kolejnosc da przeciwny rezultat tzn, z prawej do lewej poziomo
        }
        //return data;
    }

}

let tree = new BinarySearchTree();
tree.insert(10);
tree.insert(6);
tree.insert(15);
tree.insert(3);
tree.insert(8);
tree.insert(20);


tree.depthFirstSearch_preOrder();
console.log("---");
tree.breathFirstSearch();
console.log("--- POSTORDER DFS: (rekurencyjnie): ");
tree.depthFirstSearch_postOrderREK();
console.log("--- POSTORDER DFS: (iteracyjnie): ");
console.log(tree.depthFirstSearch_postOrder());
console.log("--- INORDER DFS: (rek): ");
tree.depthFirstSearch_inOrderREK();
