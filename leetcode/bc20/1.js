/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function(arr) {
    function getBitNum(n) {
        let ans = 0;
        while (n > 0) {
            if (n % 2 === 1) ans++;
            n = Math.floor(n / 2);
        }
        return ans;
    }
    return arr.sort((a, b) => {
        const aBitNum = getBitNum(a);
        const bBitNum = getBitNum(b);
        if (aBitNum > bBitNum) return 1;
        else if (aBitNum < bBitNum) return -1;
        else {
            if (a > b) return 1;
            else return -1;
        }
    });
};
console.log(sortByBits([0,1,2,3,4,5,6,7,8]));
console.log(sortByBits([1024,512,256,128,64,32,16,8,4,2,1]));
console.log(sortByBits([10000,10000]));
console.log(sortByBits([2,3,5,17,7,11,13,19]));
console.log(sortByBits([10,100,1000,10000]));