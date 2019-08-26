/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

function dfs(root, sum) {
    if (root === null) return 0;
    let value = dfs(root.right, sum);
    //console.log(root.val, value, sum);
    root.val += value;
    if (root.right === null) root.val += sum;
    //console.log(root.val);
    value = dfs(root.left, root.val);
    return (root.left === null) ? root.val : value;
}
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var bstToGst = function(root) {
    dfs(root, 0);
    return root;
};

const n8 = {
    right: null,
    left: null,
    val: 8
};
const n7 = {
    right: n8,
    left: null,
    val: 7
};
const n5 = {
    right: null,
    left: null,
    val: 5
};
const n6 = {
    right: n7,
    left: n5,
    val: 6
};
const n3 = {
    right: null,
    left: null,
    val: 3
};
const n0 = {
    right: null,
    left: null,
    val: 0
};
const n2 = {
    right: n3,
    left: null,
    val: 2
};
const n1 = {
    right: n2,
    left: n0,
    val: 1
};
const n4 = {
    right: n6,
    left: n1,
    val: 4
};
bstToGst(n4);
console.log(n8.val);
console.log(n7.val);
console.log(n6.val);
console.log(n5.val);
console.log(n4.val);
console.log(n3.val);
console.log(n2.val);
console.log(n1.val);
console.log(n0.val);