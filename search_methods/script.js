//linear search
function linearSearch(arr,val){
    for(let i = 0; i< arr.length;i++){
        if(arr[i] == val) return i;
        
    }
    return -1
}

//binary search  - recursion
function binarySearch_rec(arr,val,left=0,right=arr.length-1){
    let middle = Math.floor((left + right)/2);
    if (arr[middle] == val) return middle;
    if(left > right){
        return -1;
    }
    else if(arr[middle] > val){
        return binarySearch_rec(arr,val,left,middle-1);
    }
    else {
        return binarySearch_rec(arr,val,middle+1,right);
    }
}

//binary search - without recursion - much quicker

function binarySearch(arr,val){
    let right = arr.length -1;
    let left = 0;
    let middle = Math.floor((left+right)/2);
    if (arr[middle] == val){
        return middle;
    }
    while(arr[middle] != val && left <= right){
        if (arr[middle] > val) right = middle - 1;           
        else left = middle + 1;
        middle = Math.floor((left+right)/2);  
    }
    return arr[middle] == val ? middle: -1;
    
}

//naive search 
//find a quantity of repeating substring in a string
function naiveSearch(long,short){
    let count = 0
    for(let i = 0; i<long.length-short.length+1; i++){
        for(let j = 0; j < short.length; j++){
            if(short[j] !== long[j+i]) break
            if(j + 1 === short.length) count++
        }
    }
    return count;
}