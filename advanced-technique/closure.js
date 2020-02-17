'use strict';
// basic closure
function createCounter() {
    let count = 0;
    return function add() {
        count++;
        return count;
    };
}
const counter = createCounter();
console.log(counter(), counter(), counter());
const counter1 = createCounter();
console.log(counter1(), counter1(), counter1());

// interesting questing
let arr = [];
for (var i = 0; i < 5; i++) {
    arr.push(() => console.log(i));
}
arr[0](); // 5
arr[1](); // 5
// use let for block variable scope
arr = [];
for (let i = 0; i < 5; i++) {
    arr.push(() => console.log(i));
}
arr[0](); // 0
arr[1](); // 1
// use closure
function log(n) {
    return function() { console.log(n) };
}
arr = [];
for (var i = 0; i < 5; i++) {
    arr.push(log(i));
}
arr[0](); // 0
arr[1](); // 1

// example: use closure to protect variable
function createWallet(balance) {
    return {
        add: () => { balance++; },
        decrease: () => { balance--; },
        show: () => { console.log(balance); }
    };
}
const wallet = createWallet(30);
wallet.show();
wallet.add();
wallet.add();
wallet.show();
wallet.decrease();
wallet.show();

// example: use closure to create cache for a function
function createCachedFunction(f) {
    const cache = {};
    return (param) => {
        if (cache[param] === undefined) return cache[param] = f(param);
        else return cache[param];
    };
}
function compute(n) {
    console.log('computing...');
    return n * 2;
}
const cachedCompute = createCachedFunction(compute);
console.log(cachedCompute(100)); // will have 'computing...'
console.log(cachedCompute(100)); // will not have 'computing...'