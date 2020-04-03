const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let state = 'testCase';
let totalTestCase;
let testCase = 1;
let n, numbers;

rl.on('line', (line) => {
    switch (state) {
    case 'testCase':
        totalTestCase = parseInt(line);
        state = 'readN';
        break;
    case 'readN':
        n = parseInt(line);
        state = 'readNumbers';
        break;
    case 'readNumbers':
        numbers = line.split(' ').map(ns => parseInt(ns));
        solve(n, numbers);
        testCase++;
        if (testCase === totalTestCase + 1) rl.close();
        state = 'readN';
        break;
    }
});

function solve(n, numbers) {
    
    console.log(`Case #${testCase}: ${plainText}`);
}

