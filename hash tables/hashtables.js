/*
> Hash tables are used to store key-value pairs.
>They are like arrays, but the keys are not ordered.
>Unlike arrays, hash tables are fast for all of the following 
operations:
 finding values (in LL & DLL it is O(n))
 adding new values (in LL: only push (when tail is given) & unshift are O(1))
 removing values (only shift in LL, pop in DLL are O(1))

Due to their speed, hash tables are very commonly used,
nearly every programming language has some sort of hash table data structure

Hash tables in programming languages:
Python: dictionaries
JS: Objects and Maps* (* Objects have some restrictions, but are basically hash tables)
Java, Go & Scala: Maps
Ruby: Hashes


To implement a hash table, we'll be using an array;
In order to look up values by key, we need a way to convert keys into valid array
indices.
A function that performs this task is called a hash function.


what makes a good hash? (not a cryptographically secure one):
1. Fast (i.e. constant time)
2. doesn't cluster outputs at specific indicates, but distributes uniformly
(nie grupuje danych wyjściowych w określonych wskazaniach, ale rozkłada się równomiernie)
3. Deterministic (same input yields same output)


Prime number in the hash is helpful in spreading out the keys more uniformly.
It's also helpful if the array that you're putting values into has a prime length.

https://www.geeksforgeeks.org/what-are-hash-functions-and-how-to-choose-a-good-hash-function/

Dealing with collisions (methods):
1. Separate Chaining 
2. Linear Probing



*/

//A HashTable Class

class HashTable {
    constructor(size=5){ //let size be a prime number
        this.keyMap = new Array(size);
    }
    _hash(key){
    let total = 0;
    let prime = 15485857;
    for(let i =0;i< Math.min(key.length,20); i++){
        let char = key[i];
        let value = char.charCodeAt(0) -96;
        total  =(total * prime + value) % this.keyMap.length; //metoda haszujaca
    }
    return Math.abs(total);
    }

    set(key,value){ //separate chaining method
        let index = this._hash(key);
        if(!this.keyMap[index]){
            this.keyMap[index] = [];
        }
        this.keyMap[index].push([key,value]);
    }
    get(key){
        let index = this._hash(key);
        if(this.keyMap[index]){
            for(let i =0; i < this.keyMap[index].length;i++){
                if(this.keyMap[index][i][0] === key){
                    return this.keyMap[index][i][1] //zwroci wartosc
                }
            }
        }
        return undefined;
    }
    keys(){
        let keysArr = [];
        for(let i = 0; i < this.keyMap.length; i++){
            if(this.keyMap[i]){
                for(let j = 0; j < this.keyMap[i].length; j++){
                    //aby pozbyc sie duplikatow //jesli chcemy zrobic tablice kluczy, to zmieniamy z 1 na 0
                    if(!keysArr.includes(this.keyMap[i][j][0])) keysArr.push(this.keyMap[i][j][0]);
                }
            }
        }
        return keysArr;
    }
    values(){
        let valArr = [];
        for(let i = 0; i < this.keyMap.length; i++){
            if(this.keyMap[i]){
                for(let j = 0; j < this.keyMap[i].length; j++){
                    //aby pozbyc sie duplikatow //jesli chcemy zrobic tablice kluczy, to zmieniamy z 1 na 0
                    if(!valArr.includes(this.keyMap[i][j][1])) valArr.push(this.keyMap[i][j][1]);
                }
            }
        }
        return valArr;
    }
    
    setUniq(key,value){ //separate chaining method
        let index = this._hash(key);
        if(!this.keyMap[index]){
            this.keyMap[index] = [];
            this.keyMap[index].push([key,value]);
            return true;
        }
        for(let i = 0; i < this.keyMap[index].length;i++){
            if(this.keyMap[index][i][0] === key) {
                this.keyMap[index][i][1] = value;
                return true;
            }
        }
        //jesli nie wykonaja sie zadne z powyzszych ifow to zrob to:
        this.keyMap[index].push([key,value]);
            return true;
        
    }

}


let ht = new HashTable();
ht.set("hello world", "goodbye!!");
ht.set("dogs", "are cool");
ht.set("cats", "are fine");
ht.set("i love", "pizza");
ht.set("cats", "are cool");
ht.set("lion", "789978");
ht.set("tiger", "5674764");
ht.set("human", "080979087");
ht.set("parrots", "778678");
ht.set("wolves", "6886");

    
/*
RECAP:
-Hash tables are collections of key-value pairs
-Hash tables can find values quickly given a key
-Hash tables can add new key-values quickly
-they store data in a large array, and work by hashing the keys
-a good hash should be fast, distribute keys uniformly, and be deterministic
*/ 
