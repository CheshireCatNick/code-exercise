/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} threshold
 * @return {number}
 */
var numOfSubarrays = function(arr, k, threshold) {
    let sum = 0;
    for (let i = 0; i < k; i++) {
        sum += arr[i];
    }
    threshold *= k;
    let count = (sum >= threshold) ? 1 : 0;
    for (let i = k; i < arr.length; i++) {
        sum += arr[i];
        sum -= arr[i - k];
        if (sum >= threshold) count++;
    }
    return count;
};

console.log(numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4));
console.log(numOfSubarrays([1, 1, 1, 1, 1], 1, 0));
console.log(numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5));
console.log(numOfSubarrays([7, 7, 7, 7, 7, 7, 7], 7, 7));
console.log(numOfSubarrays([4, 4, 4, 4], 4, 1));
