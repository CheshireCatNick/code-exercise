'use strict';

class DisjointSet {
    // create a set containing a
    makeSet(a) {
        this.parent['' + a] = a;
        this.size['' + a] = 1;
    }
    // find the representative element of set
    find(a) {
        if (this.parent['' + a] === undefined) return undefined;
        if (this.parent['' + a] === a) return a;
        // this is the original version
        // return this.find(this.parent['' + a]);
        // this is an optimized version that will make the tree shorter
        const result = this.find(this.parent['' + a]);
        this.parent['' + a] = result;
        return result;
    }
    // union two set that a and b is belong to
    union(a, b) {
        let pa = this.find(a);
        let pb = this.find(b);
        if (pa === undefined || pb === undefined) return;
        if (pa === pb) return;
        // make pb a smaller one
        if (this.size['' + pa] < this.size['' + pb]) {
            const temp = pa;
            pa = pb;
            pb = temp;
        }
        // merge a smaller one into a larger one
        this.parent['' + pb] = pa;
        this.size['' + pa] += this.size['' + pb];
    }
    getSize(a) {
        return this.size['' + this.find(a)];
    }
    constructor() {
        this.parent = {};
        this.size = {};
    }
}
// test
const ds = new DisjointSet();
ds.makeSet(1);
ds.makeSet(2);
ds.makeSet(3);
console.log(ds.find(1));
console.log(ds.find(2));

ds.union(1, 2);
console.log(ds.find(1));
console.log(ds.find(2));

ds.union(2, 3);
console.log(ds.find(3));

console.log(ds.size[1], ds.size[2], ds.size[3]);
console.log(ds.getSize(1), ds.getSize(2), ds.getSize(3));