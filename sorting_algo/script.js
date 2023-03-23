//bubble sort (optimalization)

//O(n^2) - worst & average case
//O(n) - best case - gdy jest w wiekszosci posortowana to super dziala
function bubbleSort(arr){
    let flag;
    for(let i = 0; i < arr.length; i++){
        flag = true;
        for(let j=0; j < arr.length-i-1; j++){ //we don't need to checking elements all the way along,
            // because over time, more and more items from the end are sorted
            if(arr[j] > arr[j+1]) {
           [arr[j],arr[j+1]] = [arr[j+1], arr[j]];
           flag = false; //dokonalismy zamiany 
        }
        }
        if(flag) break; //jesli nie ma zamiany zadnej, poprostu skoncz dzialanie
    }
    return arr;
}
//console.log(bubbleSort([1,2,3,4,1]))
//na ogol lepiej nie uzywac, a napewno nie na asd i w pracy czy cos...
//sa lepsze algorytmy, ten jest najprostrzy



//O(n^2)
//wydajny dla niewielkiej ilosci elementow! (wynika z funkcji n^2)
//jedyny z 3 podstawowych algorytmow ktory zawsze bedzie mial O(n^2)
function selectionSort(arr){
    let lowest;
    for(let i = 0; i< arr.length-1; i++){ //konczymy na przedostatnim i porownanie z ostatnim
        lowest = i;
        for(let j = i+1;j<arr.length;j++){
            if(arr[lowest] > arr[j]) lowest = j;
        }
        if(lowest !== i) [arr[lowest], arr[i]] = [arr[i], arr[lowest]];
    }
    return arr;
}
//console.log(selectionSort([6,33,55,22,11,4,5,42,5,7,43,2,5,-59,21,32]))

//insertion sort
// jesli dane sa prawie wszystkie posortowane, to jest podobne do O(n)
//w najgorszym przypadku jest w O(n^2)
//najlepszy z tych trzech jesli juz uzywac
// dziala dobrze jesli musimy na zywo tablice uzupelniac o nowe elementy!
function insertionSort(arr){
    let chosen;
    let flag;
    for(let i = 1; i<arr.length;i++){     
        flag = false;
        j = i-1;
        chosen = arr[i];
        while((j >=0) && (arr[j] > chosen)){   
            flag = true;
            arr[j+1] = arr[j];
            j--; //z tego wzgledu potem musimy zamienic elem pod indeksem o 1 wiekszym niz j
        }
        if(flag === true) arr[j+1] = chosen;      
    }
    return arr;
}

//console.log(insertionSort([3,4,78,1,64,34,27,89,9]))



//quicksort (iteracyjnie!!)
function quicksort(arr){
    let stack = [];
    stack.push([0,arr.length-1]); //pierwsze indeksy - lewy i prawy
    let left,right,l,r,pivot,tuple;
    while(stack.length>0){
        tuple = stack.pop();
        left = tuple[0];
        right = tuple[1];
        l = left;
        r = right;
        pivot = arr[Math.floor((left + right)/2)]; //element w tablicy a nie sam index!
        while(l <= r){
            while(arr[l] < pivot) l++;
            while(arr[r] > pivot) r--;
            if(l <= r) {
                [arr[l], arr[r]] = [arr[r],arr[l]];
                l++;
                r--;
            }
        }
        //wyjscie za petle     
        if(left < r) stack.push([left,r]); //kolejne przedzialy
        if(l < right) stack.push([l,right]); //kolejne przedzialy

    }
    return arr;
}
//console.log(quicksort([6,33,55,22,11,4,5,42,5,7,43,2,5,-59,21,32]))

//merge sort!
//merge sort better for linked lists than quicksort, 
// memory is in O(n)!
//time is in O(nlogn)

//function which will be merging arrays in one sorted array!
//recursion
function merge(arr1,arr2){
    let results = [];
    let i = 0;
    let j = 0;
    while(i < arr1.length && j < arr2.length){
        if(arr1[i] < arr2[j]){
            results.push(arr1[i])
            i++;
        }
        else{
            results.push(arr2[j])
            j++
        }
    }
    while(i < arr1.length){
        results.push(arr1[i])
        i++;
    }
    while(j < arr2.length){
        results.push(arr2[j])
        j++;
    }
    return results;
}
function mergeSort(arr){
    if(arr.length <= 1) return arr;
    let mid = Math.floor(arr.length/2);
    let left = mergeSort(arr.slice(0,mid));
    let right = mergeSort(arr.slice(mid));
    return merge(left,right);
}

