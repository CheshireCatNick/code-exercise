'use strict';

const A = 'a'.charCodeAt(0);
function createGraph(arr) {
    function isNeightbor(sa, sb) {
        const stateA = Array(26).fill(0);
        const stateB = Array(26).fill(0);
        for (let c of sa) {
            stateA[c.charCodeAt(0) - A]++;
        }
        for (let c of sb) {
            stateB[c.charCodeAt(0) - A]++;
        }
        let count = 0;
        for (let i = 0; i < 26; i++) {
            count += Math.abs(stateA[i] - stateB[i]);
            if (count > 2) return false;
        }
        return count == 2;
    }
    for (let i = 0; i < arr.length; i++) {
        const sNode = {
            i: i,
            neigthBor: [],
        };
        for (let node of g) {
            if (isNeightbor(arr[node.i], arr[sNode.i])) {
                node.neigthBor.push(sNode.i);
                sNode.neigthBor.push(node.i);
            }
        }
        g.push(sNode);
    }
    return;
}
function dfs(start, isVisited) {
    isVisited[start] = true;
    //console.log(start, isVisited);
    for (let i = 0; i < g[start].neigthBor.length; i++) {
        const neigthBor = g[start].neigthBor[i];
        if (!isVisited[neigthBor]) {
            if (dfs(neigthBor, isVisited)) return true;
        }
    }
    for (let v of isVisited) {
        if (v == false) {
            isVisited[start] = false;
            return false;
        }
    }
    return true;
}
function solve(arr) {
    createGraph(arr);
    console.log(g);
    const isVisited = Array(arr.length).fill(false);
    for (let i = 0; i < arr.length; i++) {
        console.log('trying', i);
        if (dfs(i, isVisited)) {
            return true;
        }
    }
    return false;
}
let g = [];
console.log(solve(['abc', 'ccz', 'cbz', 'abd', 'cac']));
g = [];
console.log(solve(['aaa', 'aab', 'aac', 'aad']));
g = [];
console.log(solve(['aaa', 'aab', 'aba', 'abb']));