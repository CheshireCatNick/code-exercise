// !!! must be nodejs v11.7 and above
'use strict';
const readline = require('readline');
const rl = readline.createInterface({ 
    input: process.stdin, 
    output: process.stdout
});
const getLine = (function () {
    const getLineGen = (async function* () {
        for await (const line of rl) {
            yield line;
        }
    })();
    return async () => ((await getLineGen.next()).value);
})();
// read as an array of int
async function RI() {
    return (await getLine()).split(' ').map(e => Number(e));
}
// read as an array of string
async function RS() {
    return (await getLine()).split(' ');
}

(async function main() {
    let a;
    a = await RS();
    console.log(a);
    const n = a[0], m = a[1];
    console.log(n, m);
    process.exit(0);
})();