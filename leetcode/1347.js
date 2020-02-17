/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
function count(str) {
    const map = Array(26).fill(0);
    for (let c of str) {
        map[c.charCodeAt(0) - 'a'.charCodeAt(0)]++;
    }
    return map;
}
var minSteps = function(s, t) {
    const sc = count(s), tc = count(t);
    let diff = 0;
    const abs = n => (n >= 0) ? n : -n;
    for (let i = 0; i < 26; i++) {
        diff += abs(sc[i] - tc[i]);
    }
    return diff / 2;
};

console.log(minSteps('bab', 'aba'));
console.log(minSteps('leetcode', 'practice'));
console.log(minSteps('anagram', 'mangaar'));
console.log(minSteps('xxyyzz', 'xxyyzz'));
console.log(minSteps('friend', 'family'));