/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var constructMaximumBinaryTree = function(nums) {
    if (nums.length === 0) return null;
    const max = Math.max(...nums);
    const maxIndex = nums.findIndex((e) => e === max);
    //console.log(max);
    return {
        val: max,
        right: constructMaximumBinaryTree(nums.slice(maxIndex + 1, nums.length)),
        left: constructMaximumBinaryTree(nums.slice(0, maxIndex))
    };
};

const root = constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]);
console.log(root);
console.log(root.left);
console.log(root.right);