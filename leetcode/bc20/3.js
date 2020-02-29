/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    let ans = 0;
    let abc = [0, 0, 0];
    let i = 0, j = 0;
    while (i < s.length) {
        abc[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
        while (abc[0] >= 1 && abc[1] >= 1 && abc[2] >= 1) {
            ans += s.length - i;
            abc[s.charCodeAt(j) - 'a'.charCodeAt(0)]--;
            j++;
        }
        i++;
    }
    return ans;
};
console.log(numberOfSubstrings('abcabc'));
console.log(numberOfSubstrings('aaacb'));
console.log(numberOfSubstrings('abc'));
