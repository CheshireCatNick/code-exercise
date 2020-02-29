// min heap
class Heap {
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
    // return min and remove min
    pop() {
        const min = this.nodes[0];
        this.nodes[0] = this.nodes[this.nodes.length - 1];
        this.nodes.pop();
        let i = 1;
        while(!this.isLeaf(i)) {
            const left = this.getLeftChild(i);
            const right = this.getRightChild(i);
            // swap with the smallest one
            let si = (this.nodes[right - 1] < this.nodes[left - 1]) ?
                right : left;
            if (this.nodes[i - 1] <= this.nodes[si - 1]) {
                // parent is smaller than smallest child
                break;
            }
            const t = this.nodes[i - 1];
            this.nodes[i - 1] = this.nodes[si - 1];
            this.nodes[si - 1] = t;
            i = si;
        }
        return min;
    }
    insert(n) {
        this.nodes.push(n);
        let i = this.nodes.length;
        let parentI = this.getParent(i);
        while (i !== 0 && this.nodes[i - 1] < this.nodes[parentI - 1]) {
            const t = this.nodes[i - 1];
            this.nodes[i - 1] = this.nodes[parentI - 1];
            this.nodes[parentI - 1] = t;
            i = parentI;
            parentI = this.getParent(parentI);
        }
    }
    constructor() {
        // parent: i, starts from 1
        // left child: 2i
        // right child: 2i + 1
        this.nodes = [];
    }
}

const heap = new Heap();
heap.insert(30);
heap.insert(26);
heap.insert(15);
heap.insert(10);
heap.insert(25);
heap.show();
console.log(heap.pop());
heap.show();
console.log(heap.pop());
heap.show();
console.log(heap.pop());
heap.show();