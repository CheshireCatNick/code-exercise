'use strict';

const n = 3;
let s = '';
for (let i = 1; i <= n; i++) {
    s += i;
}
const count = [];
for (let i = 0; i <= 9; i++) {
    count.push(0);
}
for (let i = 0; i < s.length; i++) {
    console.log(s.charAt(i));
    count[parseInt(s.charAt(i))]++;
}
console.log(count);