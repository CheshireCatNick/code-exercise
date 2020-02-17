'use strict';

function c() {
    let a = 0;
    return function add() {
        a++;
        console.log(a);
        return a;
    }
}

const add = c();
console.log(add(), add(), add());
const add1 = c();
console.log(add1(), add1(), add1());
