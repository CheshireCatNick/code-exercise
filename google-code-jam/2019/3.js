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

function factorize(n) {
    if (n % 2 === 0) return 2;
    for (let i = 3; i < n; i += 2) {
        if (n % i === 0) return i;
    }
}

function gcd(a, b) {
    while (b !== 0) {
        let t = a % b;
        a = b; 
        b = t;
    }
    return a;
}

function solve(n, numbers) {
    const pickedPrimes = new Set();
    let i = 0;
    while (numbers[i] === numbers[i + 1]) {
        i++;
    }
    let next = gcd(numbers[i], numbers[i + 1]);
    let prev = numbers[i] / next;
    pickedPrimes.add(prev);
    pickedPrimes.add(next);
    if (i % 2 !== 0) {
        const t = prev;
        prev = next;
        next = t;
    }
    let plainNumbers = [];
    plainNumbers.push(prev);
    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] === numbers[i - 1]) {
            const t = prev;
            prev = next;
            next = t;
            plainNumbers.push(prev);
            continue;
        }
        prev = next;
        next = numbers[i] / prev;
        plainNumbers.push(prev);
        pickedPrimes.add(next);
    }
    plainNumbers.push(next);
    const array = Array.from(pickedPrimes).sort((a, b) => a - b);
    let plainText = '';
    plainNumbers.forEach(number => 
        plainText += String.fromCharCode('A'.charCodeAt(0) + array.indexOf(number))
    );
    console.log(`Case #${testCase}: ${plainText}`);
}