console.log(mergeSort([6,33,55,22,11,4,5,42,5,7,43,2,5,-59,21,32]))

//iteration

const mergeSortIt = (arr) => {
    //Create array for sorting - a dokladnie na aktualizowanie wartosci! 
    //petla wewnetrzna aktualizuje elementy od poczatku do konca w tablicy buffer
    //nim wrocimy do zewnetrznej petli trzeba zamienic wartosci tablic arr i buffer
    //let sorted = Array.from(arr);
    let n = arr.length;
    let buffer = new Array(n);
    let left,right,leftLimit,rightLimit;
    for (let size = 1; size < n; size *= 2) {
      for (let leftStart = 0; leftStart < n; leftStart += 2*size) {
        
        //Get the two sub arrays
            left = leftStart; //left & leftlimit - jedna podtablica
            right = Math.min(left + size, n);//jesli right == n to rightlimit tez == n wiec w merge sie nie wykonaja pewne czesci kodu
            leftLimit = right;
            rightLimit = Math.min(right + size, n); //right & rightlimit - druga podtablica
        
        //Merge the sub arrays
        mergeIt(left, right, leftLimit, rightLimit, arr, buffer);  
      }
      // w funkcji mergeIt ZAWSZE do tablicy "buffer" aktualizujemy WSZYSTKIE wartosci z tablicy "sorted"!!
      //dlatego wlasnie musimy zamienic teraz wartosci z tablic sorted i buffer!
      //w przeciwnym  wypadku nasza tablica sorted NIGDY by sie nie zaktualizowala!
      [buffer,arr] = [arr,buffer];
      
    }
    
    return arr;
  }

  //tutaj zawsze do tablicy "buffer" wstawiamy wartosci z tablicy "sorted"!!
  const mergeIt = (left, right, leftLimit, rightLimit, sorted, buffer) => {
    let i = left; //wskaznik i bedzie caly czas szedl do przodu!
    
    //Compare the two sub arrays and merge them in the sorted order
    while (left < leftLimit && right < rightLimit) {//nigdy left nie wejdzie na right
      if (sorted[left] < sorted[right]) {
        buffer[i++] = sorted[left++]; // i++ oraz left ++ wykona sie po podstawieniu
      } else {
        buffer[i++] = sorted[right++];
      }
    }
  
    //If there are elements in the left sub arrray then add it to the result
    while (left < leftLimit) {
      buffer[i++] = sorted[left++];
    }
  
    //If there are elements in the right sub array then add it to the result
    while (right < rightLimit) {
      buffer[i++] = sorted[right++];
    }
  }

//Time complexity: O(NlogN).
//Space complexity: O(N).
//random array

randomArray = (length, max) => [...new Array(length)]
    .map(() => Math.round(Math.random() * max));
arr = randomArray(10000000,1);

//console.log(mergeSort(arr));
//console.log(mergeSortIt(arr));
//iterational version of mergesort is faster!

//radixsort
//3 helper functions

//time complexity: O(nk) - best, O(nk) - average, O(nk) - worst
//space complexity: O(n+k)
//where: k - number of digits
// n - length of  array

function mostDigits(nums){
    let maxDig = 0;
    for(let i =0; i< nums.length;i++){
        maxDig = Math.max(maxDig, digCount(nums[i]));
    }
    return maxDig;
}
function getDigit(num,pos){
    return Math.floor(Math.abs(num)/Math.pow(10,pos))%10;
}
function digCount(num){
    if(num === 0) return 1;
    return Math.floor(Math.log10(Math.abs(num)))+1;
}
console.log(digCount(8));
function radixsort(arr){
    let longest = mostDigits(arr); 
    let k; //przyda sie do przepisywania wartosci
    for(let p = 0; p<longest;p++){ //zwiekszanie pozycji liczby
        let digitBuckets = Array.from({length: 10}, () => []); //tablica 10-elementowa zawiera puste listy na kazdej pozycji
        for(let i = 0; i<arr.length;i++){ //iterowanie po tablicy
            digitBuckets[getDigit(arr[i],p)].push(arr[i]);
        }
        //teraz mozemy przepisac elementy w nowej kolejnosci do oryginalnej tablicy
        /*k = 0;
        for(let i = 0; i < 10; i++){
            while(digitBuckets[i].length>0){
                arr[k] = digitBuckets[i].shift();
                k++;
            }
        } */
        arr = [].concat(...digitBuckets);
}
    return arr;
}


console.log(quicksort(arr))
