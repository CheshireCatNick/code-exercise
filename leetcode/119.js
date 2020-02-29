/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    if (rowIndex === 0) return [1];
    if (rowIndex === 1) return [1, 1];

    const middle = [rowIndex];
    for (let i = 0; i < rowIndex - 2; i++) {
        middle.push(middle[i] * (rowIndex - i - 1) / (i + 2));
    }
    return [1, ...middle, 1];
};