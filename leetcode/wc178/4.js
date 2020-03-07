/**
 * @param {number[][]} grid
 * @return {number}
 */
const dir = [
    [0, 0],
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0]
];
const isInRange = pos => 
    pos[0] >= 0 && pos[0] < m && pos[1] >= 0 && pos[1] < n;
const getNext = (pos, d) => [pos[0] + dir[d][0], pos[1] + dir[d][1]];
const isEnd = pos => pos[0] === m - 1 && pos[1] === n - 1;
// add path to queue and update cost
function go(grid, start, c) {
    cost[start[0]][start[1]] = c;
    if (isEnd(start)) {
        return true;
    }
    queue.push(start);
    let next = getNext(start, grid[start[0]][start[1]]);
    while (isInRange(next) && cost[next[0]][next[1]] === -1) {
        queue.push(next);
        cost[next[0]][next[1]] = c;
        if (isEnd(next)) return true;
        next = getNext(next, grid[next[0]][next[1]]);
    }
    return false;
}

const cost = [];
const queue = [];
let m, n;
var minCost = function(grid) {
    //console.log(grid);
    m = grid.length;
    n = grid[0].length;
    for (let i = 0; i < m; i++) {
        cost.push(new Array(n).fill(-1));
    }
    if (go(grid, [0, 0], 0)) {
        return cost[m - 1][n - 1];
    }
    while (queue.length > 0) {
        const start = queue.shift();
        //console.log('start', start);
        //console.log('queue', queue);
        // try other dir
        for (let d = 1; d <= 4; d++) {
            if (d === grid[start[0]][start[1]]) continue;
            const next = getNext(start, d);
            if (!isInRange(next) || cost[next[0]][next[1]] !== -1) continue;
            //console.log('go with', next);
            if (go(grid, next, cost[start[0]][start[1]] + 1)) {
                return cost[m - 1][n - 1];
            }
        }
    }
};

//console.log(minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]));
console.log(minCost([[1,1,3],[3,2,2],[1,1,4]]));
//console.log(minCost([[1,2],[4,3]]));
//console.log(minCost([[2,2,2],[2,2,2]]));
//console.log(minCost([[4]]));