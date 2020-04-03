/**
 * @param {string} s
 * @return {string}
 */
const gc = s => s.charCodeAt(0) - 'a'.charCodeAt(0);
const gChar = n => String.fromCharCode('a'.charCodeAt(0) + n);
var sortString = function(s) {
    let ans = '';
    const state = new Array(26).fill(0);
    for (let c of s) {
        state[gc(c)]++;
    }
    console.log(state);
    while (true) {
        let hasOp = false;
        for (let i = 0; i < 26; i++) {
            if (state[i] > 0) {
                ans += gChar(i);
                state[i]--;
                hasOp = true;
            }
        }
        for (let i = 25; i >= 0; i--) {
            if (state[i] > 0) {
                ans += gChar(i);
                state[i]--;
                hasOp = true;
            }
        }
        if (!hasOp) break;
    }
    return ans;
};

console.log(sortString('aaaabbbbcccc'));