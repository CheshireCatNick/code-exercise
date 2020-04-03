const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let state = 'testCase';
let totalTestCase;
let testCase = 1;

rl.on('line', (line) => {
    switch (state) {
    case 'testCase':
        totalTestCase = parseInt(line);
        state = 'readN';
        break;
    case 'readN':
        solve(line);
        testCase++;
        if (testCase === totalTestCase + 1) rl.close();
        break;
    }
});

function removeZero(s) {
    let i = 0;
    while (i < s.length && s[i] === '0') i++;
    return s.slice(i, s.length);
}
function solve(n) {
    let B = '';
    let A = '';
    for (let char of n) {
        if (char !== '4') {
            A += char;
            B += '0';
        }
        else {
            A += '3';
            B += '1';
        }
    }
    B = removeZero(B);
    console.log(`Case #${testCase}: ${A} ${B}`);
}

