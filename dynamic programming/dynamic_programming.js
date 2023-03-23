/* Dynamic programming - a method for solving complex problem by breaking it down into a collection of simpler
subproblems, solving each of those subproblems JUST ONCE, and storing their solutions. */

/*
Overlapping subproblems - a problem is said to have overlapping subproblems if it can be broken down into
subproblems which are reused several times

optimal subproblems - a problem is said to have optimal substructure if an optimal solution can be
constructed from optimal solutions of its subproblems
 */

//BIG O notation: O(2^n)
function worst_fib(n){
    if(n<=2) return 1;
    return worst_fib(n-1) + worst_fib(n-2);
}

//a memo-ized solution
//Big O notation: O(N)
//top-down approach
function memo_fib(n,memo=[undefined,1,1]){
    if(memo[n] !== undefined) return memo[n];
    //if(n<=2) return 1; //mozemy sie tego pozbyc wsm bo base case zawarty w memo!
    let res = memo_fib(n-1,memo) + memo_fib(n-2,memo);
    memo[n] = res;
    return res;
}
//O(N)
function iter_fib(n){
    let a=1,b=1;
    for(let i = 3; i <= n;i++){
        [a,b] = [b,a+b];
    }
    return b;
}

//tabulated version:
// a bottom-up approach
//O(N)
function list_fib(n){
    if(n<=2) return 1;
    let fibNums = [0,1,1];
    for(let i = 3; i <=n; i++){
        fibNums[i] = fibNums[i-1] + fibNums[i-2]; 
    }
    return fibNums[n];
}