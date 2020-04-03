var luckyNumbers  = function(matrix) {
    const state = [];
    for (let i = 0; i < matrix.length; i++) {
        state.push(Array(matrix[0].length).fill(0));
    }
    for (let i = 0; i < matrix.length; i++) {
        let m = 1000000;
        for (let j = 0; j < matrix[0].length; j++) {
            m = (matrix[i][j] < m) ? matrix[i][j] : m;
        }
        for (let j = 0; j < matrix[0].length; j++) {
            if (matrix[i][j] === m) state[i][j]++;
        }
    }
    const ans = [];
    for (let j = 0; j < matrix[0].length; j++) {
        let m = -1;
        for (let i = 0; i < matrix.length; i++) {
            m = (matrix[i][j] > m) ? matrix[i][j] : m;
        }
        for (let i = 0; i < matrix.length; i++) {
            if (matrix[i][j] === m && state[i][j] === 1) {
                ans.push(matrix[i][j])
            }
        }
    }
    return ans;
};

console.log(luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]));