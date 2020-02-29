class BST {
    getParent(i) {
        return Math.floor(i / 2);
    }
    getLeftChild(i) {
        return 2 * i;
    }
    getRightChild(i) {
        return 2 * i + 1;
    }
    isLeaf(i) {
        return this.getLeftChild(i) > this.nodes.length;
    }
    show() {
        console.log(this.nodes);
    }
    // return min
    top() {
        return this.nodes[0];
    }
    search() {

    }
    insert(n) {


    }
    constructor() {
        
        this.nodes = [];
    }
}