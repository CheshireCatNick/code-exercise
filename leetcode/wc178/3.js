/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {TreeNode} root
 * @return {boolean}
 */
function isMatched(head, root) {
    if (head === null) return true;
    if (root === null) return false;
    if (head.val === root.val) {
        return isMatched(head.next, root.left) || isMatched(head.next, root.right);
    }
    return false;
}

var isSubPath = function(head, root) {
    if (head === null) return true;
    if (root === null) return false;
    // check if linked list is matched from root
    if (isMatched(head, root)) {
        return true;
    }
    return isSubPath(head, root.left) || isSubPath(head, root.right);
};

console.log(isSubPath());