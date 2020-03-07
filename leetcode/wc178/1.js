/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    let count = new Array(101).fill(0);
    for (let n of nums) {
        count[n]++
    }
    let sum = 0;
    const sums = new Array(101).fill(0);
    for (let i = 0; i <= 100; i++) {
        sums[i] = sum;
        sum += count[i];
    }
    const ans = [];
    for (let n of nums) {
        ans.push(sums[n]);
    }
    return ans;
};

console.log(smallerNumbersThanCurrent([8, 1, 2, 2, 3]));
console.log(smallerNumbersThanCurrent([6, 5, 4, 8]));
console.log(smallerNumbersThanCurrent([7, 7, 7, 7]));