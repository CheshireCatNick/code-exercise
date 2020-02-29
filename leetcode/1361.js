/**
 * @param {number} n
 * @param {number[]} leftChild
 * @param {number[]} rightChild
 * @return {boolean}
 */

let isVisited;
// return true if cycle is detected
function visit(i, leftChild, rightChild) {
    isVisited[i] = true;
    if (leftChild[i] === -1 && rightChild[i] === -1) {
        return false;
    }
    let leftCycle = false, rightCycle = false;
    if (leftChild[i] !== -1 && isVisited[leftChild[i]]) {
        // left cycle
        return true;
    }
    else if (leftChild[i] !== -1 && !isVisited[leftChild[i]]) {
        leftCycle = visit(leftChild[i], leftChild, rightChild);
        if (leftCycle) return true;
    }
    if (rightChild[i] !== -1 && isVisited[rightChild[i]]) {
        // right cycle
        return true;
    }
    else if (rightChild[i] !== -1 && !isVisited[rightChild[i]]) {
        rightCycle = visit(rightChild[i], leftChild, rightChild);
        if (rightCycle) return true;
    }
    return false;
}
var validateBinaryTreeNodes = function(n, leftChild, rightChild) {
    isVisited = new Array(n).fill(false);
    if (!visit(0, leftChild, rightChild)) {
        console.log(isVisited);
        for (let v of isVisited) {
            if (!v) return false;
        }
        return true;
    }
    else {
        return false;
    }
};
console.log(validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, -1, -1, -1]));