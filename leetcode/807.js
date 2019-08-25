/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxIncreaseKeepingSkyline = function(grid) {
    const rowMax = [];
    const colMax = [];
    for (let i = 0; i < grid.length; i++) {
        rowMax.push(0);
        for (let j = 0; j < grid[i].length; j++) {
            rowMax[i] = (grid[i][j] > rowMax[i]) ? grid[i][j] : rowMax[i];
        }
    }
    for (let i = 0; i < grid[0].length; i++) {
        colMax.push(0);
        for (let j = 0; j < grid.length; j++) {
            colMax[i] = (grid[j][i] > colMax[i]) ? grid[j][i] : colMax[i];
        }
    }
    //console.log(rowMax, colMax);
    //const newGrid = [];
    let addedHeight = 0;
    for (let i = 0; i < grid.length; i++) {
        //const newRow = [];
        for (let j = 0; j < grid[i].length; j++) {
            addedHeight += Math.min(rowMax[i], colMax[j]) - grid[i][j];
        }
        //newGrid.push(newRow);
    }
    //console.log(newGrid);
    return addedHeight;
};
maxIncreaseKeepingSkyline([
    [3, 0, 8, 4], 
    [2, 4, 5, 7],
    [9, 2, 6, 3],
    [0, 3, 1, 0]
]);