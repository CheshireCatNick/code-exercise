/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const nIndex = [m, m, m, m];
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (grid[j][i] < 0) {
                nIndex[i] = j;
                break;
            }
        }
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        //console.log(nIndex[i]);
        ans += m - nIndex[i];
    }
    return ans;
};

console.log(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]));
console.log(countNegatives([[3,2],[1,0]]));
console.log(countNegatives([[1,-1],[-1,-1]]));
console.log(countNegatives([[-1]]));